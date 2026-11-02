# 03. Known chapter_master_id values

The table lives in one place: `upload/chapter_master_ids.md`. Read it there,
not here - this page is a pointer, not a second copy, so the two can never
drift apart and disagree.

It lives under `upload/` rather than `docs/` because it is the ground
operational fact `upload_lp.py`'s user needs at the moment of uploading, next
to the other upload tooling. This page exists under `docs/` only so the
onboarding doc set (`00` through `04`) is a complete, self-contained
sequence without a gap at "where are the ids."

Whichever file you are reading, the real rule is the same one stated in
both: **confirm live with `core/check_master_id.py <plan.json>` before every
upload.** Neither file is a substitute for that check.
