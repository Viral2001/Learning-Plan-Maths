"""Local editor for the code behind question images.

    python core/image_editor/server.py chapters/maths8_ch9_v3_question_images
    then open http://127.0.0.1:8765

Render runs arbitrary Python, so the server binds to 127.0.0.1 only and refuses
any request whose Host or Origin is not this server.
"""
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bucket  # noqa: E402

HOST = "127.0.0.1"
PORT = 8765
ALLOWED_HOSTS = {"%s:%d" % (HOST, PORT), "localhost:%d" % PORT}
ALLOWED_ORIGINS = {"http://" + h for h in ALLOWED_HOSTS}
MAX_BODY = 1024 * 1024

lock = threading.Lock()


class Chapter:
    def __init__(self, folder):
        self.folder = os.path.abspath(folder)
        self.manifest_path = os.path.join(self.folder, "manifest.json")
        self.drafts = os.path.join(self.folder, ".drafts")
        self.backups = os.path.join(self.folder, ".bak")
        spec = importlib.util.spec_from_file_location("chapter_render",
                                                      os.path.join(self.folder, "render.py"))
        self.render = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.render)
        with open(os.path.join(self.folder, "plan_text.json"), encoding="utf-8") as f:
            self.plan_text = json.load(f)

    def manifest(self):
        with open(self.manifest_path, encoding="utf-8") as f:
            return json.load(f)

    def write_manifest(self, data):
        tmp = self.manifest_path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, self.manifest_path)

    def entry(self, image_id, data=None):
        for e in (data or self.manifest())["images"]:
            if e["id"] == image_id:
                return e
        raise KeyError("Unknown image: %s" % image_id)

    def code_path(self, entry):
        return os.path.join(self.folder, "scenes", entry["scene_file"])

    def png_path(self, entry):
        return os.path.join(self.folder, "png", entry["id"] + ".png")

    def draft_png(self, entry):
        return os.path.join(self.drafts, entry["id"] + ".png")

    def draft_code(self, entry):
        return os.path.join(self.drafts, entry["scene_file"])

    def set_status(self, image_id, **fields):
        data = self.manifest()
        self.entry(image_id, data).update(fields)
        self.write_manifest(data)


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def render(ch, image_id, code):
    """Render code to a draft PNG. The saved code and PNG are not touched."""
    entry = ch.entry(image_id)
    os.makedirs(ch.drafts, exist_ok=True)
    with open(ch.draft_code(entry), "w", encoding="utf-8", newline="\n") as f:
        f.write(code)
    ok, log = ch.render.render_one(entry, code_path=ch.draft_code(entry),
                                   out_path=ch.draft_png(entry))
    if ok:
        with open(ch.draft_png(entry) + ".sha", "w") as f:
            f.write(sha(code))
    return {"ok": ok, "log": log[-6000:]}


def save(ch, image_id, code):
    """Keep the rendered draft. Refused unless this exact code rendered clean."""
    entry = ch.entry(image_id)
    sha_path = ch.draft_png(entry) + ".sha"
    if not os.path.exists(sha_path) or open(sha_path).read() != sha(code):
        return {"ok": False, "log": "Render this code first, then save."}
    os.makedirs(ch.backups, exist_ok=True)
    shutil.copy2(ch.code_path(entry), os.path.join(ch.backups, entry["scene_file"] + ".bak"))
    shutil.copy2(ch.png_path(entry), os.path.join(ch.backups, entry["id"] + ".png.bak"))
    with open(ch.code_path(entry), "w", encoding="utf-8", newline="\n") as f:
        f.write(code)
    os.replace(ch.draft_png(entry), ch.png_path(entry))
    os.remove(sha_path)
    ch.set_status(image_id, status="draft")
    return {"ok": True}


def approve(ch, image_id):
    ch.set_status(image_id, status="approved")
    return {"ok": True}


def upload(ch, image_id):
    """Send one approved image and its code. The URLs in the plan do not change."""
    data = ch.manifest()
    entry = ch.entry(image_id, data)
    if entry["status"] != "approved":
        return {"ok": False, "log": "Approve this image before uploading."}
    with open(ch.png_path(entry), "rb") as f:
        png = f.read()
    with open(ch.code_path(entry), "rb") as f:
        code = f.read()
    folder = data["key_dir"]
    sizes = bucket.upload(folder, [(entry["id"] + ".png", png)])
    sizes.update(bucket.upload(folder + "/code", [(entry["id"] + ".py", code)]))
    ch.set_status(image_id, uploaded_sha=hashlib.sha256(png + code).hexdigest())
    return {"ok": True, "sizes": sizes, "url": bucket.public_url(folder, entry["id"] + ".png")}


def listing(ch):
    images = []
    for e in ch.manifest()["images"]:
        png = ch.png_path(e)
        images.append(dict(e, version=int(os.path.getmtime(png)) if os.path.exists(png) else 0,
                           plan=ch.plan_text.get(e["concept_id"], {})))
    return {"images": images}


class Handler(BaseHTTPRequestHandler):
    chapter = None

    def log_message(self, *args):
        pass

    def send(self, code, body, ctype="application/json; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, code, obj):
        self.send(code, bucket.dump(obj).encode("utf-8"))

    def trusted(self):
        if self.headers.get("Host") not in ALLOWED_HOSTS:
            return False
        if self.command == "POST":
            return self.headers.get("Origin") in ALLOWED_ORIGINS
        return self.headers.get("Origin") in (None, *ALLOWED_ORIGINS)

    def do_GET(self):
        if not self.trusted():
            return self.send_json(403, {"ok": False, "log": "Refused."})
        ch = self.chapter
        path = self.path.split("?", 1)[0]
        try:
            if path == "/":
                with open(os.path.join(HERE, "index.html"), "rb") as f:
                    return self.send(200, f.read(), "text/html; charset=utf-8")
            if path == "/api/images":
                return self.send_json(200, listing(ch))
            if path.startswith("/api/code/"):
                entry = ch.entry(path[len("/api/code/"):])
                with open(ch.code_path(entry), encoding="utf-8") as f:
                    return self.send_json(200, {"code": f.read()})
            if path.startswith("/png/") or path.startswith("/draft/"):
                _, kind, name = path.split("/", 2)
                entry = ch.entry(name[:-4])
                target = ch.png_path(entry) if kind == "png" else ch.draft_png(entry)
                with open(target, "rb") as f:
                    return self.send(200, f.read(), "image/png")
        except (KeyError, FileNotFoundError) as e:
            return self.send_json(404, {"ok": False, "log": str(e)})
        self.send_json(404, {"ok": False, "log": "Not found."})

    def do_POST(self):
        if not self.trusted():
            return self.send_json(403, {"ok": False, "log": "Refused."})
        length = int(self.headers.get("Content-Length") or 0)
        if length > MAX_BODY:
            return self.send_json(413, {"ok": False, "log": "Code is too large."})
        action = self.path.rsplit("/", 1)[-1]
        ch = self.chapter
        try:
            body = json.loads(self.rfile.read(length) or b"{}")
            image_id = body["id"]
            with lock:
                if action == "render":
                    out = render(ch, image_id, body["code"])
                elif action == "save":
                    out = save(ch, image_id, body["code"])
                elif action == "approve":
                    out = approve(ch, image_id)
                elif action == "upload":
                    out = upload(ch, image_id)
                else:
                    return self.send_json(404, {"ok": False, "log": "Not found."})
        except KeyError as e:
            return self.send_json(400, {"ok": False, "log": "Bad request: %s" % e})
        except Exception as e:
            return self.send_json(500, {"ok": False, "log": "%s: %s" % (type(e).__name__, e)})
        self.send_json(200, out)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    Handler.chapter = Chapter(sys.argv[1])
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print("Open http://%s:%d" % (HOST, PORT), flush=True)
    server.serve_forever()


if __name__ == "__main__":
    sys.exit(main())
