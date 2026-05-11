# 02.02 — Realism Tokens

The specific words and phrases that move generated images from "AI-looking" to "indistinguishable from a real iPhone photo."

These tokens were derived from comparing a real iPhone photo (provided by Isaac, IMG_8650) against multiple AI-generated attempts. The differences in the real photo became the additions to the prompt vocabulary.

---

## The hand block — enhanced realism version

Standard hand block:
```
Light olive skin with visible pores, a small scar on the second knuckle, a faint vein on the back of the hand, short clean nails, no rings.
```

Enhanced realism hand block (use when high realism is required):
```
Light olive skin with visible pores, visible dark arm hair, a small scar on the second knuckle, a faint vein on the back of the hand, short clean nails, a silver signet ring on the pinky finger, a thin gold bead bracelet on the wrist, slight motion blur on the fingertips, natural finger shadows cast on the surface beneath the hand.
```

**Why each addition matters:**

| Token | Why it works |
|---|---|
| `visible dark arm hair` | AI defaults to clean smooth skin; real arms have hair |
| `silver signet ring on pinky` | Real people wear unique jewelry, AI hands are bare |
| `thin gold bead bracelet on wrist` | Same reason |
| `slight motion blur on fingertips` | Phone photos catch hands mid-motion; AI freezes them |
| `natural finger shadows cast on surface beneath` | AI floats hands above surfaces without shadows |

---

## The "real iPhone" tells

These are the specific visual cues that mark a photo as real-phone rather than AI:

1. **Directional sunlight harshness** (when outdoors) — not even soft studio light
2. **Slight image grain** in shadows — phone sensor noise
3. **Natural depth of field** — phone camera bokeh, not artificial blur
4. **Slightly tilted horizon** — handheld 3-5 degrees off
5. **Lens vignetting** at corners (subtle)
6. **Real-world imperfections in surroundings** (dead leaves, scuffed floor, browning plant tips)
7. **Off-center subject placement** — phones aren't perfectly composed

---

## Outdoor lighting upgrade

For outdoor product shots, replace the standard lighting line with:

```
Lighting is bright direct midday sunlight from one side, casting hard-edged shadows under the [product] and on the fingers, with the opposite side slightly underexposed.
```

This kills the "every-day-is-golden-hour" AI default.

---

## Background prop language

Generic AI background:
- "a small green plant"

Real-phone background:
- "a small green plant with a few browning lower leaves"

Generic AI background:
- "a wooden fence in the distance"

Real-phone background:
- "a weathered wooden fence with visible grain and one slightly broken slat"

The addition of one specific imperfection per background item kicks the entire shot into "real" territory.

---

## Surface detail language

Generic AI surface:
- "polished hardwood floor"

Real-phone surface:
- "polished hardwood floor with a few faint scuffs near the corner and a small water ring"

Add **one imperfection per surface** mentioned.

---

## Optional add-ons for max realism

Add to the end of the human block, before the closer:

```
The image has slight phone-camera characteristics: subtle grain in the shadows, slightly off-axis tilt of about three degrees, natural unedited color cast.
```

This is a one-line vibe override that consistently improves realism.

---

## Banned realism vocabulary

Never use these — they cause the opposite effect:

- "hyperrealistic"
- "photorealistic" (already implied by Nano Banana)
- "ultra detailed"
- "8k"
- "high definition"
- "raw photo"
- "DSLR"
- "Canon EOS"
- "shot on iPhone 15 Pro"
- "natural lighting" (too generic — be specific)

Saying "raw" or "DSLR" pushes the model toward magazine-quality polish, not amateur phone photo.

---

## A/B test before committing

When trying a new realism token, generate two versions of the same product:
1. With the new token added
2. Without it

Compare side by side. Keep what improves realism, drop what doesn't.
