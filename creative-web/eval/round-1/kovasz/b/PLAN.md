# Kovász sample, plan

## Harvest

Facts only this bakery has:

1. The shop is in Budapest.
2. The bake starts at 11pm and runs overnight.
3. The door opens at 6am.
4. The starter is 41 years old.
5. The starter was carried from a grandmother's village.
6. The boards are bare by noon. They sell out.
7. The name Kovász is the Hungarian word for the leaven itself.
8. The starter lives in a jar on the bench: sour, bubbled, grey at the skin. Physical.
9. Flour dust sits on the bench, the peel, and the baskets after the night's folds. Physical.
10. The oven mouth is the lamp in the room from 11pm until the loaves come out. Heat, orange, iron. Physical.
11. Loaves are scored before they go in. The blade, the slash, the ear. Physical.
12. Proofing baskets leave a flour ring when the dough is turned out. Physical.
13. The crust crackles as it cools on the counter before the latch goes up. Sound, temperature.
14. By noon the only things left on the wood are crumbs, flour rings, and a chalk mark. Physical.
15. Customers who want a loaf have to be at the door at 6, because the afternoon has nothing to sell.
16. The enemy is a loaf still sitting at 1pm, and a dough raised on yeast that has no village and no age.

At least six are physical or sensory: the jar, the flour dust, the oven mouth, the score, the basket ring, the crackle, the crumbs.

## Emotion

Hunger.

A visitor says: "I walked from the night bench to the noon window and the boards were already bare."

## Concepts

The site is the bakery's own night, where 11pm, 6am, and noon are three rooms you walk through and the lamp changes with the room.
Rival: a Vienna sourdough shop that stays open all afternoon. They have no 11pm oven room and no boards cleared by noon. Keep.

The site is one banneton on the bench, where the flour ring is the proof and tipping the basket shows the loaf.
Rival: a shop that sells proofing baskets. They ship empty baskets. They do not tip out a loaf that started at 11pm. Keep.

The site is grandmother's jar, where each bubble is a year and feeding it writes the bread.
Rival: a kombucha cellar with a mother jar. The jar picture fits them. FAIL.
Replaced: The site is the door latch, up only from 6 until the boards are bare.
Rival: a breakfast cafe with a morning latch. A latch alone fits them. FAIL.
Replaced: The site is the chalk by the door, where the loaves are written at 6 and wiped by noon, and the only number left is 41.
Rival: a cafe specials board. They wipe specials, but the number that survives is not a 41-year village starter. Keep.

Three different metaphors: rooms of a night, a basket, a chalk board.

## Pick

The three rooms. Walk into the place.

The visitor sentence comes true because the page is the walk: night kitchen, morning counter, noon boards. You see the shelves empty by standing in the last room. The jar, the baskets, and the chalk are objects in those rooms. They are not a second concept.

Rejected world, The verb: a knead or a score would fit any boulangerie, and the brief's fact is the clock of this room, not a technique demo.

Rejected world, Traveling object: seed to loaf is the journey every bakery site tells. This one is a room you can only stand in between 6am and noon, after an oven that started at 11pm.

Motion kept: mechanical detents. The oven dial, the latch, and the stamp are machines. 120ms a step, `steps(6)` or linear, no overshoot.

Picture kept: plate and stamp. The oven wears a serial plate, the bags wear batch marks, noon wears one red correction.

## Visual system

- Material: soot-iron oven and oak bench, because the bake starts at 11pm on a wooden bench in front of an iron oven, with flour on both.
- Light: the oven mouth at 11pm, because that mouth is the lamp until dawn. The page is as dark as that kitchen. Noon does not invent a new palette: the same flour color floods the window, because by noon the sun is on the empty boards and the oven is no longer the lamp.
- Palette, five hex values from those materials:
  - `#1A1410` soot, because the 11pm wall and the oven iron are the same dark.
  - `#E0893C` oxide, because the oven mouth is the only glow, and it stays inside the arch.
  - `#E4D7C4` flour, because the dust, the dough, the tags, the clock face, and the noon window are flour.
  - `#7A4B2C` oak, because the bench, the peel, the door, and the empty boards are wood.
  - `#B42318` stamp red, because the sold-out mark and the batch correction are stamped, and this color is only the stamp and the main action.
- Type: display "Saira Condensed" 800, file from `https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@600;800&family=Albert+Sans:wght@400;600;700&display=swap`. Body "Albert Sans" at 18px. Display 152px at 1440 wide, more than 8 times the body, tracking -0.03em, because the oven plate and the sold-out board are condensed sign letters and "Kovász" has to fit the metal. Uppercase on the plate. No italic.
- Picture rule: plate and stamp, kept. Thin rules on the oven plate and the window muntins, stamped serials, one red correction only on marks and the main action. The page is handled: the peel is cropped by the frame, the ticket and the sack have a punch hole, the serial is K-41. Not a hairline grid on every edge.
- Motion: mechanical family, kept. `steps(6)` or linear, 80 to 160ms a step, no overshoot, because the dial and the latch click. Repeated controls, the range detents included, do not use a soft landing. There is no menu. The jar tap answers in under 100ms.
- Sound: none.

## Objects

| Content | Object | id | How instances differ |
| --- | --- | --- | --- |
| The 41-year village starter | Glass jar with a hanging tag | `#jar` | One jar. Tag says the village and 41. Tap shows a scratched 41 that the others do not have. |
| The night bake | Oven, dial, and the dough on the bench | `#oven` `#dial` | Six states of one bench: fed, folded, proofing, scored, in the mouth, cooling. Size and tool change each stop. |
| What they sell in the morning | Loaves on the counter | `#loaves` | Four loaves, different size, score, flour coat, and tag. One tag is torn. One is a heel. |
| Hours | Wall clock and door latch | `#clock` `#latch` | Clock is stuck at 11 in the first room. Latch is up only in the 6am room. |
| The sell-out | Chalk board and flour rings | `#chalk` `#boards` | Rings differ in width and how rubbed out they are. The board carries the red stamp. |
| The walk | Ticket on the bench | `#ticket` | One ticket, punch hole, the only red button. |
| The peel | Foreground crop | `#peel` | One paddle, cut off by the frame. |
| The sack | Footer pantry | `#sack` | One sack, serial, punch hole, sample stamp. |

`data-object` values: jar, oven, loaf, board, sack, peel, latch.

No row of identical cards. The morning loaves are a pile, not a grid.

## Storyboard

Budget: one hero signature, two supporting moments, one delight, one small surface. Everything else is static and readable. No pin. Rooms stack in normal scroll. Techniques named here: shallow parallax, mechanical detents, live hour. Three, no more.

0 to 30% of the scroll: you are in the 11pm kitchen. `#scene` is the room: soot wall and oven (back), oak bench with jar and dough (mid), cropped peel (front). The signature is the oven dial, `data-signature` on `#dial`. Turning it steps the bench through six stops, because the night is a machine. A range input does this on touch and on a pointer. On a fine pointer only, the mid layer shifts by 2% of its width and the front by 3%, lerp 0.08. Touch keeps the layers still. The headline sits on the oven plate, left, not centered over the dark. The ticket "Walk in at 6" is on the bench in the first viewport. A first visit steps the hour hand from 12 to 11 in 0.6s, skippable, skipped if `sessionStorage` already has the tick. It does not cover the headline. On load, the local hour writes one plate: oven on, latch up, or boards bare, because this bakery is a clock.

30 to 62% of the scroll: the 6am room, its own wall, counter, and cropped bag. The latch clicks from shut to open in six detents as the room arrives, because they open at 6. The still picture already shows it open, so a screenshot is the true room. Touch: tap the latch and it detents. Loaves differ. Words are on the door plate and the hanging tags.

62 to 88% of the scroll: the noon room. Flour-colored daylight fills the window. The shelves keep flour rings. The chalk already reads the empty line, and a second red impression of ELFOGYOTT strikes in steps as you arrive, because they sell out by noon. Touch: tap the board and the stamp strikes again.

88 to 100% of the scroll: the sack in the pantry corner. Static. Sample serial, punch hole, consent line.

Delight: tap `#jar`. In under 100ms a bubble steps up and the scratched 41 shows. `data-delight` on the jar. Works with a tap. No hover-only signature.

Small surface: `#sack` carries `data-small`.

## Removal

The flour-speck pointer trail. It will be built, then deleted. Specks follow the pointer and die in under 600ms. They do not change the room, the dial, or the hour. The concept is walking into three rooms, and touch never sees a trail. A speck behind the pointer is a costume. The oven dial is the motion that stays.

## Voice

Headline, under eight words: "Gone by noon."

Subhead: "We light the oven at 11. The door opens at 6. The jar came from a village and is 41."

- Button: "Walk in at 6"
- Empty state, on the noon chalk: "Nothing on the boards. The last crumb is still warm."
- Footer, on the sack: "The sack is empty by noon. The jar is not."
- Consent: "The clock reads your hour once, then forgets it."
- Loading, on the dial before the tick: "Lighting the oven."

The footer names the sack, the noon sell-out, and the jar. A stranger can tell the bakery from that line alone. The crumb line is the oddly specific one. No banned words.

Brand is labeled sample on the plate, the sack, and the title.

## Genericness

A similar brief: a Copenhagen bakery selling cardamom buns from 7:30 until 17:00.

The part I would have written for them is a shop counter with bread sitting on it in daylight. That would have been this page if the 6am room were the hero.

What changed: the first room is the 11pm oven, the lamp is the oven mouth, and the last room is empty on purpose. The Copenhagen shop would start in daylight and would still have buns in the afternoon. The dealt world stays: walk into the place.
