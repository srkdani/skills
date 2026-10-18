# Ledgerline plan

## Harvest

Facts only this product has. Ledgerline is the match between a marketplace payout file and the bank settlement that is supposed to equal it.

1. Two paper tapes: the marketplace payout impression and the bank settlement impression.
2. Carbon blue on the second impression. The blue stains a cuff if you hold the tape.
3. Green-bar ledger stock, wide pale bars, the sheet accountants rule on.
4. A red pencil flag on the one line that is short.
5. Sprocket holes along a desktop payout tape, punched so the carriage can pull it.
6. The carriage steps in hard detents. Each notch is one line trying to sit.
7. A fluorescent tube over the desk at batch close. Cool, even, slightly green. The sheet is bright because the lamp is on.
8. Thermal warmth on a long tape that just came off the printer.
9. The penny that will not die: marketplace 18.41 against bank 18.40.
10. Operators say "it does not balance" and "that line will not sit". They do not say anomaly.
11. The batch is judged when the selling day ends and the payout file has actually landed. Before that, the second tape is still feeding.
12. Registration ticks in the margin, used to see if the second pass is a hair off.
13. An orphan line: a payout with no bank twin.
14. Flagged lines go on a wire spike. The ones that sit do not stay on the spike.
15. The enemy is the line that still sticks out after every other line has seated.

Sensory, at least six: carbon blue stain, fluorescent green cast, thermal warmth, carriage click, carbon on the cuff, the visible gap of a penny.

## Truths

1. A marketplace payout and a bank settlement are two carbon impressions of the same money, and they count as reconciled only when the second pass sits on the first. Rival: a payments dashboard that shows one balance number. It does not seat two impressions.
2. The line that will not balance stays flagged in red after the others have seated. The job is the exception, not a happy total. Rival: a reconciliation spreadsheet that clears the row and hides it. It does not keep one red flag standing.
3. The batch is judged at a cutoff, under the desk lamp, once the day's payout file has landed. Before that cutoff the second tape is still feeding. Rival: a timeless "real-time" status badge. It has no batch lamp and no tape that is still feeding.

## Emotion

Relief.

"I seated the two tapes and the only line left red was the penny that would not balance."

## Concepts

The site is a carbon-copy desk where the marketplace tape and the bank tape are two ink passes, and seating the clip makes them one line while the penny stays red. Rival: a payments dashboard. Their page is one balance and a chart. The two misregistered tapes do not fit. Keep.

The site is a night-shift spike where every product feature is a paper flag. Rival: an accounting firm's exception tray. They already spike paper. FAIL. Replaced by the concept below.

The site is a penny scale where each payout is a weight and the visitor adds a one-cent washer until the beam levels. Rival: a bookkeeping app. A washer on a beam does not fit their ledger grid. Keep as an unused alternate.

## Pick

The carbon-copy desk. Two states, one clip. The visitor seats the tapes and sees the penny stay red, which is the sentence they would tell a friend.

Rejected world: Bench in stages. Ledgerline does not build a payout by hand across craft stages. A pinned bench would turn one match into a timeline, and this task page cannot hold a long pin. The quiet failure of that world is a dotted row of steps.

Rejected world: Operable document. A sheet you fill in becomes a fake form under a headline, which is that world's fail. The product is the change from an open gap to a seated line, not a document to complete.

No merge. The carriage detent is the dealt motion, because a tape register seats one notch at a time, not a second world.

## Visual system

Material: carbon paper on green-bar ledger stock, because payouts are two impressions that must register, and exceptions are marked on ruled paper.

Light: the fluorescent tube over the batch desk, because the file is judged when it lands, under that lamp. The lamp is bright and cool, so the page is a lit sheet. Not a dark console.

Palette, from that material:
- Sheet `#E4EED6`, because that is the paper between the green bars under the tube.
- Bar `#A9C49A`, because that is the printed green bar.
- Carbon black `#1A1914`, because that is the bank impression.
- Carbon blue `#1F4E79`, because that is the marketplace carbon, the second pass.
- Flag `#B42318`, because that is the red pencil on the line that will not sit.

Type: display "Big Shoulders Display" (Google font, weight 800), because a payout total is condensed machine type, the kind a tape printer uses for a total line. Body "Public Sans" at 18px, because a note on the sheet has to stay readable under the lamp. Display size `clamp(72px, 8vw, 112px)`. 112 / 18 is more than 4. Figures in "Fragment Mono" at 13 to 32px, because the tape's numbers are a machine readout, not the display face.

Picture rule: accept screenprint. Two flat inks, carbon black and carbon blue. The second pass rests 2px off the black when seated. The open state is many units of that same miss, so the gap is obvious. No photographic texture. Large tape shapes, sprocket holes, three rules, one red flag. The picture depicts the two payout tapes, not people.

Motion: accept mechanical. Detents, 120ms linear between notches, no overshoot, because the carriage clicks. Scroll and the carriage control snap across 6 steps. Hour stamps are instant. No intro, because the page is task-focused.

Sound: none.

Grade: one treatment. Fluorescent on green-bar paper, carbon blue as the second screenprint pass. The seated pass shows a 2px blue rim. The same hard 2px second impression is the only shadow language on the page.

## Objects

- `#bank-tape` data-object `bank-tape`: the black settlement sheet. Wider rim when the blue pass is unseated. Sprocket holes punched out to the sheet color.
- `#market-tape` data-object `market-tape`: the carbon blue payout sheet. Open state shifted by a full notch. Seated state shifted 2px. Shorter visual overlap than the bank sheet until the last detent.
- `#penny-tick` data-object `penny-flag`: the only red flag. Larger than the other marks. A pencil tick appears on tap. The other lines do not get this flag once seated.
- `#batch-slip` data-object `batch-slip`: the desk-clock line. Wording changes with the local hour. Feeding, on the desk, or judging.
- `#reg-ticks` data-object `reg-mark`: crop marks in the margin labeled +2px. Smaller than the tapes. They do not move.
- `#spike` data-object `exception-spike`: three sample slips on a wire. Different width, notch, and tilt. One starts flagged.

Sample lines, marked sample: North stall 1840.20 and 1840.20, Ferry goods 220.00 and 220.00, Night cart 18.41 and 18.40.

## Budget

Big, truth 1, `#registration`: the signature. Two built scenes, one clip-path, inset from opposite edges, driven by one progress value in 6 detents. Open scene: blue tape a full notch off the black, red marks on the unseated rules. Seated scene: blue rests 2px off, only the penny flag remains. No opacity crossfade. Teaches the job at rest: you see the miss before you touch anything. Headline and the Seat the tapes key are on the sheet, outside the clip, visible on load.

Storyboard: 0 to 30% of the scroll, the seam crosses the first rules and those passes start to sit, because truth 1. 30 to 70%, the seam keeps stepping and the uncrossed side still shows the gap. 70 to 100%, the sheet shows the seated pass and the penny stays red, because truth 2. Touch: the range carriage and the Seat the tapes key jump the same detents. Reduced motion: no scroll travel, the range still snaps the clip, layout stays.

Medium, truth 2, `#spike`: tap a sample slip to flag it. Tap the flagged slip again and the spike shows the empty state. Touch path: tap, 44px targets.

Medium, truth 3, `#hour-guide`: three desk-lamp stamps. Tap one to read that part of the batch. The stamp that matches the local hour is marked now. Touch path: tap. Instant, under 150ms.

Small, truth 3, `#batch-slip`: desk clock sets feeding, on the desk, or judging. `data-live="time"`. Changes the lamp strip, not only a digit.
Small, truth 1, `#reg-ticks`: the +2px registration mark in the margin.
Small, truth 2, `#penny-tick`: tap the penny flag and a pencil tick draws in 80ms. The fidget. Does not cover the Seat the tapes key.
Small, truth 2, `#sheet-stamp`: SAMPLE stamp and the plate that reads "Penny still open" or "Tapes seated, penny red".
Small, truth 3, `#cuff-note`: the footer is the carbon on the cuff, not a link row.

Small and medium controls sit in the margin, on the spike, or on the record. They do not cover the headline or the Seat the tapes key.

## Rhythm

1. Split sheet: a full-viewport picture, the headline printed on the sheet, the seam moving through two tapes.
2. Batch record: one ruled form, label and value on horizontal rules, lamp stamps along the bottom edge.
3. Spike: a vertical wire and three hanging slips of different notches.
4. Cuff: one large sentence, then two short lines. No rules, no wire, no seam.

No section is heading, then text, then cards.

## Removal

Carbon-dust grain overlay. Built as a full-sheet turbulence multiply, then deleted. The picture rule forbids photographic texture, and the 2px misregistration already shows the carbon. A grain pass does not teach the match.

## Voice

Headline: Seat the two tapes.
Subhead, open: The marketplace carbon and the bank line do not share a rule.
Subhead, seated: They sit. The penny stays red.

Button: Seat the tapes.
Empty state: No gap tonight. The tapes sat.
Footer: Carbon on the cuff. The penny is still open.
Missing page: This sheet is a sample. The batch you want is not on this spike.
Loading: Feeding the second tape.

The footer names the cuff and the penny. A stranger can tell the brand without the headline.

## Genericness

Similar brief: a marketplace payout API page in the usual payments costume (one balance, three feature cards, a green check). That plan would have used a dashboard and the phrase "match rate". Changed: the page is two carbon tapes under a desk lamp, the match is a registration, and the only number that matters is the sample penny that will not sit. The dealt world stays: two states, one clip.

## Batch 1 gate

Signature placed. `#registration` is the only big tier. The open gap is visible in the first viewport. Headline "Seat the two tapes." and the Seat the tapes key are on the sheet before any scroll.

## Batch 2 gate

GRADE comment names one screenprint grade. GSAP and ScrollTrigger are loaded. The scene draws the tapes with more than 8 SVG shapes. Both states are built.

## Batch 3 gate

Two medium interactions: the spike flags, and the desk-lamp stamps. Each has a tap path. Neither covers the main key.

## Batch 4 gate

Five small details are visible: desk clock, registration ticks, penny tick, sample plate, cuff footer. The desk clock uses `data-live="time"`. Every tier element carries `data-truth`.

## Batch 5 gate

`prefers-reduced-motion` drops scroll travel and keeps the carriage usable. Narrow screens use a stacked sheet, not a hover-only control. No intro. Practical facts (desk clock, POST /v1/match, match@ledgerline.sample) are on the first sheet.
