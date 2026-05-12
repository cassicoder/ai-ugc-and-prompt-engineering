# 03.04 — Video Prompt Examples

Worked examples — successful patterns and failure modes.

---

## Example 1 — Yaheetech Adirondack Folding Chair (worked)

```
First-person POV, vertical 9:16, the camera is the creator's eyes on a sunlit backyard patio. A man's right arm extends forward from the bottom-right of the frame, hand resting on the wide armrest of an Adirondack folding chair. Bare forearm, white short-sleeve t-shirt edge at the shoulder. Setting: worn patio, beige doormat, terracotta pot, iced tea glass. Multi-shot enabled. Shot 1 (0-5s): wide on the chair, hand taps the armrest twice, ending hand flat on the armrest. Shot 2 (5-10s): close on the wood grain of the seat slats, hand sliding along the curved back, ending fingers on the top slat. Shot 3 (10-15s): pull back wide, hand back on the armrest, ending at start framing. As the hand moves, the late afternoon light shifts across the wood grain. Audio: [Speaker: young American male mid-twenties, warm expressive gay-best-friend voice, animated and excited like he's telling his girl about a find, light theatrical lilt, crisp clear English, pronounces ORANGE clearly as orange not ornage, natural inflection, not flat, not salesy] (0-15s, continuous, no pauses, starts at frame 1): "Okay STOP — y'all need to see this chair right now. It folds, it's real acacia wood, and it holds like four hundred pounds. I've been looking for one for my patio for months and finally found it. Huge sale right now, click the orange cart below before they sell out." Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

**Why it worked:**
- 3 shots with explicit timing and endpoints
- Voice tag has all 9 anchor tokens
- Dialogue ~42 words (right length for 15s)
- Hook lands at frame 1 with "Okay STOP"
- ORANGE spelled phonetically
- Realism phrase included
- Locked closer

---

## Example 2 — Curvy Moon Teeth Cleaner v1 (FAILED on compliance)

**Original script (wrong):**
> "I've been embarrassed about my teeth for years. Tartar buildup that flossing wouldn't touch. Got this little teeth cleaner thing — five modes, LED light, waterproof. Took off stuff my dentist couldn't even get. Link's in the bio."

**Two problems:**
1. ❌ "Tartar buildup that flossing wouldn't touch" — dental efficacy claim
2. ❌ "Took off stuff my dentist couldn't even get" — disparages a healthcare professional, implicit medical efficacy claim
3. ❌ "Link's in the bio" — should be "click the orange cart below"

**Compliant rewrite:**

> "I cannot stop using this little thing on my teeth. Five modes, LED light, totally waterproof, USB-C charging. It's just nice to have something that makes my teeth feel cleaner. Huge sale right now, click the orange cart below."

**Changes:**
- Removed medical efficacy claims
- Replaced with subjective sensory language ("makes my teeth feel cleaner") — opinion-based, allowed
- Fixed CTA

---

## Example 3 — Mirror video v1 (FAILED — hand disappeared)

**Original prompt:**
```
... Static iPhone POV shot of the arched full-length floor mirror. ABSOLUTELY NO person, NO hand, NO body part in the frame. Voiceover only. [dialogue] ...
```

**What went wrong:**
The start_image was a mirror without a hand (correct for "no person"), but Kling hallucinated a hand briefly around frame 30, then dropped it — looks glitchy.

**Lesson:**
If you want NO person at all, the prompt must include `humans: none, zero people, zero hands` AND the start image must clearly have NO person. If the start image's framing is ambiguous, Kling fills in.

**Fix:**
For "no person" videos, use a tighter framing on the product where there's no room for a hand to plausibly appear.

---

## Example 4 — Palm tree video v1 (FAILED — product grew)

**Original prompt:**
```
... Camera tilts up to capture the full height of the palm tree fronds at the top, capturing the eight-foot height ...
```

**What went wrong:**
Kling interpreted "tilt up to capture full height" as "scale the tree up so it fills the frame." The palm tree visibly grew on screen.

**Lesson:**
Camera moves must include endpoints. The phrase "to capture" is ambiguous to Kling — it can mean "until the subject fills the frame," which means scaling.

**Fix:**
```
Camera slow tilt up the trunk of the palm tree from the planter base to the top fronds, ending framed on the top fronds. The palm tree stays the same size and position throughout, only the camera moves.
```

The explicit "tree stays the same size" instruction blocks the scaling interpretation.

---

## Example 5 — Fireplace TV Stand video v1 (FAILED — repeated dialogue)

**Original script (32 words):**
> "Yo whoever priced this fireplace TV stand needs a raise. Real wood top, sixteen LED color options underneath, fireplace insert that actually heats. Huge sale right now. Link's in the bio."

**Output:** Kling spoke the script in ~10 seconds, then looped "Real wood top, sixteen LED color options" again to fill the remaining 5 seconds.

**Lesson:**
At 32 words, Kling has 5 seconds of extra duration to fill → repeats lines.

**Fix:**
Stretch to ~42 words:

> "Yo whoever priced this fireplace TV stand needs a raise. Real wood top, sixteen LED color options underneath, fireplace insert that actually heats up the whole room. Genuinely obsessed. Huge sale right now, click the orange cart below if you want it."

42 words = ~14.5 seconds spoken at natural pace = no room to repeat.

---

## Example 6 — Office Chair video (worked once features were accurate)

```
First-person POV, vertical 9:16, the camera is the creator's eyes looking slightly down at a big and tall executive office chair in a modern home office. A man's right arm extends forward from the bottom-right, hand resting palm-down on the wide padded armrest of the chair. [arm clothing]. Setting: wood desk, closed laptop, small plant, mug, cream wall. Multi-shot enabled. Shot 1 (0-5s): wide on the full chair, hand on the armrest, ending fingers pressing into the cream bouclé padding once. Shot 2 (5-10s): close on the flip-armrest mechanism and footrest extending from under the seat, hand sliding to flip the armrest down, ending armrest flat. Shot 3 (10-15s): pull back wide, hand back on the armrest at start position, ending at start framing. As the hand moves, the warm room light shifts across the bouclé fabric. Audio: [Speaker: ...]. ...
```

**Why it worked:**
- Specific feature interactions in each shot
- Material name ("cream bouclé") locks the chair color/texture
- "Light shifts across the bouclé fabric" — material-specific realism phrase

---

## The pattern checker (use before every fire)

Before submitting a Kling prompt, run this mental check:

1. Is every claim in the dialogue accurate to the product? → `01-accuracy-protocol.md`
2. Is the dialogue 35-45 words? → if short, will loop; if long, gets cut
3. Are there 3 numbered shots with timing? → multi-shot rule
4. Does every camera move have an endpoint? → endpoint rule
5. Does every hand action have an endpoint? → endpoint rule
6. Is the realism phrase present? → "As the hand moves, the light shifts across the [surface]"
7. Is the speaker tag complete with all 9 anchor tokens? → voice rule
8. Is the timing tag `(0-15s, continuous, no pauses, starts at frame 1)`? → frame-1 rule
9. Is ORANGE spelled `orange`? → pronunciation rule
10. Is the closer present? → "Real person, real room, real phone — ..."

If any answer is no, fix before firing.
