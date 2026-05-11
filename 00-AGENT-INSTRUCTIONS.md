# 00 — Agent Instructions (Read First)

If you are an AI agent (Claude, GPT, Gemini, etc.) and you've been given this repo as a reference, this file is your entry point. Read it before doing anything else.

---

## What you are doing

You are producing AI-generated UGC (User-Generated Content) videos for TikTok Shop affiliate work. The end product is a 15-second vertical TikTok video that looks like a real person holding their phone and recommending a product to a friend.

The bar is **indistinguishable from a real iPhone video**. Not "looks like AI tried hard." Real.

---

## The two non-negotiable rules

### Rule 1 — 100% accuracy on the product

The product in your generated image/video must match the reference image **exactly** in:
- Color (don't say "white" if it's cream; don't say "beige" if it's grey)
- Shape and proportions
- Branding and text
- Visible features (drawer count, knob style, leg style, material finish)

If you are not 100% sure of a feature, **do not claim it.** Not 99%. Not "probably." If the reference image doesn't clearly show it and the listing title doesn't clearly state it, leave it out.

If you need more reference angles, ask. Do not improvise.

### Rule 2 — Wait for explicit instruction before generating

Never auto-generate images, videos, scripts, or pick products on your own. Always:
1. Propose the plan in detail (model, prompt, settings, product specs)
2. Wait for explicit approval
3. Only then call the generation tool

The user controls the spend. You propose, they approve.

---

## The pipeline

```
1. Pick product (user-driven, never agent-pick unless asked)
2. View product reference image directly (not just title text)
3. Write image prompt — follow 02-image-prompts/01-rules.md
4. Get approval
5. Generate image with Higgsfield Nano Banana 2 (4k, 9:16, ref attached)
6. Review with user
7. Write video prompt — follow 03-video-prompts/01-kling3-rules.md
8. Get approval
9. Generate video with Kling 3.0 (std mode, 15s, sound on, image as start frame)
10. Review with user
11. Generate on-screen text + caption — follow 04-scripts/04-examples.md
12. Compliance check — 04-scripts/03-compliance.md
13. Ship
```

---

## How to read this repo

- **`01-accuracy-protocol.md`** — read this entirely, twice
- **`05-realism-protocol.md`** — the difference between "AI-looking" and "real-looking" UGC
- **`06-failure-modes.md`** — every failure we've already lived through; don't repeat them
- Subfolder files — reference when actively writing prompts

---

## Anti-patterns to never repeat

1. Generating a product image without viewing the reference image first
2. Claiming features in the script that aren't 100% verified visible
3. Using third-person camera angles when the user asked for first-person POV
4. Using banned phrases in Kling prompts (see `03-video-prompts/01-kling3-rules.md`)
5. Picking which products to generate without explicit user approval
6. "Selfie capture" framing when actual first-person POV is required
7. Writing scripts with medical/health/legal claims
8. Repeating dialogue in a 15s video (cause: script too short for the duration)
9. Showing a second person in frame when faceless POV is required
10. Forgetting to spell ORANGE phonetically in voice cue (Kling will mispronounce it)

---

## The voice

When generating Kling audio for the creator character:

> Young American male, mid-twenties, warm expressive gay-best-friend voice, light theatrical lilt, animated and excited like he's telling his girl about a find, crisp clear English, natural inflection, not flat, not robotic, not salesy. Pronounces ORANGE clearly as orange.

This is the locked voice persona. Do not deviate unless instructed.

---

## The closer

Every image prompt ends with this exact sentence:

> Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.

Every video prompt ends with the same closer.
