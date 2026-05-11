# 06 — Failure Modes

Every mistake we've made and what to do instead. This is the most important learning document. Read it before starting any new project.

---

## Image generation failures

### F1 — "I generated based on the title without viewing the reference image"

**Symptom:** Product in generated image doesn't match the actual product.

**Lived examples:**
- Vowner Vanity: generated Hollywood bulb-bordered mirror; actual product has standalone 3-color lighted mirror
- Pukami Fireplace: generated solid oak wood; actual product is black high-gloss with wood-tone top
- Cat Litter Box: generated fully enclosed with lid; actual product is semi-enclosed open-top
- Office Chair: generated black tech fabric; actual product is cream bouclé
- Basket Chair: generated warm tan rattan; actual product is dark grey rattan
- Bassinet: generated grey fabric with canopy; actual product is dusty pink without canopy in main shot

**Cause:** Trusted the listing title or my own assumptions instead of looking at the image file.

**Fix:** Mandatory — call `view` on the reference image before writing any product prompt. Note exact color, shape, knob style, leg style, drawer count, branding location.

**Prevention rule:** Add to internal checklist: "Did I look at the image with my own [eyes/view tool]?"

---

### F2 — "I made up features that aren't on the product"

**Symptom:** Generated image has features that don't exist on the real product.

**Lived examples:**
- Vowner Vanity: invented a cushioned bench (not in listing)
- Pukami Fireplace: described "cyan LED accent strip" specifically (product has 16 colors, cyan was one sample)
- Cat Litter Box: described an "oval entry hole on the lid" (product has no lid)

**Cause:** Adding details from intuition or pattern-matching to similar products.

**Fix:** Hard rule — only include features that are (a) visible in the reference image OR (b) explicitly named in the listing title.

**Prevention:** Before each feature in the product spec block, mark mentally: V (visible in image) / T (in title) / A (assumed). Drop everything A.

---

### F3 — "I picked products the user didn't approve"

**Symptom:** I generated images for products the user never asked for.

**Lived example:**
- User said "do next 5 products" without naming them; I auto-picked Pukami Fireplace, Vanity, Office Chair, Basket Chair, Bassinet.

**Cause:** Filled in ambiguity by choosing rather than asking.

**Fix:** Before any batch generation, list the exact products I'm proposing and wait for explicit name-level approval.

**Prevention rule (saved to memory):** Never auto-pick products user didn't specify.

---

### F4 — "Third-person observer angle instead of first-person POV"

**Symptom:** Generated image has the camera reaching in from the side of the room — observer angle — when the user wanted true first-person POV.

**Lived examples:** First batch of 5 product images (dresser, mirror, etc.) all had third-person framing.

**Cause:** Used phrase "iPhone selfie capture" which triggers the "creator filming themselves" framing. True first-person POV means "the camera IS the creator's eyes."

**Fix:** Lead with `First-person POV, vertical 9:16, the camera is the creator's own eyes looking [direction] at...` and have the arm extend forward from the bottom-right, not reaching in from the side.

---

### F5 — "Selfie framing instead of POV framing"

**Symptom:** Arm visible reaching in from the side at chest height; product centered in frame.

**Fix:** See F4 — switch to "the camera is the creator's own eyes looking at..."

---

## Video generation failures

### V1 — "Dialogue repeated twice in a 15s video"

**Symptom:** Kling output speaks the script, then loops back to repeat the second half.

**Lived example:** Fireplace TV Stand v1 — 32-word script duplicated to fill 15s.

**Cause:** Script is too short; Kling fills remaining duration by repeating.

**Fix:** Stretch script to ~42 words. Add a "Genuinely obsessed" or "I'm telling you" filler if short.

---

### V2 — "Dead air opening (first 1-2s silent)"

**Symptom:** Video starts with silence, dialogue begins around 0:01.5.

**Cause:** Kling adds default breath/setup lead-in.

**Fix:** Include `(0-15s, continuous, no pauses, starts at frame 1)` in the speaker tag. Start dialogue with a sharp consonant (S, P, W, K, Y).

---

### V3 — "Product magically grew on screen"

**Symptom:** Tall product (palm tree, gazebo post) appears to scale up during the shot.

**Lived example:** Palm tree v1 — "tilt up to capture the full height" → tree grew.

**Cause:** Camera move without explicit endpoint, model interprets "to capture full height" as "scale subject to fill frame."

**Fix:** Add explicit endpoint and "the [product] stays the same size and position throughout, only the camera moves."

---

### V4 — "Hand disappeared mid-video"

**Symptom:** Hand visible at the start, then drops out around 2-3 seconds in.

**Lived example:** Mirror video — hand appeared briefly then vanished.

**Cause:** Start image didn't include a hand, but the prompt described one — Kling hallucinated then dropped.

**Fix:** Either (a) make the start image include the hand anchored to a specific product part, OR (b) prompt for true "no person in frame" with a tight enough framing that there's no plausible space for a hand.

---

### V5 — "Voice flat and emotionless"

**Symptom:** Dialogue sounds robotic, no enthusiasm.

**Cause:** Speaker tag too generic ("young male voice").

**Fix:** Use the full 9-token voice description from `03-video-prompts/03-voice-and-audio.md`. Include emotional context ("like he just walked into the store and found this").

---

### V6 — "ORANGE pronounced 'ornage'"

**Symptom:** Kling fumbles the word "orange" in the CTA.

**WRONG fix (do not repeat):** Spell phonetically as `orange` in the dialogue. Kling reads the dash literally and produces "OR-ange" with an audible robotic pause. This is WORSE than the original mispronunciation.

**Correct fix:** Write `orange` plainly. Reinforce with `crisp clear English with clear natural pronunciation of common words` in the speaker tag. If the word still consistently fumbles in output, REPLACE the word entirely with "cart icon below" or "tap the cart below" — never respell.

### V6.1 — "Described part of product not visible in reference"

**Symptom:** Generated video describes or shows a feature on the back, side, top, or inside of the product that isn't visible in the reference image.

**Lived examples:**
- Office chair script said "hidden footrest" — footrest mechanism not visible from the front-only reference
- Bassinet generated with canopy — main reference image had no canopy attached
- Litter box generated with lid — main reference shows open-top semi-enclosed, no lid

**Cause:** Filled in features from the listing title or from guessing what "products like this usually have."

**Fix:** Only describe in dialogue and show in image what is **visible in the main reference image** provided. If the listing title mentions a feature not visible in the image, describe it verbally in the script (it's a verifiable spec) but **do not include it in the visual image prompt**. If a feature needs to be shown but isn't visible in any reference image, **ask the user for a reference angle that shows it** before generating.

---

### V7 — "Brand name mispronounced"

**Symptom:** Kling fumbles compound brand names (HomeGoods → "HomGoods", Pinterest → "Pintrest").

**Fix:** Don't use compound brand names in dialogue. Substitute:
- HomeGoods → "the home store"
- Pinterest → "online" or "scrolling"
- Wayfair → "the furniture site"

---

### V8 — "Camera move was erratic"

**Symptom:** Camera jerks, whips, or moves unpredictably.

**Cause:** Banned camera move language (whip pan, crash zoom, 360 rotation) or no endpoint.

**Fix:** Use safe camera move vocabulary from `03-video-prompts/02-multi-shot-structure.md`. Every move needs an endpoint.

---

## Script failures

### S1 — "Used 'link in bio' CTA"

**Symptom:** Script ends with "link in the bio" instead of "click the orange cart below."

**Cause:** Default ad-style CTA habit.

**Fix:** Always "click the orange cart below" — this is the TikTok Shop in-app CTA. Saved to memory.

---

### S2 — "Made medical claim accidentally"

**Symptom:** Script implies a health/dental/medical benefit.

**Lived example:** Curvy Moon Teeth Cleaner v1 — "Took off stuff my dentist couldn't even get."

**Cause:** Reaching for impactful claims without checking compliance.

**Fix:** Compliance check — see `04-scripts/03-compliance.md`. Replace medical claims with sensory language ("makes my teeth feel cleaner").

---

### S3 — "Named a competitor brand"

**Symptom:** Script mentions HomeGoods, Costco, Wayfair, etc.

**Fix:** Always generic — "the home store," "online," "the other place."

---

### S4 — "Used real dollar amounts in TOF"

**Symptom:** Script says "$47" or "20% off."

**Cause:** Forgot the TOF rule.

**Fix:** TOF = no $, no %. Use "huge sale," "before it's gone."

---

## Process failures

### P1 — "Auto-generated without confirmation"

**Symptom:** Fired image/video generation without listing settings + getting approval.

**Cause:** Skipped the standing rule (saved to memory).

**Fix:** Hard rule — propose settings + wait for approval before every fire.

---

### P2 — "Ran the chat way past optimal length"

**Symptom:** Token costs balloon, context drift increases, errors multiply.

**Cause:** Didn't flag the chat length to the user, didn't draft a handoff summary.

**Fix:** At ~15-20 messages, flag the chat as nearing the cap. At 25+ messages, mandatorily flag and offer a handoff summary.

---

### P3 — "Memory full, couldn't save important rule"

**Symptom:** Tried to add a new memory rule, got 30/30 cap error.

**Cause:** Memory bloated with old or consolidatable rules.

**Fix:** Periodically audit memory and consolidate. Each rule should be unique, atomic, and current.

---

## Compliance failures (the most expensive)

### C1 — "Made a claim without 100% verification"

**Symptom:** Spec claim in video isn't visible or stated in the listing.

**Cause:** Skipped the accuracy protocol.

**Fix:** See `01-accuracy-protocol.md` — the 100% rule. Mandatory verification before every claim.

**Cost of failure:** CHR violation. Six strikes = permanent account removal.

---

### C2 — "Forgot to toggle AI label on upload"

**Symptom:** AI-generated content posted without the AI label.

**Cause:** Upload step missed.

**Fix:** Add to publish checklist. AI label is non-negotiable for AI content.

---

## Meta-lesson

The pattern across all these failures: **I tried to move fast without verifying.** Every single one would have been prevented by 30 seconds of double-checking before firing.

The rule: **slow down at the prompt-writing stage so you don't have to redo at the generation stage.** Generation costs credits + time. Prompt writing is free.

For every product:
1. Look at the image (60 seconds)
2. Read the listing title (30 seconds)
3. Write the prompt with verified specs (3 minutes)
4. Re-read the prompt (60 seconds)
5. Get approval (waiting)
6. Fire

This 5-step flow consistently produces clean output. Skipping any step causes a failure that costs more time to fix than the step would have cost upfront.
