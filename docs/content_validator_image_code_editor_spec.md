# Content validator: edit image code on double-click

## Goal

A reviewer double-clicks an image in the content validator, sees the code that made it, edits the code, previews the new image and saves it. Reviewers can then fix a wrong label or layout without waiting for an engineer.

The local prototype already does this outside the validator. This spec covers moving it into the validator.

## What exists today

| Piece | Location |
| --- | --- |
| Working prototype (server and page) | `core/image_editor/` |
| Bucket upload and size check | `core/image_editor/bucket.py` |
| Trial chapter: 46 images with code | `chapters/maths8_ch9_v3_question_images/` |
| Render call | `render_one()` in that folder's `render.py` |
| Live plan with the new fields | `cbse_eng_maths8_ch9_V3` v13 on staging, master 203, phase 3 |

To run the prototype:

```
python core/image_editor/server.py chapters/maths8_ch9_v3_question_images
```

Then open `http://127.0.0.1:8765`.

The prototype needs a local Manim 0.20 install and MiKTeX. It runs code on the reviewer's own machine, so its security model does not carry over to a hosted service.

## Plan data

Each image node in `topic.media` that has code carries two new fields:

```json
{
  "id": "M3.S11.T11.C46.IMG1",
  "image_url": ".../image_v5/M3.S11.T11.C46.IMG1.png",
  "image_role": "question",
  "render_source": {
    "engine": "manim",
    "scene": "C46_q",
    "code_url": ".../image_v5/code/M3.S11.T11.C46.IMG1.py",
    "style_url": ".../image_v5/code/_style.py"
  }
}
```

- `image_role` is `question` or `solution`. Nodes without it are ordinary images.
- `render_source.engine` is `manim` today. Keep it as a field so LaTeX or SVG engines can be added later.
- `render_source.scene` is the class to render.
- `style_url` is a shared helper file. Each scene runs `from _style import *`, so it must sit beside the scene at render time.
- Code is a `.py` file in the bucket, not text in the plan, because plan dash gates can change strings and would corrupt code.

## User flow

1. An image with `render_source` shows an edit hint. Other images behave as they do now.
2. Double-click opens a full-screen editor: code on the left, image on the right, and the plan's question, steps and answer below the image.
3. **Render** shows a preview, or the error log if the code fails. Nothing saved changes.
4. **Save** is enabled only when the current code has rendered successfully. It keeps the previous code and PNG.
5. **Approve** records that a person checked the image. Any later save clears the approval.

## Backend

### `POST /images/render`

Input: chapter id, media id, code. Output: preview URL, or the log.

The service runs code written by users, so it needs:

- An isolated container per render, with no network and no access to secrets.
- A read-only filesystem except for a scratch folder.
- A timeout of 180 seconds, plus CPU and memory limits.
- A login check, limited to reviewer roles.
- One render at a time per user. A render at 1920x1080 took a few seconds locally.

The image needs Manim 0.20, a TeX distribution and the fonts used by `_style.py`.

### `POST /images/save`

Input: chapter id, media id, code. The server must check that a successful render exists for the same code hash, then:

1. Copy the current PNG and `.py` to a versioned path.
2. Write the new PNG and `.py` to the same keys.
3. Read back the stored size with a cache-buster query parameter.
4. Record who saved, when, and the code hash.

### Approval

Store this per image: `draft` or `approved`, with reviewer and time. Saving sets it back to `draft`.

## Open decisions

1. **Plan version on save.** The URL stays the same, so saving an image does not need a new plan version. We recommend keeping image saves out of plan versions, because a save inside the validator can renumber concept ids. Please confirm this against the validator's save code.
2. **CDN cache.** Objects are served with `max-age=3600`, so a replaced image can look old for up to an hour. Either purge on save or add a version query to `image_url`. The validator should preview from the render output, not the CDN URL.
3. **Unknown fields.** v13 imported with `image_role` and `render_source`, and the API returned them unchanged. Please confirm that a validator save keeps them too.

## Player requirement

A `solution` image must stay hidden until the student has attempted the question. In the plan both images are linked to the same concept through `media_ids`, in the order `[IMG1, VID1, IMG2]`: question image, video, solution image. The player code was not available when this was built, so this behaviour is not confirmed. It needs a check on v13 and, if the player shows every image at once, a change that gates on `image_role`.

## Acceptance checks

- Double-click opens the code for that exact image.
- A failed render shows the log and leaves the saved image unchanged.
- Save is refused for code that has not rendered.
- After a save, the bucket holds the new size and the old version can be restored.
- A saved image loses its approval.
- Code in the render service cannot reach the network or read secrets.
- `render_source` and `image_role` survive a validator save.
