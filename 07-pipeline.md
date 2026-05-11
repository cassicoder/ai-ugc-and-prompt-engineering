# 07 — Full Pipeline

End-to-end workflow from product idea to published TikTok video.

---

## The 11-step pipeline

```
1. Product selection           ← User-driven, never agent-pick without approval
2. Reference image acquisition ← Pull from Google Drive Product folder
3. Reference image VIEWING     ← Look at it with view tool, list specs
4. Image prompt writing        ← Follow 02-image-prompts/01-rules.md
5. Approval                    ← Propose, wait for explicit go
6. Image generation            ← Higgsfield Nano Banana 2, 4k, 9:16
7. Image review                ← User selects keepers, requests re-rolls if needed
8. Video prompt writing        ← Follow 03-video-prompts/01-kling3-rules.md
9. Approval                    ← Propose, wait for explicit go
10. Video generation           ← Kling 3.0, std, 9:16, 15s, sound on
11. Compliance + assets        ← Check + provide on-screen text + caption
```

---

## Step 1 — Product selection

User picks the product. If user says "do the next 5" or "your pick," I propose specific products by name and wait for explicit approval.

Always confirm:
- Product name
- Category
- TOF/MOF/BOF target
- Avatar mode (full face / faceless POV / no person)

---

## Step 2 — Reference image acquisition

Pull the product image from the user's Drive Product folder (`1r8U_AikSHw4VaD0zEEc9idzpeYGL3Enu` for Isaac).

If the user provides a new image directly in chat, save it.

Never generate from text alone.

---

## Step 3 — Reference image VIEWING

**This is the most-skipped, most-critical step.**

Use the `view` tool to actually look at the image. Note:

- Exact color (specific shade)
- Material finish
- Specific features visible
- Counts (drawers, wheels, panels)
- Branding location
- Anything attached/included

If the image is unclear or the user might have additional angles, ask before proceeding.

---

## Step 4 — Image prompt writing

Follow the template in `02-image-prompts/01-rules.md`:

```
[FORMAT]. [POV/FRAMING]. [HUMAN BLOCK]. The [PRODUCT] matches the attached reference image exactly: [PRODUCT SPEC BLOCK]. Setting: [3 NAMED CLUTTER ITEMS]. Lighting is flat and slightly uneven, [LIGHT SOURCE]. [AUTHENTICITY CLOSER].
```

Run the accuracy checklist:
- Each spec claim verified V (visible) or T (in title)
- No banned phrases
- 130-180 words single paragraph

---

## Step 5 — Approval

Show the prompt + settings to the user:

```
Settings:
- Model: nano_banana_2
- Resolution: 4k
- Aspect ratio: 9:16
- Count: 1
- Reference: [product name]

Prompt:
[full prompt text]
```

Wait for "go" or equivalent before firing.

---

## Step 6 — Image generation

```
Higgsfield:generate_image
  model: nano_banana_2
  aspect_ratio: 9:16
  resolution: 4k
  count: 1
  medias: [{role: "image", value: "<product ref UUID>"}]
  prompt: [full prompt]
```

Note the job ID for tracking.

---

## Step 7 — Image review

User reviews the generated image. Three outcomes:

- **Keeper** → proceed to video step
- **Re-roll same prompt** → fire again with same prompt (different seed)
- **Re-roll different prompt** → diagnose what went wrong, rewrite prompt, re-fire

Common re-roll triggers:
- Wrong color/style for product
- Hand looks AI-clean (apply enhanced realism)
- Setting too studio-polished (more lived-in clutter)
- POV angle is wrong (true first-person vs observer)

---

## Step 8 — Video prompt writing

Follow `03-video-prompts/01-kling3-rules.md`:

```
[FORMAT]. [HUMAN BLOCK]. Setting: [items]. Multi-shot enabled. Shot 1 (0-5s): [camera + action + endpoint]. Shot 2 (5-10s): [...]. Shot 3 (10-15s): [...]. As the hand moves, the [light source] shifts across the [surface]. Audio: [Speaker: ...] (0-15s, continuous, no pauses, starts at frame 1): "[~42 word script]". [CLOSER].
```

Script accuracy check:
- Every claim verified
- No medical/health language
- No competitor brand names
- CTA = "click the OR-anj cart below"
- ~42 words

---

## Step 9 — Approval

Show video prompt + settings:

```
Settings:
- Model: kling3_0
- Mode: std
- Aspect ratio: 9:16
- Duration: 15s
- Sound: on
- Start frame: [image job ID]

Prompt:
[full prompt text]

Script:
"[dialogue]"
```

Wait for "go."

---

## Step 10 — Video generation

```
Higgsfield:generate_video
  model: kling3_0
  mode: std
  aspect_ratio: 9:16
  duration: 15
  sound: on
  medias: [{role: "start_image", value: "<image UUID>"}]
  prompt: [full prompt]
```

Note the job ID. Wait for completion (~2-4 min for std mode).

---

## Step 11 — Compliance + assets

Once video is approved:

1. Compliance check (full audit per `04-scripts/03-compliance.md`)
2. Provide on-screen text overlay (6-8 words + emoji)
3. Provide caption (1-2 lines + emoji)
4. Confirm AI label toggle on upload

Done. Ship.

---

## Batch workflow (5 products at once)

For batch processing:

1. List 5 product names → user approval
2. Pull all 5 refs from Drive in parallel
3. View each ref → note specs
4. Write all 5 image prompts
5. Show all 5 prompts → user approval
6. Upload all 5 refs to Higgsfield
7. Confirm uploads
8. Fire all 5 image generations in parallel
9. User reviews → flags re-rolls
10. Write video prompts for keepers
11. Show video prompts → user approval
12. Fire video generations
13. Compliance + assets for all

Batch is efficient but requires very disciplined approval gates. The opportunity cost of skipping a check at the batch level is 5x higher.

---

## Daily output target

For Isaac's TikTok Shop workflow:
- 1 new product video per day (sustainable)
- 5 product videos per week (aggressive)
- 22 days of content per batch of 22 products

Don't post 2 furniture videos back-to-back. Rotate categories to prevent the FYP from typing the account as single-niche.

---

## Failure recovery

If a generation fails or produces an unusable output:

1. Diagnose root cause (which doc does it map to?)
2. Update the relevant `04-examples.md` with the failure
3. Update `06-failure-modes.md` with the lesson
4. Re-fire with the fix

If the same failure happens 3 times in a session, **stop and audit the system prompt** — there's a deeper pattern issue.

---

## Cost management

Approximate credit cost per asset:

| Asset | Model | Cost |
|---|---|---|
| Image (1) | Nano Banana 2, 4k | ~4 credits |
| Video (15s std) | Kling 3.0 std | ~50 credits |
| Image+Video pair | (combined) | ~54 credits |

For 5 products end-to-end: ~270 credits.

Always check balance before a batch. Top up if low.

---

## Tool reference

Required Higgsfield tools:
- `media_upload` — get presigned URLs
- `media_confirm` — confirm S3 upload
- `generate_image` — Nano Banana 2
- `generate_video` — Kling 3.0
- `models_explore` — verify model params
- `balance` — credit check
- `show_generations` — review past outputs

Required for asset retrieval:
- `Google_Drive:search_files` — find product refs
- `Google_Drive:download_file_content` — pull reference image

Required for repo management:
- `git` commands via bash — read vault skills, push updates to this repo

---

## Repo update protocol

When new learnings emerge:

1. Identify which doc in this repo needs updating
2. Make the edit
3. Commit with a descriptive message
4. Push to `cassicoder/ai-ugc-and-prompt-engineering`

This repo is meant to be living. Failures get added to `06-failure-modes.md`. New realism tokens get added to `05-realism-protocol.md`. Hook patterns get added to `04-scripts/02-hook-frameworks.md`.
