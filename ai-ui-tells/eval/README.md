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
