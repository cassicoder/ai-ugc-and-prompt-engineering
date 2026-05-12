# Failure Modes

Every mistake we've already lived through. Read before assuming a thing will work.

The biggest lesson: **every failure was preventable by 30 seconds of verification before firing.** Generation costs credits and time. Prompt writing is free.

---

## Image-generation failures

### F1 — Generated without viewing the reference image

Symptom: product in generated image doesn't match the actual product.

Examples:
- Vowner Vanity → generated Hollywood bulb mirror; actual product is standalone 3-color lighted mirror
- Pukami Fireplace → generated solid oak wood; actual product is black high-gloss with wood-tone top
- Cat Litter Box → generated fully enclosed with lid; actual product is semi-enclosed open-top
- Basket Chair → generated warm tan rattan; actual product is dark grey rattan

Cause: trusted the listing title or pattern-matching instead of looking at the image.

Fix: **mandatory** — call `view` on the reference before writing any product prompt. Note exact color, shape, knob style, leg style, drawer count, branding location.

### F2 — Ambiguous spec word (the v1 batch failure mode)

Symptom: model picks the wrong visual interpretation of an ambiguous word.

Examples:
- "tufted" → button tufts instead of channel tufts (XKHOMESHOP folding sofa v1)
- "chenille" → bumpy boucle instead of smooth flat (Weture U-sofa v1)
- "double egg chair" → single egg instead of double-wide (RIWENGO v1)
- "yellow outer ring tube, teal top edge stripe" → teal on top instead of yellow on top (AMERLIFE v1)

Cause: model defaulted to most common training-data interpretation.

Fix: see `workflows/image-accuracy-v1.md` § Step 2. Every adjective gets an ambiguity audit. If a word could go two ways, rewrite as `X — NOT Y, NOT Z`.

### F3 — Made up features that aren't on the product

Symptom: generated image has features that don't exist on the real product.

Examples:
- Vowner Vanity: invented a cushioned bench (not in listing)
- Pukami Fireplace: described cyan LED accent strip specifically (16 colors, cyan was one sample)
- Cat Litter Box: described oval entry hole on lid (no lid)

Cause: adding details from intuition or pattern-matching.

Fix: hard rule — only include features that are (a) visible in the reference image OR (b) explicitly named in the listing title. Mark each feature internally: V (visible in image) / T (in title) / A (assumed). Drop everything A.

### F4 — Picked products user didn't approve

Symptom: generated for products the user never asked for.

Example: user said "do next 5 products" without naming them; I auto-picked.

Fix: before any batch generation, list the exact products being proposed and wait for explicit name-level approval.

### F5 — Third-person observer angle instead of first-person POV

Symptom: camera reaching in from the side of the room — observer angle — when user wanted true first-person POV.

Cause: phrase "iPhone selfie capture" triggers "creator filming themselves" framing.

Fix: lead with `First-person POV, vertical 9:16, the camera is the creator's own eyes looking [direction] at...` and have the arm extend forward from the bottom-right, not reach in from the side.

### F6 — Top-down view when ground-level was wanted

Symptom: camera angle is overhead bird's-eye, looking down at product from above.

Cause: said "looking down at" without specifying "at adult standing height looking forward."

Fix: lead with `camera is the creator's eyes standing at adult height ... looking forward at [product] a few feet away`. The phrase "at adult height" anchors vertical position.

### F7 — Hand floating, not touching the product

Symptom: hand visible but hovering in air, not actually in contact with the product.

Cause: used soft verbs like "reaching toward" or "fingertips on" — the model interprets as "hand near."

Fix: use contact verbs: `fingers gripping`, `fingertips pressing into`, `palm in firm contact`. Specify firm contact every time.

---

## Video-generation failures

### V1 — Dialogue repeated twice in 15s video

Symptom: Kling speaks the script, then loops back to repeat the second half.

Cause: script too short; Kling fills remaining duration by repeating.

Fix: stretch script to ~42 words. Add "Genuinely obsessed" or "I'm telling you" filler if short.

### V2 — Dead air opening (first 1–2s silent)

Symptom: video starts with silence, dialogue begins around 0:01.5.

Cause: Kling adds default breath/setup lead-in.

Fix: include `(0-15s, continuous, no pauses, starts at frame 1)` in speaker tag. Start dialogue with a sharp consonant (S, P, W, K, Y).

### V3 — Product magically grew on screen

Symptom: tall product (palm tree, gazebo post) appears to scale up during the shot.

Example: Palm tree v1 — "tilt up to capture the full height" → tree grew.

Cause: camera move without explicit endpoint, model interprets "to capture full height" as "scale subject to fill frame."

Fix: explicit endpoint + `the [product] stays the same size and position throughout, only the camera moves`.

### V4 — Hand disappeared mid-video

Symptom: hand visible at start, then drops out around 2–3 seconds in.

Cause: start image didn't include a hand, but prompt described one — Kling hallucinated then dropped.

Fix: either (a) make the start image include the hand anchored to a specific product part, OR (b) prompt for true "no person in frame" with tight framing.

### V5 — Voice flat and emotionless

Symptom: dialogue sounds robotic, no enthusiasm.

Cause: speaker tag too generic ("young male voice").

Fix: use the full 9-token voice description from `video-prompts.md` § Audio. Include emotional context.

### V6 — "ORANGE" mispronounced as "ornage"

Symptom: Kling fumbles the word "orange" in the CTA.

**Wrong fix (do not repeat):** spell phonetically as `OR-anj`. Kling reads the dash literally and produces "OR-ange" with an audible robotic pause. Worse than the original.

**Correct fix:** write `orange` plainly. Reinforce in speaker tag: `pronounces ORANGE clearly as orange not ornage`. If still fumbles in output, REPLACE the word — `tap the cart below` or `click the cart icon below`. Never respell.

### V7 — Brand name mispronounced

Symptom: Kling fumbles compound brand names (HomeGoods → "HomGoods", Pinterest → "Pintrest").

Fix: don't use compound brand names in dialogue. Substitute:
- HomeGoods → "the home store"
- Pinterest → "online" or "scrolling"
- Wayfair → "the furniture site"

### V8 — Camera move erratic

Symptom: camera jerks, whips, or moves unpredictably.

Cause: banned camera move language or no endpoint.

Fix: use only safe vocabulary from `video-prompts.md` § Camera vocabulary. Every move needs an endpoint.

### V9 — Described part of product not visible in reference

Symptom: video describes or shows a feature on the back, side, top, or inside of the product that isn't visible in the reference image.

Examples:
- Office chair: script said "hidden footrest" — not visible from the front-only reference
- Bassinet: generated with canopy — main reference had no canopy attached
- Litter box: generated with lid — main reference shows open-top, no lid

Fix: only describe in dialogue and show in image what is **visible in the main reference image** provided. If a feature is in the title but not visible in any reference, ask the user for an angle showing it before claiming it visually.

---

## Script failures

### S1 — Used "link in bio" CTA

Symptom: script ends with "link in the bio" instead of "click the orange cart below."

Fix: always "click the orange cart below."

### S2 — Made medical claim accidentally

Example: Curvy Moon Teeth Cleaner v1 — "Took off stuff my dentist couldn't even get."

Fix: replace medical claims with sensory language ("makes my teeth feel cleaner"). See `scripts.md` § Compliance.

### S3 — Named a competitor brand

Fix: always generic — "the home store," "online," "the other place."

### S4 — Used dollar amounts in TOF

Symptom: TOF script says "$47" or "20% off."

Fix: TOF = no $, no %. Use "huge sale," "before it's gone."

---

## Process failures

### P1 — Auto-generated without confirmation

Fix: hard rule — propose settings + wait for approval before every fire.

### P2 — Ran the chat past optimal length

Symptom: token costs balloon, context drift increases, errors multiply.

Fix: at ~15–20 messages, flag the chat as nearing the cap. At 25+, mandatorily flag and offer a handoff summary.

### P3 — Memory full, couldn't save important rule

Fix: periodically audit memory and consolidate. Each rule unique, atomic, current.

---

## Compliance failures (the most expensive)

### C1 — Made a claim without 100% verification

Symptom: spec claim in video isn't visible or stated in listing.

Cost: CHR violation. Six strikes = permanent account removal.

Fix: see `scripts.md` § Compliance. Mandatory verification before every claim.

### C2 — Forgot to toggle AI label on upload

Fix: AI label is non-negotiable. Add to publish checklist.

---

## The meta-lesson

The pattern across every failure: **moved fast without verifying.**

Every single failure was preventable by 30 seconds of double-checking before firing.

**The rule: slow down at prompt-writing so you don't redo at generation.**

For every product:
1. Look at the reference (60s)
2. Read the listing title (30s)
3. Build spec card (60s)
4. Ambiguity audit (60s)
5. Write prompt from template (3 min)
6. Re-read the prompt (60s)
7. Get approval
8. Fire

This 7-step flow consistently produces clean output. Skipping any step causes a failure that costs more time to fix than the step would have cost upfront.
