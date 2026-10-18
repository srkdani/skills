# Techniques

Use a technique only when the storyboard names it. A page that uses more than three is too many. Values marked source come from a published case study. Values marked proposed are defaults for this skill. A named site lends one decision, not its concept.

1. Metaphor light or material overlay. When the brand is a physical condition. Shadow or color layer at opacity 0.15 to 0.35, `mix-blend-mode: multiply`, sway 8 to 14s, ease in and out, paused off screen (proposed). Build it from a few blurred shapes or one texture of that material.

2. Branded preloader. When the mark can be built from parts, and the page is not task-focused. Total under 1.2s, never block past 1.5s, skip on repeat via `sessionStorage` (proposed). Content is in the DOM behind it.

3. One object carries the story. When the product has a journey. ScrollTrigger scrub 0.6 to 1, pin 200 to 220vh (proposed, capped so the page does not feel stuck). One SVG changes state. Text sits beside it, at most 18 words, not on top of it.

4. Content as objects. For any list of products, works, or chapters. CSS perspective 1200 to 2000px. Stacked spines can use rotateX 50 to 70deg (proposed). Each object differs in size, label, or wear.

5. Shared-element transition. When a click opens a detail. Flip duration 1.2s, `expo.inOut` (source). The clicked object becomes the next view. Do not crossfade the whole page.

6. Chaos resolves to order. When the brand tension is raw versus finished, or free versus strict. Scatter, then resolve. Duration about 2s, `expo.inOut`, stagger 0.05s. Reverse about 1.2s, `power4.inOut` (source). Wait for `document.fonts.ready` before measuring. On a narrow screen, do not scatter. Show the ordered state.

7. Split-screen clip. For two states of one brand. `clip-path: inset()` from opposite edges, both driven by one progress value (source). No opacity toggling.

8. Proximity type field. When type, sound, or response is the product. Several rings, weight and color change with distance (source idea). Write CSS variables from a rAF loop. On touch, render a static frame. Do not use this as decoration on body copy.

9. Character reveal or scramble, headlines only. When the brand is precise, technical, or about time. Character stagger amount 0.4 to 0.8s, from random. Scramble 0.8 to 1.2s (proposed). Play once. Real text stays in the DOM for assistive tech. Never on body text.

10. Pointer as a tool. Only when the concept has a verb (stir, pull, cut, light). A trail, if you use one, stays short (radius under 0.1 of the view, life under 600ms) (source scale). Build the scroll or slider version first. A ring that only follows the pointer is banned.

11. Self-drawing doodles. Warm, handmade brands. Draw 500 to 800ms, then a small settle with `back.out(1.4)` (proposed). Round caps, 1.5 to 2.5px. Doodles sit inside sentences or on objects. Geometric only.

12. A character that acts on the UI. Playful brands. At least three poses: idle, act, rest. Idle loop 2 to 4s, paused off screen (proposed). Build from circles and rounded rects.

13. Restricted palette drawings. When the brand wants wit without photos. One ink, one color, one accent used only on the action. Same stroke weight everywhere. Wobble, if needed, with a displacement scale of 2 to 4 (proposed).

14. Grain and print texture. Only when the harvest names film, risograph, paper, or dust. Turbulence base frequency 0.65 to 0.8, 3 octaves, opacity 0.05 to 0.12, overlay or soft-light (source range). Tile it. Do not animate a full-screen filter.

15. One grade on every image. When pictures exist and would otherwise clash. Duotone or a single brand hue (proposed). Mixed generated images get the same grade.

16. Brand-native display type. Display at least 4 times the body size. At 1440 wide, that often means 96 to 180px. Tracking about -0.03em to -0.05em if the face can take it (observed range on large display type). Pick the face because of the world: stencil for crates, a stamp for tickets, a technical face for a panel. Do not pick a face because it looks "editorial".

17. Shaped seams. When the world has a physical edge (torn paper, a wave, a ticket perforation). Wave amplitude 8 to 24px (proposed). An SVG mask or a clip path. One seam, not every section.

18. Instrument readout. Only when the metaphor is a lab, a machine, a vehicle, or an archive. Mono labels at 10 to 12px with a live value (proposed). Mono eyebrows on a normal marketing page are banned.

19. Interface metaphor. A fake OS, magazine, ticket, receipt, or packet, for nostalgic, printed, or event brands. The real action is reachable in one tap (proposed). The metaphor is the page, not a frame around a normal page.

20. Scroll or drag scrub of a sequence. When the product has a tactile action. If you use video, short keyframe intervals keep the scrub honest. Provide a stepped control under reduced motion. Do not scrub the body text.

21. Shallow parallax. A portrait or product with 2 to 3 cut-out layers, or a depth shift of 1 to 3% of width, pointer lerp about 0.08 (proposed). Off on touch and reduced motion.

22. Horizontal pinned gallery. Galleries and media only, never the main text. Distance is the track width minus the viewport. `invalidateOnRefresh`. Wait for fonts before measuring. Keep a vertical escape.

23. Copy as a surface. Headline under 8 words (proposed). Rewrite the title, the button, the empty state, the footer, the consent line, and the loading line. If the footer could belong to another brand, rewrite it.

24. One fidget. Every brand, one per page. It responds in under 100ms (proposed). A click that recolours, a dial, a hidden state. It is not a second hero.

25. Opt-in sound. Music, food, games, instruments, night events. Default off, with a visible toggle (source pattern). Clips 50 to 200ms for UI, longer only for a real sample the user asked to hear. Never autoplay.

26. Generative piece tied to the concept. Data, science, weather, music, growth. Budget under 3ms a frame, pause off screen (proposed). It must form the concept's shape. A network of nodes and lines is banned.

27. Motion personality. Product UI under 300ms, ease-out (source guidance). Heavy or architectural: 0.9 to 1.4s, `expo.inOut`. Playful: `back.out(1.4)`, once. Mechanical: `steps(n)` or linear. Calm: slower `sine.inOut`. Write one sentence in the plan. Do not default to `cubic-bezier(0.16, 1, 0.3, 1)`.

28. Live context. Brands tied to time or place. Read the local hour once on load (proposed) and change a real state: light, copy, which object is forward. A clock that does not change the page is decoration.
