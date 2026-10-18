# Harvest

Facts only this bakery has. The street, the village name, and the price were not given, so they stay unnamed or marked sample.

1. The mix starts at 11pm and runs through the night.
2. The door opens at 6am.
3. The basket is empty by noon.
4. The starter is 41 years old.
5. The starter was brought from the baker's grandmother's village. The village was not named.
6. Kovász is the Hungarian word for the leaven itself.
7. The shop is in Budapest.
8. Flour dust sits on the bench and on the palms (touch, sight).
9. At 11pm the dough is cool and slack. By morning it is taut (touch, temperature).
10. The oven throws a dry heat when it opens in the night (temperature).
11. The score crackles as it opens. Bakers call that jump oven spring (sound).
12. The crust smell reaches the door at 6am (smell).
13. A lame, a razor on a handle, cuts the skin before the bake (tool).
14. A wooden peel carries the loaf into the oven and back out at six (tool).
15. The dough sleeps in a linen cloth on the bench (material, ritual).
16. One bulb lights the bench at 11pm. At 6am the light is the open door (light).
17. The loaf sold at 6am is the same dough mixed at 11pm.
18. After noon there is nothing left to sell. The day ends when the basket does.

At least six of these are physical or sensory: flour dust, cool slack dough, oven heat, the crackle, the crust smell, the bulb against the morning door.

# Truths

1. The loaf you can hold at 6am is the same dough that went on this bench at 11pm. Rival: a hotel breakfast bakery that bakes frozen par-baked loaves delivered in the morning. They never have one dough working the night on a bench.
2. The starter in the jar is 41 years old and came from the baker's grandmother's village. Rival: a new sourdough shop that grew a starter this year or bought one. They do not have this jar.
3. The basket is finished by noon. Rival: a supermarket bakery that restocks all afternoon. Their shelf is not a clock that ends at noon.

# Emotion

Appetite.

"I ran one loaf from a slack mix at eleven until the cut sprang open, and the basket was already thinning."

# Concepts

The site is a night bench where one dough changes from a slack mix at eleven to a cracked crust at six, and scrolling the bench does the bake. Rival: a hotel breakfast bakery that receives frozen par-baked loaves. They have no bench and no living dough. Keep.

The site is a linen couche, and each fold is a loaf you unroll. Rival: a croissant shop that proofs on cloth. The line still fits them. FAIL.

The site is the grandmother's jar, and tipping it shows which loaf is still alive today. Rival: a new bakery that bought a starter last season. They do not have a 41-year village jar. Keep as an alternate, not the pick.

The site is a street queue where the gaps are people waiting. Rival: a brunch cafe. A queue fits them. FAIL.

The site is the noon basket, and each gap is a loaf that already left. Rival: a supermarket bakery that refills the shelf. An empty gap is not their story. Keep as an alternate, not the pick.

# Pick

The night bench. The visitor scrolls one loaf from a slack mix to a cracked crust, which is the sentence they would tell a friend. The jar and the basket stay objects on that bench. They are not a second site. Material weather is rejected: steam and a swaying light would show heat, and this shop's story is the dough changing, not a weather layer. Worker in the room is rejected: a geometric baker would mime the work, and the sentence is about the loaf itself. A character beside the bench would be a mascot parked near the process.

Motion is accepted from the deal. Spring, `back.out(1.4)`, 0.45s, once, because oven spring is the one jump a loaf makes and then it stops. It plays on the ear when the bake stage arrives. It does not bounce every block. Picture rule is accepted. Ink and one fill, 1.75px round caps, a displacement wobble of scale 3, because the bench is drawn in pencil and dough, and detail is not the point.

# Visual system

The page is a floured beech bench because the dough is worked on wood that stays dusted from eleven until the peel.

The light is one baker's bulb at 11pm because that is when the mix starts. The work surface stays pale because flour under that bulb is pale. The wood rim is the unlit edge of the bench. This is not a dark room and not a paper sheet.

Palette, from that bench:

- `#6B4428` bench wood, because oiled beech at the rim and the front lip is this dark honey in the bulb.
- `#E8DCC0` dough fill and flour dust, because an unbaked loaf and the dust on the bench are the same pale crumb.
- `#1C1612` ink, because the crust edge and the baker's pencil are the same dark brown.
- `#8C3418` oven mouth, because that is the only hot color in the room at night, and it sits only on the hold action.

Type: display is Alfa Slab One, file `fonts/alfa-slab-one.woff2`, because a bread stamp is a heavy slab pressed into the dough. Body is Figtree, file `fonts/figtree.woff2`, because the bench notes are plain working type, not a second stamp. Display is 92px on a wide screen and 60px on a narrow one. Body is 18px wide and 15px narrow. 92 is more than four times 18, and 60 is four times 15, because the stamp has to dwarf the note.

Picture rule: ink `#1C1612` and one fill `#E8DCC0`. Stroke 1.75px, round caps. Wobble via `feDisplacementMap` scale 3 on the loaf and the jar. No gradients as shading. The picture is the bench, the loaf, the jar, the lame, the peel, the cloth, and the rack. No photographs. Missing street and village stay unnamed rather than fake pictures.

Motion: spring family, `back.out(1.4)`, 0.45s, once, on the ear at oven spring. The rise itself is a scroll scrub, 0.7, because the night is a long change and the spring is the one jump inside it. Small taps stay under 300ms and do not bounce. Repeated taps (taking a loaf) are instant. The hold confirmation is instant, because a person trying to get bread should not wait on a bounce.

Sound: none.

Grade: one ink on dough fill, under the bulb. The whole page uses that drawing. GRADE comment names it. There is no second grade.

# Objects

| Content | Object | id | How instances differ |
| --- | --- | --- | --- |
| The night loaf | one dough on the bench | `#loaf-wrap` `data-object="loaf"` | Same shape, five states: slack, domed, scored, sprung ear, sitting on the peel. Scale and the cut change. Fill does not. |
| The starter | glass jar | `#starter` `data-object="starter"` | One jar. Closed label names 41 years. Open label names the feed and her village. Flour ring on the lid. |
| The sell-out | linen basket | `#basket` `data-object="basket"` | Three loaves from one dough, different sizes: round, long, heel. Each can leave. After noon the cloth starts empty. |
| Place, hours, price | wooden peel | `#peel` `data-object="peel"` | One peel. The blade carries Budapest, the clock, and a sample price. Not a row of cards. |
| The bulb | hanging bulb | `#bulb` `data-object="bulb"` | Lit during the night bake, filament hidden once the door light takes over, word changes with the hour. |
| Stage note | paper scrap | `#note` `data-object="note"` | One scrap. The sentence swaps with the stage. It does not cover the loaf. |

# Budget

Every idea names a truth.

Small:

1. `#live-line` truth 3, `data-live="time"`. Local hour sets the line: bulb still on (11pm to 6am), door open (6am to noon), or past noon and the basket empty. Also sets the tab title.
2. `#bulb` truth 1, `data-live="time"`. The same hour lights the filament or turns it off, because the bulb is the overnight work light.
3. `#lame` truth 1. Tap scores the loaf. The razor flicks and returns. Under 300ms. Touch is the tap.
4. `#flour-ring` truth 2. Tap spins the dried ring on the 41-year jar. Under 300ms.
5. `#rack` truth 1. The footer is the cooling rack, the place the night loaf rests, not a link row.

Medium:

1. `#starter` truth 2. Tap "Read the jar". The label swaps from "41 years in this glass." to "Fed before the mix. Brought from her village." The glass tilts once and stops. Touch is the same tap. Reduced motion swaps the words with no tilt.
2. `#basket` truth 3. Tap a loaf to take it. Round, long, and heel are different sizes. The count drops. The last tap shows "Noon took the last crust. The jar did not notice." If the local hour is already past noon, the cloth starts empty and "Put the morning back" restores the three loaves so the tap still works. Repeated taps are instant.

Big:

1. `#loaf-wrap` truth 1. The signature. One loaf on the bench. Scroll runs five stages. Touch is the same scroll. Reduced motion shows stage one and a "Next stage" control, with no pin and no travel.

Storyboard:

- 0 to 30% of the scroll: the slack eleven o'clock mix tightens and domes, because truth 1, the same dough works all night. Touch is that scroll. Reduced motion: the step control moves one stage with no travel.
- 30 to 55%: the lame score draws across the skin, because truth 1.
- 55 to 80%: the ear springs open with one `back.out(1.4)` of 0.45s, because truth 1, oven spring, then it stops. The body scale also peaks and settles as the scroll moves through this beat.
- 80 to 100%: the loaf settles and the peel slides under it. The note says six, because truth 1, the door is about to open.

Pin travel is one viewport, under the 220vh cap. A longer empty track read as a blank band, so the track under the bench holds the opened loaf, the end of the same dough. The headline, the hold button, and the hours stay on the bench during the pin, so nobody has to finish the night to know when to come.

# Rhythm

1. Night bench: a pinned work surface, one loaf changing, one scrap of note, the hold action on the front lip.
2. Basket: one cloth you reach into, three loaves of different sizes, no heading block above a grid.
3. Peel: one long paddle, place and hours and sample price written along the blade.
4. Rack: wires and one closing slip.

No section repeats heading, then text, then cards.

# Removal

Build a dotted hour rail on the left rim of the bench, five dots that mark the stage, then delete it. The world forbids a dotted timeline, and the loaf's own change is already the clock. A second clock does not serve the bench. Leave the REMOVED comment.

# Voice

Headline: "One night loaf."

Subhead: "From a 41-year jar, on the bench until six."

Button: "Hold the six o'clock loaf"

Empty state: "Noon took the last crust. The jar did not notice."

Footer: "Kovász, sample. Budapest. We mix at eleven and the basket is a rumor by noon."

Missing page: "Sample page. This is not a real order. If it overproofed, walk back to the bench."

Loading: "Flour on the bulb. Almost."

The empty state is the oddly specific line. The footer alone names the bakery, the city, the night mix, and the noon basket. The brand is marked sample in the top bar and the footer. The 1900 forint price is sample. No street and no village name were invented.

# Genericness

A similar brief is a daytime bakery that sells pastries until evening. For them this plan would have drawn a case of many buns and a standing menu. That part is changed. There is one loaf, the clock is 11pm, 6am, and noon, and the jar is 41 years from her village. There is no pastry case and no menu of flavors.

# Batch 1 gate

The signature is the one loaf on the bench. Scroll advances the stages. The headline and the hold action are visible before the pin finishes. The scene is the bench, not a text column.

# Batch 2 gate

GRADE is one ink on dough fill, bulb-lit bench. The scene is drawn with SVG shapes in that ink and that fill. The motion library named in the skill is loaded. No second grade.

# Batch 3 gate

Two medium interactions: the jar's second state, and the basket loaves. Each has a tap path. No third medium.

# Batch 4 gate

Five small details are on the page: the live hour line, the bulb, the lame, the flour ring, and the cooling rack. The hour line and the bulb use data-live time.

# Batch 5 gate

Reduced motion drops the pin and the travel and keeps a Next stage control. Narrow screens restack the bench. The hold action stays immediate. The hours stay on the lip.
