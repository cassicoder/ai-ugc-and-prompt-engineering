# Video Prompts (Kling 3.0)

For Higgsfield Kling 3.0 video generation. 9:16. 15 seconds. Sound on. Image-to-video with the generated product image as start frame.

---

## Settings

```
model: kling3_0
mode: std       (use pro only for keepers)
aspect_ratio: 9:16
duration: 15
sound: on
medias: [{role: "start_image", value: "<generated image job ID>"}]
```

---

## The locked template

```
[FORMAT / FRAMING].
[HUMAN BLOCK — same as image].
Setting: [3-5 setting items].
Multi-shot enabled.
Shot 1 (0-5s): [camera + action + endpoint].
Shot 2 (5-10s): [camera + action + endpoint].
Shot 3 (10-15s): [camera + action + endpoint].
As the [thing] moves, the [light/element] shifts across the [surface].
Audio: [SPEAKER TAG] (0-15s, continuous, no pauses, starts at frame 1): "[DIALOGUE]".
Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

Target length: 110–145 words. Single paragraph when sent.

---

## Multi-shot timeline

15 seconds = 3 shots × 5 seconds each. This works because:
- Kling 3.0 dialogue drifts past 5s without a shot change
- Multi-shot keeps the viewer's eye moving
- Each shot gives a fresh visual beat for one script line

### Endpoint rule

Every camera move and every hand action needs a defined endpoint. The model treats prompts without endpoints as "open-ended" and produces erratic moves.

Bad: `Camera slowly tilts up.`

Good: `Camera slowly tilts up the post to the double-tier roof, ending framed on the upper tier.`

### Camera vocabulary

Safe:
- `slow dolly forward toward [X], ending close on [Y]`
- `slow pull back to chest distance, ending at start framing`
- `slow pan right across [X], ending on [Y]`
- `slow tilt up [X] to [Y], ending at [Z]`
- `static handheld with subtle micro-shake only`

Banned:
- `0.5x` / `ultrawide` / `fisheye` — fisheye artifacts
- `whip pan` / `crash zoom` / `dolly zoom` — erratic motion
- `tilt` alone without endpoint — product magically grows on screen
- `growing` / `rising` — same problem

### Hand action vocabulary

Same structure. Every action has an endpoint.

Bad: `Hand moves toward the product.`

Good: `Hand reaches out from the right, fingers grip the chrome handle, ending fingers wrapped around the handle.`

Safe actions:
- `fingers tap the surface twice, ending hand still on surface`
- `hand slides from [X] to [Y] along the edge, ending at [Y]`
- `fingers grip the pull, pulling [direction] [distance], ending [open/closed]`
- `thumb presses the button, ending activated`
- `hand rotates the device [degrees], ending angled toward camera`

---

## The realism phrase (single biggest realism upgrade)

Include this sentence after the timeline blocks:

```
As the [hand / camera] moves, the [daylight / amber light] shifts across the [surface].
```

Why: This makes Kling animate light response to motion. Without it, lighting is static and feels CGI.

Variations:
- `As the camera moves, the daylight shifts across the wood`
- `As the hand moves, the amber light shifts across the marble`
- `As the chair swings, the light shifts across the rattan weave`

---

## Audio / speaker tag

```
Audio: [Speaker: <voice description>] (0-15s, continuous, no pauses, starts at frame 1): "<dialogue>"
```

### The locked voice persona

```
young American male mid-twenties, warm expressive gay-best-friend voice, animated and excited like he's telling his girl about a find, light theatrical lilt, crisp clear English, pronounces ORANGE clearly as orange not ornage, natural inflection, not flat, not robotic, not salesy
```

Why each token matters:
- `young American male mid-twenties` — anchors age, gender, accent
- `gay-best-friend voice` — drives expressive inflection
- `like he's telling his girl about a find` — drives natural enthusiasm
- `light theatrical lilt` — controlled, not over the top
- `pronounces ORANGE clearly as orange not ornage` — Kling specifically fumbles "orange"
- `natural inflection, not flat, not robotic, not salesy` — three negation guards

---

## Dialogue rules

- **Length:** ~40 words to fill 15 seconds without repeating
- **Timing tag:** Always `(0-15s, continuous, no pauses, starts at frame 1)` — frame-1 start prevents the dead-air opening
- **CTA:** Always end with `click the orange cart below`

### Pronunciation traps

| Word | Behavior | Fix |
|---|---|---|
| `orange` | Kling sometimes says "ornage" | Reinforce in speaker tag: `pronounces ORANGE clearly as orange`. NEVER respell as `or-anj` — the dash is read literally. |
| `Pinterest` | Mispronounced as "Pintrest" | Don't use. Say `online` or `scrolling`. |
| `HomeGoods` | Mispronounced + competitor brand | Say `the home store`. |
| `Wayfair` | Mispronounced + competitor brand | Say `the furniture site`. |

If a word still fumbles in output after speaker-tag reinforcement, **replace the word entirely** rather than respelling. E.g. `the orange cart` → `the cart icon below`.

---

## Banned phrases for Kling

| Banned | Why |
|---|---|
| `iPhone 15 Pro main lens` | Triggers ad polish |
| `cinematic` | Hollywood polish |
| `4k quality` / `HDR` | Already set / causes oversaturation |
| `tilt up` without endpoint | Subject grows on-screen |
| CAPS for emphasis | Model often does opposite |
| `--no [thing]` | Doesn't parse |
| `(Style: realistic)` | Stylization tags ignored or harmful |

---

## Closer (locked)

Same as image prompts:

```
Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

---

## Worked example — Folding Camping Chair

```
First-person POV, vertical 9:16, the camera is the creator's eyes looking forward at a black folding camping chair set up on a wooden cabin deck. A man's right arm extends forward from the bottom-right, fingers gripping the chrome flip-up armrest at waist height. Sage green quarter-zip pullover sleeve cuff at the wrist. Setting: a half-empty enamel mug on the deck, a folded plaid blanket on the seat, a stack of two paperback books at the chair's foot. Multi-shot enabled. Shot 1 (0-5s): wide on the full chair, hand on the chrome armrest, ending fingers tapping the armrest once. Shot 2 (5-10s): slow dolly forward to the seat cushion, hand sliding to the cup holder, ending fingers resting on the cup holder rim. Shot 3 (10-15s): slow pull back to chest distance, hand returning to the armrest, ending at the start framing. As the hand moves, the amber light shifts across the wood deck. Audio: [Speaker: young American male mid-twenties, warm expressive gay-best-friend voice, animated and excited like he's telling his girl about a find, light theatrical lilt, crisp clear English, pronounces ORANGE clearly as orange not ornage, natural inflection, not flat, not robotic, not salesy] (0-15s, continuous, no pauses, starts at frame 1): "My grandma's been struggling at our family camping trips — her old chair killed her back. Got her this one and she actually wants to come now. Holds four hundred and fifty pounds, padded headrest, cup holder built right in, folds completely flat. Huge sale right now, click the orange cart below." Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

---

## Troubleshooting

### Dialogue repeats in output

Cause: script too short, Kling loops to fill 15s.
Fix: stretch script to ~42 words minimum, 3 distinct beats. Add `I'm telling you` or `genuinely obsessed` filler if short.

### Dead air at start

Cause: Kling adds default breath/setup lead-in.
Fix: ensure speaker tag includes `(0-15s, continuous, no pauses, starts at frame 1)`. Open dialogue with a sharp consonant (S, P, W, K, Y).

### Camera move erratic

Cause: banned camera language or no endpoint.
Fix: use only safe vocabulary from "Camera vocabulary" above. Every move needs an endpoint.

### Hand disappears mid-clip

Cause: start image didn't include the hand, but prompt described one — Kling hallucinated then dropped.
Fix: either (a) make the start image include the hand anchored to a specific product part, OR (b) prompt for true "no person in frame" with framing tight enough that there's no space for a hand.
