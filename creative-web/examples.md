# Examples

Three sample brands. Copy the specificity and the refusal to merge. Do not reuse these worlds, hex values, or typefaces on a new brand. Every name below is a sample.

## Sample: North Wharf oyster bar

Harvest: crushed ice, pewter cups, a shucking knife, lemon halves, paper tickets on a nail, boats at 4 am, tide chalked on a board, cold brine smell, one glove, the counter is zinc, shells in a bucket, they stop seating when the ice runs out.

Emotion: appetite. Take-out: "I watched the tide climb the zinc and the board change to whatever the boat brought."

Concepts:
- The site is a zinc counter where each oyster is a shell on ice and scrolling raises the tide. Rival: a downtown cocktail bar. FAIL, they could use a wet counter too. Replaced.
- The site is a ticket nail where today's catch is paper stubs and pulling one stub opens that boat. Rival: a cocktail bar. The nail and the boats do not fit. Keep.
- The site is a shucking glove where the menu is written on the fingers. Rival: a fish and chip shop. The glove could be forced onto them. FAIL.

Pick: the ticket nail. The visitor sees stubs change with the tide, which is the sentence.

Visual system:
- Material: wet zinc and cheap paper, because the counter is zinc and the tickets are paper.
- Light: overcast morning through a wet window, because boats come at 4 am. Bright, cold, not a dark restaurant.
- Palette: zinc `#A7B0AE`, ice `#E7EEEA`, brine `#1E3A36`, paper `#F3E6C8`, nail `#6E4A32`. Because those are the counter, the ice, the water, the ticket, the nail.
- Type: display "Ultra" for the stamped ticket words, because the tickets are rubber-stamped. Body "Literata". Display 92px, body 18px.
- Picture: cut paper. Shells are two flats and a shadow piece offset 6px.
- Motion: calm, `sine.inOut`, 1.1s, because cold water drifts. The tide moves. Nothing bounces.
- Sound: none.

Objects: today's oysters are stubs on the nail (`#stubs`), each a different length. Hours are the tide chalk (`#tide`). The knife is the delight (`#knife`), a click rocks it. The footer is the bucket of shells (`#bucket`).

Storyboard: 0 to 40% the tide rises over the zinc and the lowest stubs darken, because the seating ends when the ice is spent. Touch: scroll does this, no hover. Delight: click the knife, it turns once. Small surface: the footer bucket. Removal: a second ripple on the footer, deleted, because one tide is the story.

Voice: headline "Ice is the seating chart." Button "Pull today's stub." Footer "When the bucket is full, the boats won."

## Sample: Parcel and Pine movers

Harvest: raw pine crate, black stencil, wool blankets, a dollied stair, tape measure, 7 am start, one scuffed banister, cardboard smell, labels that say which room, two people, a handwritten "this side up", the truck door sticks.

Emotion: relief. Take-out: "A crate went up the stair and became my kitchen, and I could see which box."

Concepts:
- The site is one crate that travels porch, stair, and truck, and the rooms are stencils on its boards. Rival: a storage company. Their unit does not climb a stair. Keep.
- The site is a blanket fort. Rival: any home brand. FAIL.
- The site is a tape measure. Rival: a hardware shop. FAIL.

Pick: the crate. The visitor watches one object change rooms, which is the sentence.

Visual system:
- Material: pine boards and black stencil ink, because the crate is pine and the labels are stenciled.
- Light: a porch bulb at 7 am, mixed with grey street light, because they start at 7 am.
- Palette: pine `#C4A06A`, board shadow `#8A6A3E`, stencil `#16160F`, blanket `#B7C4BE`, porch `#D9D3C5`. Because those are the wood, the ink, the blanket, and the morning.
- Type: "Allerta Stencil" for labels, because the crate is stenciled. Body "Source Serif 4" at 18px. Display 88px. Tracking on the stencil 0.04em, because stencil faces need air.
- Picture: plate and stamp. One red correction only on "this side up".
- Motion: heavy, `expo.inOut`, 1.1s, short travel, because a crate is heavy. Menus are instant.
- Sound: none.

Objects: services are stencil faces on the crate (`#faces`), each a different word and board width. Prices are a tape-measure tick (`#tape`), marked sample. The stuck truck door is the footer (`#door`).

Storyboard: the crate is pinned through porch, stair, kitchen. Scroll rotates and wears the same SVG. Touch is the same scroll. Delight: double-click a board and the "this side up" stamp appears. Removal: a second crate in the footer, deleted, because one crate is the point.

Voice: headline "This side up the stairs." Button "Book the 7 am." Footer "The truck door sticks. We still make it."

## Sample: Ironweed Press

Harvest: a Chandler and Price press, cotton paper, one ink color per job, metal type in a galley, the chase (the locking frame), brayer, tympan, the shop smells like solvent and cotton, two people, they print until the ink is even, misregistration of a hair, drying rack.

Emotion: patience. Take-out: "I pulled the bar and the red pass landed a hair off the black one, on purpose."

Concepts:
- The site is the chase, and each project is a locked form you ink by scrolling. Rival: a digital print shop. They do not lock a chase. Keep.
- The site is a paper stack. Rival: a paper mill. FAIL, it fits them better.
- The site is a letter drawn huge. Rival: a type foundry. FAIL.

Pick: the chase. The visitor pulls a print, which is the sentence.

Visual system:
- Material: cotton sheet locked in a black iron chase, because that is the press.
- Light: a shop fluorescent over a white sheet, because you judge ink on white paper. The page is light. The iron is the dark part, not the background.
- Palette: sheet `#F7F4EC`, iron `#2A2E27`, ink `#B43328`, galley `#D8D2C6`, solvent stain `#E4D2A8`. Because those are the paper, the chase, today's ink, the tray, and a real stain. The cream is the sheet, not a theme.
- Type: "Bodoni Moda" only for the locked metal letters, because the type is the product. Body "Nunito Sans" is banned in spirit here: use "Atkinson Hyperlegible" at 18px. Display letters 120px.
- Picture: screenprint. Two inks, the red pass 2px off the black.
- Motion: mechanical, `steps(8)`, 120ms a step, because a press is a detent. No bounce.
- Sound: opt-in, one clunk of the bar, default off.

Objects: projects are locked forms in the chase (`#forms`), each a different lockup. The ink brayer is the control (`#brayer`). The drying rack is the footer (`#rack`).

Storyboard: scroll steps the brayer across the sheet and the red pass appears misregistered, because that is how they print. Touch: the same scroll, plus a range input under reduced motion. Delight: a tap on the galley sorts one letter upside down. Removal: a paper-grain overlay, deleted, because the misregistration already shows the process.

Voice: headline "Pull until it sits." Button "See the locked jobs." Footer "Two people, one chase, ink on our cuffs."
