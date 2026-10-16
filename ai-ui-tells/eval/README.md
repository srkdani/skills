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

The table above was written by one author. This pass uses a fresh sample product, Harbor Kit, a sample gear checklist for small film crews. Every price, name, quote, logo, and figure on these pages is labeled sample.

Each task started from a one-shot in a separate context that did not have the skill. The prompt was short: "build a landing page for Harbor Kit, a sample product", and the same shape for a pricing page and a mobile app dashboard. Version A is that file after one further instruction, "make it better", still with no skill. Version B is a different context that read `SKILL.md`, drew a direction, and was told "make it look less AI / make it better". B was run twice per task with different draw salts so the skill could not collapse onto one look.

What the one-shot actually did: system-ui or Segoe UI, a teal or blue gradient, uppercase tracked labels, equal cards, soft shadows, and (on landing and pricing) an emoji. "Make it better" increased the noise. Landing shadows went from 0 to 9 and eyebrows from 6 to 12. Pricing shadows went from 4 to 17 and eyebrows from 17 to 24. Mobile glass went from 0 to 2. It did not always use a purple glow. That is the recorded before, not a hand-built one.

`python score.py` still scores the original `src/` pages. `python score.py independent 1280` scores this set at 1280 px wide and writes `independent/scores.json`. The counter now also reports eyebrows, the real H1 over body size, H1 letter-spacing (em), H1 line-height, contrast pairs under WCAG AA, and banned words.

### Automatic counts (independent A vs B)

B is the first draw. B2 is the second draw.

| Task | Version | Direction | Gradients | Shadows | Pills | Emoji | Eyebrows | Radii | Font sizes | Spacing | H1/body | H1 tracking | H1 line-height | Contrast fails | Filled buttons | Display face |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| landing | A | none | 0 | 9 | 2 | 2 | 12 | 2 (8, 12) | 18 | 21 | 2.82 | -0.02 | 1.15 | 8 | 2 | system-ui |
| landing | B | Pool clipboard | 0 | 0 | 0 | 0 | 0 | 2 (4, 6) | 4 | 8 | 4.25 | -0.02 | 1.05 | 0 | 1 | Syne |
| landing | B2 | Split-flap board | 0 | 0 | 0 | 0 | 0 | 1 (2) | 6 | 6 | 5 | 0.02 | 1 | 0 | 1 | Anton |
| pricing | A | none | 0 | 17 | 7 | 1 | 24 | 3 (4, 8, 14) | 23 | 27 | 3 | -0.035 | 1.12 | 7 | 2 | system-ui |
| pricing | B | Locker enamel | 0 | 0 | 0 | 0 | 0 | 2 (2, 6) | 5 | 8 | 4 | -0.02 | 1.05 | 0 | 1 | Syne, number in Anton |
| pricing | B2 | Night call sheet | 0 | 0 | 0 | 0 | 0 | 2 (2, 6) | 4 | 6 | 4.5 | -0.02 | 1.05 | 0 | 1 | Newsreader |
| mobile | A | none | 0 | 4 | 1 | 0 | 15 | 10 | 14 | 22 | 1.31 | -0.017 | 1.2 | 7 | 4 | system-ui |
| mobile | B | Darkroom safelight | 0 | 0 | 0 | 0 | 0 | 1 (2) | 4 | 4 | 4 | -0.02 | 1.05 | 0 | 1 | Fraunces |
| mobile | B2 | Ticket window | 0 | 0 | 0 | 0 | 0 | 1 (8) | 4 | 6 | 1.75 | -0.02 | 1.05 | 0 | 1 | Fraunces |

Mobile baseline (the one-shot, before "make it better") had 1 blue gradient. Glass on mobile A is 2. Equal icon grids: landing A 1, mobile A 1, and 0 on every B. Banned words: 0 on A and B. Anton on the split-flap uses the stencil tracking exception (0.02em) and line-height 1.0.

The six B pages use six directions. Shrunk to about 300 px wide, A is a teal or white template and B is a colored band with one huge element (a clipboard, a flap, the number 108, a red circle, a safelight, a ticket). B and B2 on the same task do not match each other.

First viewport, A on the left and B on the right: `independent/landing_side_by_side.png`, `independent/pricing_side_by_side.png`, `independent/mobile_side_by_side.png`.

The two skill runs: `independent/landing_two_runs.png`, `independent/pricing_two_runs.png`, `independent/mobile_two_runs.png`.

## Install test

A fresh directory received this folder at `.agents/skills/ai-ui-tells/`. The agent was asked only to build a landing page and make it look less AI, and to list the files it read.

The first file it read was `SKILL.md`, then `directions.md` and `draw.py`. It did not read the eval HTML. It drew Locker enamel and tied it to a sample morning fish auction (North Wharf), with the bold place a stamped door number, 214. The page is not in this repo.

`score.py` at 1280 px on that page: blue-violet gradients 0, resting shadows 0, pills 0, emoji 0, eyebrows 0, contrast failures 0, distinct radii 2 (2, 6), font sizes 5, spacing values 5, H1/body 4, H1 letter-spacing -0.02em, H1 line-height 1.05, filled buttons above the fold 1, banned words 0. Display stack: Syne, with Anton on the number. No em dash in the file.
