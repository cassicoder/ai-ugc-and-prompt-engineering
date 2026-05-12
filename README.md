# AI UGC & Prompt Engineering

Knowledge base for producing AI-generated UGC videos for TikTok Shop affiliate. The bar is **indistinguishable from a real iPhone video**.

If you are an AI agent picking this up, the entire repo fits in 5 files. Read them in order.

## The 5 files

1. **[`workflows/image-accuracy-v1.md`](workflows/image-accuracy-v1.md)** — the 3-step workflow that makes generated product images match the reference 100%. Read first. Built after empirical testing on a 21-product batch.
2. **[`image-prompts.md`](image-prompts.md)** — the locked template for Nano Banana image prompts. Skeleton, realism tokens, banned phrases, fully-worked examples.
3. **[`video-prompts.md`](video-prompts.md)** — the locked template for Kling 3.0 video prompts. Multi-shot structure, voice persona, audio rules, examples.
4. **[`scripts.md`](scripts.md)** — TikTok Shop scripting: TOF / MOF / BOF, hook frameworks, storytelling + consumer psychology, compliance.
5. **[`failure-modes.md`](failure-modes.md)** — every mistake already lived through. Read before assuming a thing will work.

## The two non-negotiable rules

1. **100% product accuracy.** The product in the generated image must match the reference image exactly in color, silhouette, texture, and visible features. If you can't verify a feature, leave it out. See `workflows/image-accuracy-v1.md` for the workflow that produces this.
2. **Wait for explicit approval before firing a generation.** Propose the prompt + settings, wait for "fire," only then call the generation tool. The user controls the spend.

## The pipeline

```
1. Pick product (user-driven, never agent-pick unless asked)
2. View reference image directly
3. Build spec card + ambiguity audit (workflows/image-accuracy-v1.md)
4. Write image prompt from template (image-prompts.md)
5. Get approval → fire → verify against reference
6. Write video prompt (video-prompts.md)
7. Get approval → fire → verify
8. Write on-screen text + caption (scripts.md)
9. Compliance check (scripts.md § Compliance)
10. Ship
```

## The voice

```
Young American male mid-twenties, warm expressive gay-best-friend voice, animated and excited like he's telling his girl about a find, light theatrical lilt, crisp clear English, natural inflection, not flat, not robotic, not salesy.
```

Locked. Do not deviate.

## The closer (locked, every image and video prompt ends with this)

```
Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

## Archive

The previous 12-file structure lives in `_archive/`. Same content, more redundancy. Keep for reference; don't read for working.
