# Known chapter_master_id values

**Always confirm live via `core/check_master_id.py <plan.json>` before
uploading.** This table is sourced from the base plan JSONs in a separate
checkout (`lp_pipeline`) as of this writing. It goes stale the moment a new
chapter is registered or an id is reissued, and `upload_lp.py` will attach
good content to the wrong chapter and still answer `success: true` if this
table is wrong and nobody checked. Treat every number below as "last known",
never as ground truth.

## Grade 5

Only verified ids are listed.

| Chapter | chapter_master_id | subject_ref_id |
|---|---|---|
| 1 We the Travellers - I | 145 | 80 |

## Grade 6

| Chapter | Master id |
|---|---|
| ch1 | 185 |
| ch2 | 186 |
| ch3 | 187 |
| ch4 | 188 |
| ch5 | 189 |
| ch6 | 190 |
| ch7 | 191 |
| ch8 | 192 |
| ch9 | 193 |
| ch10 | 194 |

Contiguous 185-194, ch1-ch10 in order.

## Grade 7 - the Part II numbering trap

Part I has 8 chapters. **Part II Ch N is built and filed as `maths7_ch(8+N)`**
- the user names a chapter by its Part II number, the repo folder and master
id continue the Part I count. "Class 7 Ch 2" = Part II Ch 2 = `maths7_ch10` =
master id 66, not "ch2".

| Chapter folder | Master id | Part II number (if any) |
|---|---|---|
| ch1 | 53 | - |
| ch2 | 58 | - |
| ch3 | 59 | - |
| ch4 | 60 | - |
| ch5 | 61 | - |
| ch6 | 62 | - |
| ch7 | 63 | - |
| ch8 | 64 | - |
| ch9 | 65 | Part II Ch 1 (Geometric Twins) |
| ch10 | 66 | Part II Ch 2 (Operations with Integers) |
| ch11 | 67 | Part II Ch 3 |
| ch12 | 68 | Part II Ch 4 |
| ch13 | 69 | Part II Ch 5 |
| ch14 | 70 | Part II Ch 6 |
| ch15 | 71 | Part II Ch 7 (Finding the Unknown) |

Note the gap: ch1=53, then ch2=58 (not 54). That gap is real in the source,
not a transcription error - do not smooth it into a clean run of 53-66.

## Grade 8 - the equivalent trap, a different offset

Part I has 7 chapters. **Part II Ch N is built and filed as `maths8_ch(7+N)`**
- a different offset from Grade 7's. "Class 8 Ch 1" (Part II) = `maths8_ch8`
= master id 202, not "ch1".

| Chapter folder | Master id | Part II number (if any) |
|---|---|---|
| ch1 | 195 | - |
| ch2 | 196 | - |
| ch3 | 197 | - |
| ch4 | 198 | - |
| ch5 | 199 | - |
| ch6 | 200 | - |
| ch7 | 201 | - |
| ch8 | 202 | Part II Ch 1 (Fractions in Disguise) |
| ch9 | 203 | Part II Ch 2 (The Baudhāyana-Pythagoras Theorem) |
| ch10 | 204 | Part II Ch 3 (Proportional Reasoning-2) |
| ch11 | 205 | - |
| ch12 | 206 | - |
| ch13 | 207 | - |
| ch14 | 208 | - |

Contiguous 195-208, ch1-ch14 in order; the Part II label is just a naming
convention on top of ch8-ch10, not a different id range.

## Grade 9

Two folders in the source checkout refer to the **same live chapters**: the
older `Class 9/maths9_ch<N>/` working copy and the newer `Std_9/maths9_ch<N>/
new_design/` rebuild share identical master ids for the chapters both cover
(ch5 = 230, ch6 = 231 in both). Treat them as one id space, not two books.

| Chapter | Master id |
|---|---|
| ch1 | 226 |
| ch2 | 227 |
| ch3 | 228 |
| ch4 | 229 |
| ch5 | 230 |
| ch6 | 231 |
| ch7 | 232 |
| ch8 | 233 |

Contiguous 226-233, ch1-ch8 in order.

## Grade 10

| Chapter | Master id |
|---|---|
| ch1 | 158 |
| ch2 | 159 |
| ch3 | 160 |
| ch4 | 161 |
| ch5 | 162 |
| ch6 | 163 |
| ch7 | 164 |
| ch8 | 165 |
| ch9 | 166 |
| ch10 | 167 |
| ch11 | 168 |
| ch12 | 169 |
| ch13 | 170 |
| ch14 | 171 |

Contiguous 158-171, ch1-ch14 in order. As of this writing no Grade 10 chapter
had been rebuilt in the new design yet - verify before assuming any of these
are still accurate.

## Why this table can go stale

- A chapter can be re-registered under a new master id if its `lp2_chapters`
  row is ever dropped and recreated.
- A new chapter (Grade 6-10, any Part) gets the next free id when it is first
  issued - this table will simply not have it yet.
- `upload_lp.py` reads `chapter_master_id` from the plan JSON itself, never
  from a table like this one; this table exists only to help a human sanity-
  check a plan before building it, and to catch a Part-II-numbering slip
  before it reaches the uploader.

Run `core/check_master_id.py <plan.json>` against the live database before
every upload. It compares the plan's `chapter_master_id`, `subject_ref_id`
and `medium_id` against the live `chapterMaster` row and fails loudly on any
disagreement - that is the actual gate, not this file.
