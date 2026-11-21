# Diagram trigger word — cross-standard companion note

Nov 18, 2026 · @HALAJI

## What this is, and what it isn't

This note describes one small, optional convention from the Std 9/10 maths-chapter pipeline: a shared word used to tag diagram/figure images so any team's fetch tooling can pull every diagram out of the dataset with one search, across standards, chapters and schemas.

It is **not** a replacement for your own rules on how many images a question or answer gets, how your media objects are structured, or how you decide a question needs a figure at all. Adopt only the two pieces below — the naming token and the figure-content guidance — and keep everything else about your pipeline as it already is. If a rule here ever conflicts with something your schema already enforces, your rule wins; skip the piece that conflicts and keep the rest.

Who should read this: anyone building or maintaining the question/solution JSON for a different standard, who wants their diagram images to be findable the same way ours are, without re-architecting their own media schema to match ours.

## The trigger-word convention

- **Word:** `DIAGRAM` — all caps, exact spelling, never abbreviated or translated, whatever language the rest of your content is in.
- **Where it goes:** the first token of the image's `name` (or display-title / label field — whatever your schema calls the human-readable name of a media item), followed by `·` (space, middle dot, space), then your existing label unchanged. Example: `DIAGRAM · Q7 given figure`, `DIAGRAM · Q7 solution figure`.
- **What gets it:** only an image that is itself a diagram/figure of the question or the solution — never a solution video, an icon, a formula screenshot, or any other image a question/answer object might carry.
- **What doesn't need to change:** your concept IDs, your field names, how many images you attach per question, or how you decide a question needs a figure. The word is additive — it rides on top of whatever naming you already use for that image.
- **Why a word in the name, not a new field:** a plain string search works across schemas that don't share a common structure. If your schema already has a `tags` or `role`-style field, adding `"diagram"` there too is a welcome extra, not a substitute — the word in the name is the one guarantee every consumer can rely on.

## The figure-content rule (independent of how many images you use)

However many images your schema allows per question or answer, this rule governs what goes inside the one(s) that are a diagram of the question or the solution:

- **A question's figure shows only what the question gives.** If the question includes a pre-drawn diagram, a graph, or a pre-marked shape, that image contains exactly what's printed in the source text — no construction lines, no labels the student hasn't been given yet, nothing solved.
- **A solution's figure shows the complete final state.** Whatever drawing, plotting, or construction the solution involves, the figure tied to the solution shows every point, label, line and mark the finished answer needs — not an intermediate step, not a blank canvas, the end result.
- **If a question has no given figure, don't invent a question-figure.** A "blank" or placeholder image is worse than none — it implies something was given when nothing was.
- **Labels stay consistent between a question's figure and its solution's figure.** Points named in the given figure keep the same letters in the solution's figure; new points the solution introduces continue the same labelling scheme (next letter, matching case) rather than restarting it.

This rule says nothing about whether you use one image, two, or a sequence of step-by-step images for a solution — it only says: wherever a figure's job is to represent the given state, keep it to the given state; wherever a figure's job is to represent the final state, make it complete.

## Adopting it without conflicting with your own image-count rule

**If your schema already uses one image per question-object and one per answer-object** (same shape as the Std 9 pipeline this note comes from): just prefix whichever of those is a diagram with ` DIAGRAM ·  `. Nothing else changes.

**If your schema allows several images per question or answer** (step-by-step construction frames, multiple views, a given-figure plus a worked-figure both attached to the same object): prefix *every* one of them that is itself a diagram/figure with ` DIAGRAM ·  `, not just the last one. A consumer searching for `DIAGRAM` should get every figure image you have, and your own metadata (sequence number, step label, whatever you already use) still tells them the order or role among themselves — the trigger word only says "this is a figure," it doesn't claim to be the only one.

**If your schema has no given-figure/worked-figure distinction at all** (e.g. a single image per question that already shows the full worked solution): still worth tagging that image `DIAGRAM · …` so it's findable — the figure-content rule above is guidance for anyone who does separate the two, not a requirement that you start separating them.

**If you use a different image-count or staging convention than any of the above**: the trigger word still applies the same way — tag whichever image(s) in your own structure are diagrams/figures, however many there are, however they're organised.

## Summary

Prefix the `name` of every diagram/figure image — question-side or solution-side, however many you have — with ` DIAGRAM ·  `, exact spelling, first token, nothing else gets it. That's the whole convention: one word, one search, works across standards without touching your own image-count rules. Separately, if you do distinguish a question's figure from a solution's figure, keep the question's figure to exactly what's given and the solution's figure to the complete final state — that's a content rule, not a counting rule, and applies whether you use one image or several.
