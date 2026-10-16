# Eval

Three tasks, each built three ways for a fictional invoicing product called Tally (all names, prices and numbers are sample data):

- `src/<task>_baseline.html`: a typical first-pass generated page.
- `src/<task>_A.html`: the baseline after a "make it better" pass with no skill.
- `src/<task>_B.html`: the baseline rebuilt by applying this skill.

Tasks: `landing` (SaaS landing page, 1280 px), `pricing` (pricing page, 1280 px), `mobile` (mobile dashboard and settings screen, 390 px).

`score.py` renders each page in headless Chromium, saves full-page screenshots, and counts tells from computed styles. Run with `pip install playwright pillow && python -m playwright install chromium && python score.py`.

## Automatic counts (A vs B)

| Task | Version | Blue/purple gradients | Resting shadows | Pill badges | Emoji | Glass surfaces | Distinct radii (px) | Font sizes | Spacing values | Title / body ratio | Filled buttons above fold |
|---|---|---|---|---|---|---|---|---|---|---|---|
| landing | A | 3 | 8 | 4 | 8 | 3 | 1 (24) | 8 | 18 | 2.13 | 1 |
| landing | B | 0 | 0 | 0 | 0 | 0 | 2 (6,12) | 6 | 7 | 3.5 | 1 |
| pricing | A | 6 | 8 | 4 | 17 | 5 | 1 (28) | 8 | 14 | 2.25 | 3 |
| pricing | B | 0 | 0 | 0 | 0 | 0 | 2 (6,12) | 6 | 9 | 3.5 | 1 |
| mobile | A | 2 | 5 | 4 | 9 | 5 | 1 (24) | 8 | 10 | 1.73 | 0 |
| mobile | B | 0 | 0 | 0 | 0 | 0 | 2 (6,12) | 4 | 5 | 2.86 | 1 |

Counted by hand from the screenshots:

| Task | Version | Equal-size card grid | Centered hero with two buttons | Focal element |
|---|---|---|---|---|
| landing | A | yes (3 icon cards) | yes | none clear, gradient competes with headline |
| landing | B | no (7/5 split, one feature ranked first) | no (left aligned, 1 button + text link) | headline beside a product view |
| pricing | A | yes (3 equal plans, 3 identical gradient buttons) | yes | none, all three buttons equally loud |
| pricing | B | no (4/5/4 columns, Pro taller and tinted) | no | Pro price at 56 px, the only filled button |
| mobile | A | yes (3 equal emoji stat tiles) | n/a | none, header gradient and tiles compete |
| mobile | B | no (one large number, one breakdown bar) | n/a | $12,480 at 40 px with one action |

## Expert score (1 to 10)

| Task | A | B | Reasons |
|---|---|---|---|
| landing | 3 | 8 | A added more gradient, gradient text, glass cards and a "New" pill to every card; nothing says what the product is best at. B states the job in the headline, shows sample product data in the first viewport, and ranks reminders above other features. |
| pricing | 3 | 8 | A has three identical gradient buttons and a glowing card; the recommendation is carried only by an emoji pill. B uses one filled button on the recommended plan, uneven column widths, and a larger price for Pro; FAQ copy is left aligned and readable. |
| mobile | 3 | 8 | A: LIVE pill, emoji on every row, pill values, gradient toggle, glass over a flat gradient. B: one number, a paid/due/late bar, one action tied to the data, and a plain grouped settings list with standard toggles. |

B beat A on every task and met every checklist target except spacing on pricing (9 distinct values vs a target of 8 or fewer). The A versions also show the problem the skill targets: the "make it better" pass increased tells (landing pill badges 1 to 4, glass 0 to 3; pricing emoji 14 to 17) instead of reducing them.

Limitations: one author produced A and B, and the expert scores are a single reviewer's judgment. The automatic counts are reproducible with `score.py`.

Side by side images: `landing_side_by_side.png`, `pricing_side_by_side.png`, `mobile_side_by_side.png`.

## Independent A/B

The table above was written by one author. This pass repeats the three tasks in separate contexts, so version A never receives the skill.

Sample product: Keel, a sample invoicing tool for independent design studios. Every name, price, and figure on these pages is sample data: Starter $18 per month, Studio $42 per month, Practice $79 per month, sample studio North Room, sample outstanding $4,280, sample paid this month $9,150, and 3 sample overdue invoices.

Each task started from its own baseline. The baseline prompt was: "Build a <task> for Keel, a sample product, as a single HTML file."

- Version A was a separate context. It received that baseline and only the instruction "make it better". It was not given `SKILL.md`.
- Version B was another context. It read `SKILL.md`, received the same baseline, and was then told "make it look less AI / make it better".

Sources are in `independent/src/`. `python score.py` still scores the original `src/` pages. `python score.py independent` runs the same counter on `independent/src/` and writes `independent/scores.json` plus full-page screenshots. Viewports are unchanged: landing and pricing at 1280 px, mobile at 390 px.

### Automatic counts (independent A vs B)

| Task | Version | Blue/purple gradients | Resting shadows | Pill badges | Emoji | Glass surfaces | Distinct radii (px) | Font sizes | Spacing values | Title / body ratio | Filled buttons above fold |
|---|---|---|---|---|---|---|---|---|---|---|---|
| landing | A | 0 | 5 | 3 | 0 | 1 | 5 (8, 14, 16, 20, 24) | 16 | 24 | 3.56 | 2 |
| landing | B | 0 | 0 | 0 | 0 | 0 | 2 (6, 12) | 6 | 7 | 3.5 | 1 |
| pricing | A | 0 | 1 | 0 | 0 | 0 | 0 | 16 | 22 | 4.25 | 0 |
| pricing | B | 0 | 0 | 0 | 0 | 0 | 2 (6, 12) | 6 | 7 | 3.5 | 0 |
| mobile | A | 0 | 4 | 1 | 0 | 0 | 2 (12, 16) | 10 | 12 | 2 | 0 |
| mobile | B | 0 | 0 | 0 | 0 | 0 | 2 (6, 12) | 5 | 6 | 2 | 0 |

The equal-size icon grid count from `score.py` is 0 for A and B on all three tasks. Font weights are 2 on landing A and 3 on landing B, 5 on pricing A and 3 on pricing B, and 3 on both mobile versions.

"Make it better" increased tells on two tasks. Landing shadows went from 0 on the baseline to 5, pills from 2 to 3, and glass from 0 to 1. Mobile shadows went from 0 to 4. Pricing shadows went from 0 to 1, and font sizes went from 12 to 16.

B is lower than A on every tell that is non-zero for A. Type and spacing scales are tighter on B for every task (landing 16 sizes and 24 spaces vs 6 and 7, pricing 16 and 22 vs 6 and 7, mobile 10 and 12 vs 5 and 6). Two counts are lower on A and still inside the checklist targets: pricing radii are 0 on A and 2 on B, and landing font weights are 2 on A and 3 on B.

The filled-button counter only matches an element whose class contains `btn`. Landing uses that class, so the counts above are the on-screen buttons. Pricing B uses the class `button` and mobile B uses `action`, so the automatic count is 0 even though each screenshot shows one filled action: "See sample plans" on pricing B, and "Review 3 overdue" on mobile B. Pricing A has three text links that all say "Compare sample plans" and no single filled action. Mobile A has no button.

Labeled pairs, A on the left and B on the right: `independent/landing_side_by_side.png`, `independent/pricing_side_by_side.png`, `independent/mobile_side_by_side.png`.

## Install test

A fresh directory got a copy of this folder at `.agents/skills/ai-ui-tells/`. The agent was asked only to build a landing page and make it look less AI, and to list the files it read.

It read `SKILL.md` first. It then read `eval/README.md`, `eval/score.py`, `eval/src/landing_B.html`, and `eval/src/landing_baseline.html`. The page it wrote shares no non-empty lines with `landing_B.html`. It did reuse the sample product name Tally from this eval writeup.

`score.py` on that page at 1280 px: blue/purple gradients 0, resting shadows 0, pill badges 0, emoji 0, glass surfaces 0, equal icon grids 0, distinct radii 2 (6, 12), font sizes 6, font weights 3, spacing values 8, title/body ratio 3.5, filled buttons above the fold 1. Those match the checklist targets. The document title contains one em dash, so the page was left out of the repo.
