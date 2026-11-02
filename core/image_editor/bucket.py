"""Upload files to the learning_plan_assets bucket and read their stored size back."""
import io
import json
import time
import urllib.error
import urllib.request
import uuid

BUCKET = "learning_plan_assets"
BASE = "https://staging.singularity-learn.com"
PUBLIC = "https://media.singularity-learn.com/" + BUCKET
DIRECT = "https://storage.googleapis.com/" + BUCKET

TYPES = {".png": "image/png", ".py": "text/plain; charset=utf-8"}


def _multipart(fields, files):
    boundary = "----image" + uuid.uuid4().hex
    out = io.BytesIO()
    for name, value in fields:
        out.write(('--%s\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n'
                   % (boundary, name, value)).encode("utf-8"))
    for filename, data in files:
        ctype = TYPES[filename[filename.rindex("."):]]
        out.write(('--%s\r\nContent-Disposition: form-data; name="files"; filename="%s"\r\n'
                   "Content-Type: %s\r\n\r\n" % (boundary, filename, ctype)).encode("utf-8"))
        out.write(data)
        out.write(b"\r\n")
    out.write(("--%s--\r\n" % boundary).encode("utf-8"))
    return "multipart/form-data; boundary=%s" % boundary, out.getvalue()


def stored_size(key):
    """Size GCS holds for key, or None. The cache-buster matters on a re-upload."""
    url = "%s/%s?cb=%d" % (DIRECT, key, time.time() * 1000)
    req = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return int(r.headers.get("x-goog-stored-content-length") or -1)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def upload(folder, files):
    """files: [(filename, bytes)]. Each one is checked on GCS afterwards.

    Returns {filename: stored size}. Raises if any file did not land at its full size.
    """
    ctype, body = _multipart([("folder_name", folder), ("bucket_name", BUCKET)], files)
    req = urllib.request.Request(BASE + "/agentapi/api/topics/upload", data=body,
                                 headers={"Content-Type": ctype})
    with urllib.request.urlopen(req, timeout=180) as r:
        reply = r.read().decode("utf-8", "replace")
    sizes = {}
    for filename, data in files:
        size = stored_size(folder + "/" + filename)
        if size != len(data):
            raise RuntimeError("%s: sent %d bytes, bucket holds %s. Reply: %s"
                               % (filename, len(data), size, reply[:500]))
        sizes[filename] = size
    return sizes


def public_url(folder, filename):
    return "%s/%s/%s" % (PUBLIC, folder, filename)


def dump(obj):
    return json.dumps(obj, ensure_ascii=False)
