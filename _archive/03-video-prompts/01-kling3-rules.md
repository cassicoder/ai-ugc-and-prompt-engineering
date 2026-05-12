# 03.01 — Kling 3.0 Video Rules

For Higgsfield's Kling 3.0 video generation. 9:16. 15 seconds. Sound on. Image-to-video with the generated product image as start frame.

---

## Tool settings

```
model: kling3_0
mode: std (use pro only when std quality is insufficient)
aspect_ratio: 9:16
duration: 15
sound: on
medias: [{"role": "start_image", "value": "<UUID of generated image>"}]
```

`std` is the default. `pro` costs more and only matters for keepers.

---

## The skeleton

```
[FORMAT / FRAMING]. [HUMAN BLOCK — same as image]. Setting: [3-5 SETTING ITEMS]. Multi-shot enabled. Shot 1 (0-5s): [CAMERA + ACTION + ENDPOINT]. Shot 2 (5-10s): [CAMERA + ACTION + ENDPOINT]. Shot 3 (10-15s): [CAMERA + ACTION + ENDPOINT]. As the [thing] moves, the [light/element] shifts across the [surface]. Audio: [SPEAKER TAG] (0-15s, continuous, no pauses, starts at frame 1): "[DIALOGUE]". [AUTHENTICITY CLOSER].
```

Target: 110-145 words. Single paragraph. No JSON. No CAPS.

---

## Section 1 — Multi-shot timeline

15 seconds = 3 shots × 5 seconds each (default). This works because:
- Kling 3.0 native dialogue drifts past 5 seconds without a shot change
- Multi-shot keeps the viewer's eye moving
- Each shot gives a fresh visual beat for the script line

**Endpoint rule:**
Every camera move and hand action needs an endpoint. The model treats prompts without endpoints as "open-ended" → produces erratic moves.

Bad:
```
Camera slowly tilts up.
```

Good:
```
Camera slowly tilts up the post to the double-tier roof, ending framed on the upper tier.
```

**Camera move vocabulary (safe):**
- "slow dolly forward toward X, ending close on Y"
- "slow pull back to chest distance, ending at start framing"
- "slow pan right across X, ending on Y"
- "slow tilt up X to Y, ending at Z"
- "static handheld with subtle micro-shake only"

**Camera move vocabulary (banned):**
- `0.5x` / `ultrawide` / `fisheye`
- `whip pan` / `crash zoom` / `dolly zoom`
- `tilt` alone without endpoint
- `growing` / `rising` (makes products magically scale up)

---

## Section 2 — Hand action timeline

Same structure as camera. Each action has an endpoint.

Bad:
```
Hand moves toward the product.
```

Good:
```
Hand reaches out from the right, fingers grip the chrome handle, ending fingers wrapped around the handle.
```

**Common safe actions:**
- "fingers tap the surface twice, ending hand still on surface"
- "hand slides from X to Y along the [edge/top/side], ending at Y"
- "fingers grip the [pull/handle/edge], pulling [direction] [distance], ending [open/closed/extended]"
- "thumb presses the [button/toggle], ending [activated]"
- "hand rotates the device [degrees], ending [angled toward camera]"

---

## Section 3 — The realism phrase

Include this exact sentence after the timeline blocks:

```
As the hand moves, the light shifts across the [surface].
```

Variations:
- "As the camera moves, the daylight shifts across the [marble / wood / fabric]"
- "As the hand moves, the amber light shifts across the wood"
- "As the chair swings, the light shifts across the rattan weave"

Why: This phrase makes Kling animate light response to motion, which is the single biggest realism upgrade in a Kling clip. Without it, the model often renders shots where lighting is static and feels CGI.

---

## Section 4 — Audio / Speaker tag

Exact structure:

```
Audio: [Speaker: <voice description>] (0-15s, continuous, no pauses, starts at frame 1): "<dialogue>"
```

**The locked voice description:**

```
young American male mid-twenties, warm expressive gay-best-friend voice, animated and excited like he's telling his girl about a find, light theatrical lilt, crisp clear English, pronounces ORANGE clearly as orange not ornage, natural inflection, not flat, not robotic, not salesy
```

**Why every part of this matters:**
- "young American male mid-twenties" — anchors age/gender/accent
- "gay-best-friend voice" — drives expressive inflection
- "animated and excited like he's telling his girl about a find" — drives natural enthusiasm
- "light theatrical lilt" — controlled, not over-the-top
- "crisp clear English" — pronunciation guard
- "pronounces ORANGE clearly as orange not ornage" — Kling specifically fumbles "orange"
- "natural inflection, not flat, not robotic, not salesy" — three negation guards

---

## Section 5 — Dialogue rules

- **Length:** ~40 words to fill 15 seconds without repeating
- **Timing tag:** Always `(0-15s, continuous, no pauses, starts at frame 1)` — frame-1 start prevents the dead-air opening
- **Pronunciation traps:** spell phonetically in the speaker tag
  - ORANGE → orange
  - Pinterest → don't use (Kling mispronounces "Pintrest")
  - Compound brand names (HomeGoods, BestBuy) → replace with generic equivalent ("the home store")
- **CTA:** Always end with "click the orange cart below" (or "click the orange cart below" if pronunciation guard active)

---

## Section 6 — Banned phrases for Kling

| Banned | Why it fails |
|---|---|
| `0.5x ultrawide` | Causes fisheye artifacts |
| `iPhone 15 Pro main lens` | Triggers ad polish |
| `cinematic` | Hollywood polish |
| `tilt up` (without endpoint) | Makes product grow on-screen |
| `4k quality` | Already quality-set |
| `HDR` | Causes oversaturation |
| CAPS for emphasis | Kling does the opposite |
| `--no [bad thing]` style negatives | Doesn't parse |
| `(Style: realistic)` | Stylization tags ignored or harmful |

---

## Section 7 — Authenticity closer

Same as image prompts:

```
Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

---

## Full prompt template (copy this)

```
First-person POV, vertical 9:16, the camera is the creator's eyes looking [direction] at [product] in [setting]. A man's right arm extends forward from the bottom-right, hand resting [verb] the [specific part] at [waist/chest] height. [ARM CLOTHING]. Setting: [item 1], [item 2], [item 3]. Multi-shot enabled. Shot 1 (0-5s): [wide on full product, hand on X, ending fingers tapping Y once]. Shot 2 (5-10s): [close on Z, hand sliding to W, ending fingers on V]. Shot 3 (10-15s): [pull back wide, hand back on X, ending at start framing]. As the hand moves, the [light source] shifts across the [surface]. Audio: [Speaker: young American male mid-twenties, warm expressive gay-best-friend voice, animated and excited like he's telling his girl about a find, light theatrical lilt, crisp clear English, pronounces ORANGE clearly as orange not ornage, natural inflection] (0-15s, continuous, no pauses, starts at frame 1): "[HOOK]. [FEATURE LINE]. [FEATURE LINE]. Huge sale right now, click the orange cart below." Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

---

## Multi-shot vs single-shot

**Use multi-shot (3 × 5s) when:**
- Product has multiple visual features to show
- 15s of static one-angle would be boring
- Script has 3-4 distinct beats

**Use single-shot when:**
- Product is small and one frame captures it
- Setting has limited motion room
- You're aiming for a slow, considered vibe

Default to multi-shot for product UGC.

---

## When dialogue repeats in the output

If Kling generates 15s of audio that includes the same line twice:

**Cause:** Script is too short for 15s, so Kling loops to fill the duration.

**Fix:** Stretch script to ~42 words minimum. Include 3 distinct beats. Add a "genuinely obsessed" or "I'm telling you" filler if running short.

---

## When audio starts late

If the first 1-2 seconds of the video are silent:

**Cause:** Kling adds a default lead-in for breath/setup.

**Fix:** Ensure the speaker tag includes `(0-15s, continuous, no pauses, starts at frame 1)`. The "starts at frame 1" instruction matters.
