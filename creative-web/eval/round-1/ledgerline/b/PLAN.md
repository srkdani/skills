# Harvest

1. Continuous-feed green-bar paper, a pale sheet with green bars, the stock a night payout batch prints on. Physical.
2. Sprocket holes down the margin, the tractor feed that keeps a column straight. A torn hole means the line slipped. Physical.
3. Carbon ribbon ink in one brown-black. Every figure comes off the same ribbon. Physical.
4. The dry smell of warm toner when a sheet tears off the feed. Sensory.
5. A desk lamp after the marketplace closes. It hits the front sheet only. Sheets lower in the pile stay cool. Sensory: light, temperature, time of day.
6. The printer sound is a detent: one line, a stop, six steps, then a pause. Sensory.
7. A binder clip on the batch that still has an open exception. Physical tool.
8. Desk vocabulary: tie-out, short line, gross, fee, refund, net, hold, match key, batch tab.
9. The enemy is a line that almost ties: a fee taken twice, a refund on the wrong order, a cent lost in conversion.
10. Marketplace finance says "this payout will not tie" and "the net is short by the label." Customers' words.
11. Ritual: nobody leaves the lamp until each pulled sheet is tied or tagged with a reason.
12. Seller holds stay clipped until delivery or the doors close, so some sheets are many days thick and some are one thin night. Physical process.
13. The match key is the marketplace order id plus the seller payout id.
14. The batch freezes after midnight, when the day's orders stop.

# Emotion

Scrutiny.

"I pulled the sheet that stuck out and saw the printed net miss the fees."

# Concepts

1. The site is a stack of green-bar settlement sheets where each marketplace batch is a different thickness and pulling the sheet that will not sit flush shows the line whose fees do not equal the net. Rival: a checkout gateway. A gateway takes a payment. It does not stack night-batch sheets or pull a short payout. Keep.

2. The site is a carbon adding machine where each key is a fee and the total bar stamps the variance. Rival: a bookkeeping suite. The machine and the total bar fit them. FAIL. Replaced: The site is the torn sprocket margin of a payout feed, where each hole is a matched order and a ripped hole is the seller whose refund landed on the wrong order. Rival: a label printer. They own sprockets. A ripped hole that means a mis-posted marketplace refund does not fit them. Keep.

3. The site is one ruled ledger line that money must sit on, and a figure floating off the rule is the exception. Rival: a spreadsheet product. The ruled line fits them. FAIL. Replaced: The site is a midnight binder of seller holds, and unclipping one hold shows the shipping label that shorted the net. Rival: a document scanning bureau. Unclipping a seller hold to find a short shipping label does not fit them. Keep.

# Pick

The stack of green-bar settlement sheets. The visitor sees a slip already out of the column and can pull it, which is the sentence they would tell a friend. The sprocket story and the binder story stay out. Using them as well would merge worlds.

Worlds rejected:

- Material weather. A payout that will not tie is not heat, fog, dust, steam, or safelight. The facts are sheets, holes, a clip, and a lamp on paper.
- Bench in stages. Ledgerline does not make a payout by hand on a bench. A stage pin would also hold a task page past the first glance the job needs.

Dealt motion kept: mechanical detents, because the line printer advances one line and stops. Dealt picture kept: cut paper, because the settlement is flat stock.

# Visual system

- Material: continuous-feed green-bar ledger paper, because night-batch payouts are ruled lines of gross, fee, refund, and net on that stock.
- Light: a desk lamp after the marketplace closes, because the tie-out starts when the day's batch freezes. The lamp hits the front sheet, so the page is bright paper, not a dark room.
- Palette: sheet `#F3F6EE`, because that is the lit face of the green-bar stock under the lamp.
- Palette: bar `#B7CFA6`, because those are the printed bars a figure has to sit on.
- Palette: ink `#1C2416`, because the carbon ribbon is one color for every figure, tab, and stamp. The shadow is this same bar paper offset 6px, not a fourth paint.
- Type: display Staatliches, file `https://fonts.googleapis.com/css2?family=Staatliches&family=Public+Sans:wght@400;600;700&display=swap`, because the lid and the batch tabs are stamped in condensed caps so a thin sheet still reads from the side.
- Type: body Public Sans at 18px from that same file. Display is `clamp(72px, 7.2vw, 108px)`, because the margin notes are a plain form grotesque and the lid must be at least four times the body (72 / 18 = 4, 108 / 18 = 6).
- Picture: cut paper, kept from the deal. It depicts the stack, the sprocket holes, one torn hole, and the pulled net slip. Hard edges, no blur, overlaps only. Shadows are a second piece of bar paper offset 6px, because the stock is flat and the deal forbids a blur shadow.
- Motion: mechanical `steps(6)`, 120ms a step, so a six-step pull lasts 0.72s, because the printer is a detent and does not overshoot. Spine jumps and other repeated controls are instant.
- Sound: none, because this is a task page and the printer is shown with steps, not played.

# Objects

- `#slip` `data-object="short-sheet"`: the pulled net slip. Dog-ear, its own bars shifted off the parent bars, resting translate to the right. Sample batch prints 1700.00 against a column that adds to 1731.60. This is the signature.
- `#goods` `data-object="goods-batch"`: thickest sheet, three plies of different heights, square corners, every figure in the column. The empty state is printed on this sheet.
- `#tickets` `data-object="ticket-batch"`: thinnest sheet, about half the goods height, top-right corner clipped, a HOLD stamp, one night only.
- `#rentals` `data-object="rental-batch"`: medium sheet, one sprocket torn into a slot, the refund row shifted, copy about the wrong stay.
- `#rate` `data-object="rate-slip"`: a narrow sample slip, rotated, no sprockets, overlapping the file strips, a different width from every batch sheet.
- `#clip` `data-delight="clip"`: the binder clip on the short slip. A tap snaps it and stamps HELD.
- `#foot` `data-small="tractor"`: the tear-off tractor strip.

Spine controls `#spine-short`, `#spine-goods`, `#spine-tickets`, `#spine-rentals` are the stack edges. Thicknesses differ (short pulled, goods widest, tickets narrowest, rentals notched). They are not equal cards.

# Storyboard

Budget: one hero signature (the pulled net slip in the first viewport), one supporting journey (scroll moves through the pile, and the slip detents toward the column as the short sheet leaves), one hidden delight (the clip), one small surface (the tractor footer). No intro. No pin. The headline and the pull button are on the front sheet when the page loads. The signature teaches the job at rest: the printed net is off the bars, so the payout does not balance.

0 to 30% of the scroll: the short slip steps from its pulled rest toward the column in six detents, because the next sheet is a batch that ties and you are leaving the exception. Touch: the same scroll. A tap on the slip or the button "Pull the short sheet" runs it back out in six detents. Reduced motion: the slip stays pulled, and the button jumps it with no travel.

30 to 55% of the scroll: the goods sheet arrives, three plies thick, every figure in the column, with "This batch sat flush. Nothing to pull." because a tied batch has no exception. Touch: scroll, or a tap on the goods spine, which jumps there with no tween.

55 to 75% of the scroll: the ticket sheet, thin, corner clipped, HOLD stamped, because the doors have not closed and the payout is still a hold. Touch: scroll or tap the ticket spine.

75 to 100% of the scroll: the rental sheet with the torn sprocket, then the file strips the stack will take, the sample rate slip, and the tractor footer. Touch: scroll, a spine tap, or the file word on the lid, which jumps straight to the strips and is instant.

Delight: tap the binder clip. It rotates in six detents and the stamp HELD appears at once. Reduced motion: the stamp appears and the clip jumps, no rotate tween.

# Removal

A full-scene paper-grain turbulence overlay. It was built, then deleted, because cut paper is flat and the 6px offset sheet already supplies the shadow. Grain does not teach the tie-out. A console log does not count, so the overlay was a real painted layer.

# Voice

Headline: The short line sticks out.

Subhead: Marketplace payouts hit the stack. Ledgerline pulls the one that will not tie.

Button: Pull the short sheet

Empty state: This batch sat flush. Nothing to pull.

Footer: Ledgerline sample. Tear along the sprockets. If the lamp is still on, the batch is not done.

Consent and missing page: Lost the feed? This page tore off. The stack is back under the lamp. The night desk keeps the batch. No one else gets the sheet.

Loading: Advancing one line.

The footer is the oddly specific line. From that strip alone, this is the night payout desk.

# Genericness

Similar brief: the in-house payout screen of a marketplace, same columns of gross, fee, and net. The part this plan would have shared with them is a flush column with a status word beside the net. That part changed. The printed net sits on its own slip, shifted off the bars, and the other batches are a thick sheet, a thin clipped sheet, and a torn sprocket, not a status column. A status word would still fit the in-house screen. The slip and the tractor holes would not.
