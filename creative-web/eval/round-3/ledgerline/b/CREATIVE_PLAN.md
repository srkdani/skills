# Ledgerline sample

Task-focused payout API. The signature teaches matching in one glance: slips that do not share a height do not balance. Headline and the action sit in the first viewport, immediate, with no intro and no pin. Small and medium ideas stay off that action.

## Harvest

Facts only this desk has. At least six are physical or sensory.

1. The working surface is a green desk blotter, cool under the hand, darker at the edges than in the lamp pool. (temperature, touch)
2. Marketplace orders are manila slips. Bank payouts are blue carbon copies, tacky, with a faint sweet smell when a night batch is pulled. (material, smell, touch)
3. A red china-marker, waxy, flags only the slip that does not share the sum. (tool, smell)
4. The lamp is brass with a green glass shade. The shade is warm. It goes on after the marketplace cutoff and is the only light on the desk. (light, temperature)
5. The adding machine dings once when a column sits even, then the paper tape takes a double underline. (sound)
6. A rubber thumb picks one slip so the carbon does not smear. (tool)
7. Matched pairs go on a brass spindle. An open item stays flat on the blotter and is never spiked. (ritual, object)
8. A small cold brass anvil holds the open column so the fan cannot lift it. (temperature, tool)
9. The fee is written in a thinner hand in the right margin, never inside the amount column. The enemy is a fee that hid in the shipping line, a cent off, so the carbon will not kiss. (process)
10. Clerks say "kiss" when two amounts meet and "open item" when a slip has no pair. (vocabulary)
11. Seller names are rubber-stamped in a condensed face because the name is long and the slip is narrow. One stamp is light, one is smudged. (material)
12. The night batch starts at the 6 pm cutoff. The spindle is full by morning. Before cutoff the open column is still waiting. (time)
13. Operators say the deposit will not match the order slip, and that a seller is short. (customers' words)
14. The short slip sits proud of the stack because a clerk will not file a pair that does not share a sum. (ritual)

## Truths

1. A carbon payout and a manila ticket kiss only when they share one sum. The pair is seated, edge to edge, on the blotter. Rival: Adyen's settlement report, which puts a variance in a row and does not seat two slips until they kiss.
2. Only a kissed pair is spiked. An open item stays flat on the blotter through the night batch. Rival: Shopify's payout CSV, which files every row into one export and has no spindle that refuses an open item.
3. The short slip takes a china-marker, and the fee that made it short sits in the right margin in a thinner hand. Rival: BlackLine's exception grid, which paints a cell and does not keep a grease-pencil flag or a margin hand.

## Emotion

Certainty.

"I lined the carbon slip on the ticket and the short one stood up under a red mark."

## Concepts

1. The site is a green blotter where marketplace tickets and carbon payouts are unlike slips, and lining one onto its pair shows a kiss or a china-marker flag. Rival: Modern Treasury. Their ledger is a software register, not unlike paper slips on a blotter. The blotter line does not fit them. Keep.
2. The site is a brass spindle where a pair can be filed only after it kisses, and an open item never leaves the desk. Rival: Tipalti. They pay suppliers from a dashboard and do not spike paper pairs. Keep.
3. The site is an adding-machine tape where the carriage dings only when the column sits even. Rival: QuickBooks. A register that totals, and a ding when it totals, still fits them. FAIL. Replaced: The site is a china-marker resting on the short slip, and the rest of the desk is what that mark refuses to file. Rival: Stripe payouts. They do not leave a grease pencil on a paper slip. Keep.

## Pick

The green blotter. The visitor sentence is the act of lining the carbon onto the ticket and seeing the short slip stand up under a red mark. That happens on the blotter, not on a spindle and not on a marker alone.

World, one only: Unlike objects on a surface. The blotter is the surface. Slips, tape, anvil, and spindle are the objects. They do not share a size.

Rejected, Worker in the room: a clerk built from circles would sit as a mascot beside the slips. The fit is a playful or studio brand. Ledgerline's job is the match, and the slips already do that job.

Rejected, Clock in the room: the 6 pm cutoff is real, but a timepiece at 40% of the viewport would teach the hour. The signature has to teach matching. The hour stays a small plate.

No merge. The spindle and the marker are objects on the blotter, not a second site metaphor.

## Visual system

- Material: green desk blotter and manila slips, because the working surface is the blotter and the orders are manila. Not a dark console.
- Light: the brass banker's lamp with a green glass shade, on after the 6 pm cutoff, because that shade is the only light on the desk. The lamp picks the brightness. The pool is bright enough to read a sum. The edges of the pad fall darker. This is not a chosen dark mode.
- Palette, five hex values from those materials:
  - `#163C2C` blotter edge, because the pad is dark green where the shade does not reach.
  - `#2C7A50` lamp pool, because the green glass throws this brighter green on the working desk.
  - `#E8C16A` manila, because the marketplace ticket is manila card.
  - `#D2E1EA` carbon, because the payout copy is blue carbon.
  - `#C4382C` china-marker, because the flag is a red grease pencil. The same red is the action, so the verb and the flag are one ink.
- Type: display "Big Shoulders Display" (700 and 800), file from `https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=Newsreader:opsz,wght@6..72,500;6..72,600&family=Courier+Prime:wght@400;700&display=swap`, because seller names are rubber-stamped in a condensed face so a long name fits a narrow slip. Body "Newsreader" at 18px, because the fee is a thinner written hand in the margin. Display size is 5.2rem (93.6px), more than four times the 18px body. On a 390 width the body is 16px and the display is 4.5rem (72px), still more than four times. No italic word inside the headline. Tape figures use "Courier Prime" at 12 to 16px only, because the adding machine prints mono figures. Courier Prime is not the display.
- Picture rule: kept, screenprint. Two or three flat inks, a second pass 2px off the first, large shapes, no photographic texture, because the slips are printed forms and a carbon copy is a second pass. This is the grade, not a print-shop concept.
- Motion: kept, calm drift. `sine.inOut`, 0.8 to 1.6s, a move under 12px or an opacity change, because lining a slip is a small settle on a desk. The unmatched state is already visible as height, rotation, and overlap, so the kiss does not need a long slide. Menus and the fee toggle are instant, under 150ms. One fidget, the anvil, is under 100ms.
- Sound: none.
- Grade: one treatment. `GRADE:` screenprint, the carbon pass 2px off the manila pass, under the one green lamp. No second grade.

## Objects

The surface is `#scene`, the blotter. Positions are chosen. Names are stamped on the objects. No equal cards, no equal radii, no equal shadows.

| Content | Object | id | data-object | How it differs |
| The marketplace order | manila ticket | `#manila-ticket` | `manila-ticket` | widest slip, radius 2px, dark stamp, holds the headline |
| The bank payout | carbon copy | `#carbon-payout` | `carbon-payout` | rotated 11 degrees, overlaps the ticket, shorter, radius 2px |
| The exception | short slip | `#short-slip` | `short-slip` | taller than the ticket so the pair cannot share a height, smudged stamp, china-marker |
| The column | adding tape | `#adding-tape` | `adding-tape` | narrow curl, radius 0, cropped by the right edge of the viewport |
| The fee lesson | margin sheet | `#fee-margin` | `fee-margin` | one wide sheet, thin right column, no rotation, radius 0 |
| A filed pair | spindle slip A | `#spindle-a` | `spindle-a` | short, rotate 8 degrees, light stamp |
| A filed pair | spindle slip B | `#spindle-b` | `spindle-b` | longer, rotate -12 degrees, worn corner |
| A filed pair | spindle slip C | `#spindle-c` | `spindle-c` | taller, rotate 3 degrees, smudged stamp |
| The weight | brass anvil | `#anvil` | `anvil` | small, not a slip, radius 0, sits low left |
| The hour | lamp plate | `#live-plate` | `lamp-plate` | small brass rectangle, copy changes with the local hour |

A click or a scroll beat expands the carbon once it kisses (about 8px of growth, the scroll beat). A tap brings one slip forward. Hover is extra and only on a fine pointer.

## Budget

Every idea names a truth. Counts: small 6, medium 2, big 1.

Big, truth 1, technique 20 (scroll or drag scrub of the lining). Element `#signature` with `data-tier="big"` and `data-truth="1"`. Visible in the first viewport. Teaches the job at rest: the carbon and the ticket do not share a baseline, the short slip does not share a height. No pin. No intro.

Storyboard, same beats for touch:

- 0%: carbon sits 10px above the manila amount rule, rotated 11 degrees, overlapping the ticket. The short slip is taller and unmarked. Headline "Flag what will not kiss." and the button "Line the slips" are already visible, because truth 1. The practical fact (night cutoff 6 pm, sample batch) is on `#live-plate`.
- 0 to 30% of the scroll, the first 270px, no pin: the carbon drifts 10px down, `sine.inOut` 1.1s, until the baselines kiss. The short slip does not travel. The china-marker on it becomes visible because that pair still does not share the sum (truth 3 shows inside the picture; the signature's truth is 1). The tape takes its double underline when the kiss completes.
- Touch, designed first: the range `#line-range` and the button `#line-slips` drive the same 0 to 1 progress. A tap on a slip brings that slip forward. Hover does nothing required.
- After 30%: the kissed state holds. The fee sheet and the spike scroll natively. Body text does not move.
- Reduced motion, batch 5: the range snaps between open and kissed. No travel, no pin. Layout and picture stay. The action still lines the pair.

Medium, two, built one at a time. Both sit below the scene so they cannot cover the action.

- Medium 1, truth 3, technique 18 (instrument readout on the adding figures). `#fee-margin`, `data-tier="medium"` `data-truth="3"`. Two taps, "In the margin" and "In the shipping line", instant under 150ms. In the margin, the 0.30 fee is visible in the thin hand and the sums can kiss. In the shipping line, the fee leaves the margin, the carbon reads short, and the china-marker shows. Touch: the same two taps. Sample figures, marked sample.
- Medium 2, truth 2, technique 4 (content as objects that do not match). `#spike`, `data-tier="medium"` `data-truth="2"`. Three slips, different size, angle, and wear. Tap one to spike it: it shifts 8px toward the nail, takes a hole, and stamps SPIKED. An open item stays flat. When all three are spiked, the empty line shows. Touch: tap. Hover, fine pointer only: the stamp darkens.

Small, six. Each under 300ms, each off the headline and the button.

- Small, truth 2, `#live-plate`, `data-tier="small"` `data-truth="2"` `data-live="time"`. On load, read the local hour once. From 6 pm to 6 am the plate says "Night batch. Open items stay flat." and the lamp pool is the working green. Otherwise it says "Waiting on the 6 pm cutoff." and the pool dims. The loading line "Warming the green shade." is the plate's first text.
- Small, truth 1, `#state-stamp`. A visible stamp on the ticket reads OPEN ITEM or KISSED, and `document.title` follows it. Updates with the signature. Under 150ms.
- Small, truth 2, `#anvil`. One fidget. A tap settles the anvil 6px and back in 90ms, the weight that keeps open items flat.
- Small, truth 3, `#china-flag`. The red grease-pencil slash on the short slip only. Opacity follows the lining. It does not sit on the button.
- Small, truth 1, `#tape-rule`. The double underline on the adding tape, visible when the column kisses.
- Small, truth 2, `#footer-line`. The footer is the spindle's last line, not a link row: "Ledgerline sample. Open items stay flat. Only a kiss takes the spike."
- Small, truth 2, `#empty-state`. "No open item. The spike took the night." Shown when the three spike slips are filed. Triggerable, and the sentence is printed on the spindle base.

`#empty-state` is a seventh small if both it and the footer are marked. Mark six or seven, never fewer than five. The empty state and the footer are both truth 2 and both visible or triggerable.

## Rhythm

1. Blotter: scattered unlike slips at chosen positions, words stamped on the paper, the action in the lamp pool.
2. Margin: one wide sheet, the lesson written in a thin right hand, figures on the left. Not a heading over a grid.
3. Spike: a nail with three slips at clashing angles, no shared baseline. A pile, not a row.
4. Tape: one narrow curl, one sentence on the paper, cropped at the edge. The footer lives on this strip.

No section is a heading, then text, then cards. No section can swap with the one above it unchanged.

## Removal

Build a lamp flicker: the pool ellipse opacity loops, a slow pulse. Delete it in batch 5. A flicker is mood. It does not teach the kiss or the flag, and the shade has to stay a steady pool so a sum can be read. Leave the `REMOVED:` comment. A console log does not count.

## Voice

Headline, five words: "Flag what will not kiss."

Subhead: "The payout API that seats a marketplace ticket on its carbon copy and flags the slip that does not share the sum."

- Button: "Line the slips"
- Empty state: "No open item. The spike took the night."
- Footer: "Ledgerline sample. Open items stay flat. Only a kiss takes the spike."
- Missing page: "This page is off the blotter. The slips are still on the desk."
- Loading: "Warming the green shade."

The empty line is the oddly specific one. A stranger can tell the brand from the footer: open items, a kiss, a spike. The brand is marked sample beside the name and in the footer. No fake logos, no fake quotes, no invented company metrics. The fee figures are a sample worked pair, labeled sample.

## Genericness

Similar brief: a payout reconciliation API in the same industry, the kind of Stripe Connect add-on or close-the-books page that would ship as a dark console.

The part I would have written for them: a variance table and three equal cards named Match, Flag, and Export, with a headline about real-time reconciliation.

Changed: the page is a green blotter of unlike paper slips. Match is a kiss of two heights, the flag is a china-marker, and the file is a spindle that refuses an open item. The dealt world stays. Unlike objects on a surface. This does not escape into cream and an italic serif, black and an acid accent, glass, or a particle network.

Batch 1 gate: Grey slips on the blotter still teach the kiss, the carbon rotated over the ticket and the taller short slip beside it, after the objects were pinned to the surface and the anvil was moved off the slider.

Batch 2 gate: The blotter now prints the unlike slips in two inks, the carbon still settles onto the ticket while the taller short slip stays proud, and the open-to-kiss scrub is the touch path after the slider was drawn so it can be seen.

Batch 3 gate: The margin sheet still keeps the fee in a thinner hand, and the spindle still files only a tapped pair, after those two interactions were built one at a time below the lining action.

Batch 4 gate: The cutoff plate, the open-item stamp, the anvil tap, the china-marker, the tape underline, and the footer all stay off the lining button, after the marker was moved below the headline on a narrow screen.

Batch 5 gate: The lining action stays immediate on the blotter and the cutoff plate still tells the hour, after reduced motion snaps the kiss, the narrow screen keeps the headline clear, and the lamp flicker was deleted.

## Score

Thumbnail at a small size: unlike slips, one tilted carbon, one taller slip with a red slash. T1 2, T2 2, T3 2, T4 2 (the tilted carbon and the red slash). Scroll: R1 2, R2 2 (the short slip stays proud), R3 2, R4 2, R5 2. Creative score 14. Floor 4. The idea of the site: a green blotter where a carbon payout either kisses its ticket or the taller slip takes the china-marker.
