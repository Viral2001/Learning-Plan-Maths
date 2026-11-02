# 04. Class 9/10 variant

Learned from `maths9_ch5` (circles) and `maths9_ch6` (perimeter and area).
Where this conflicts with anything in `docs/00`/`docs/01`, this wins for a
Class 9 or 10 chapter.

Rules 1-8 are mechanically checkable and belong to `gates/theorem_variant.py`.
Rules 9-12 are process notes for a human to apply - they are about what to
ask the user before building, not something a gate can verify from the plan
alone.

## Mechanically checkable (gates/theorem_variant.py)

1. **A tool sits at every theorem**, popping the first time the student
   meets the statement: statement, then a prediction, then the tool. A
   theorem and its converse share one tool.
2. **One video and one hint-free question image per exercise question.**
   The image shows the statement only - no hints, no working, no answer. A
   question the book pairs with its own figure shows only that figure.
3. **End-of-chapter exercises get their own topic, just before the
   Summary**, with exactly 2 concepts - core and starred - kept apart. The
   student attempts first; hint, solution and video open afterwards.
4. **Enrichment blocks carry no objective.** `objective_id` is null,
   `objective_ids` is empty, and no other objective in the plan mentions an
   enrichment concept either.
5. **A theorem concept's objective names the theorem explicitly** - e.g.
   "State Theorem 4, that the line joining the centre to the midpoint of a
   chord is perpendicular to the chord, and test it..." - not a generic
   "understand the theorem."
6. **No Fig./section/theorem-number references anywhere in authored text.**
   This is stricter than the base no-book-numbers rule (`docs/02`): the base
   rule allows a bare theorem number like "Theorem 7" to survive; the
   Class 9/10 variant does **not** allow even that. Name the theorem instead
   ("the theorem about tangents from an external point"), never "Theorem 7."
7. **No scaffolding labels in rendered text.** No "Textbook text
   (verbatim)", "On the board", "Predict first", "Discussion", or any other
   internal category name leaking into what the student reads. These stay
   as machine metadata (`block_kind`) only.
8. **Exercise sets get their own name, never NCERT's.** "Exercise Set 5.2"
   becomes something like "Chords and the Centre"; a practice concept is
   named "Practice: <that new name>."

## Process notes (ask the user; not gate-checkable)

9. **Default a new tool to a spec, not a built tool**, unless the user
   explicitly asks for it to be built. Building every tool for a theorem
   chapter is expensive; most ship as specs first.

10. **Check `/chapter/<id>/versions` before any rebuild.** Carry forward any
    live, built asset (image, tool, rendered video) through pinning
    (`core/published_media.py`) rather than replacing it with a fresh
    placeholder - but drop any carried asset whose own fields mention NCERT
    or "textbook", even if it is otherwise usable.

11. **Never merge archived or legacy media into a rebuild.** This has been
    accidentally reintroduced more than once on these chapters - restate it
    to yourself immediately before every Class 9/10 upload, not only when
    first briefed. A rebuild is built from the chapter's own authored
    content and whatever live assets step 10 pins forward; nothing from an
    archived or superseded version is ever attached on top.

12. **Upload straight after the dry-run check**, same Phase-2-only
    convention as Class 6-8 (`docs/01`). There is no separate Class 9/10
    upload path and no `_V3` step here either.

## Reference

`maths9_ch5` (circles, "I'm Up and Down, and Round and Round") and
`maths9_ch6` (Measuring Space: Perimeter and Area) are the two chapters this
variant was learned from, in the older checkout this pipeline's docs were
condensed from.
