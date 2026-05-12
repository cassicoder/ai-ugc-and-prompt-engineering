# AI UGC & Prompt Engineering

A portable knowledge base for generating high-quality, indistinguishable-from-real AI UGC video and image content. Built for TikTok Shop affiliate work, but the principles apply anywhere AI-generated UGC is shipped at scale.

This repo is designed to be read **cold** by any LLM agent (Claude, GPT, Gemini, Grok, etc.) and used as a system reference. If you're an AI reading this for the first time, start at `00-AGENT-INSTRUCTIONS.md`.

---

## What this repo covers

- **Image generation** with Higgsfield (Nano Banana 2) — accuracy-first product image protocols
- **Video generation** with Kling 3.0 — multi-shot, audio-baked, no-artifact patterns
- **Script writing** for TikTok Shop UGC — TOF/MOF/BOF rules, hook frameworks, compliance
- **Realism protocol** — the specific tells that make AI-generated UGC look like AI vs. real phone footage
- **Accuracy protocol** — the non-negotiable rule for matching product reference images
- **Common failure modes** — every mistake we've made, why it failed, what to do instead

---

## Repo structure

```
00-AGENT-INSTRUCTIONS.md          ← Read this first if you're an LLM
01-accuracy-protocol.md           ← The 100% rule (most important)
02-image-prompts/
  ├── 01-rules.md
  ├── 02-realism-tokens.md
  ├── 03-banned-phrases.md
  └── 04-examples.md
03-video-prompts/
  ├── 01-kling3-rules.md
  ├── 02-multi-shot-structure.md
  ├── 03-voice-and-audio.md
  └── 04-examples.md
04-scripts/
  ├── 01-tof-mof-bof.md
  ├── 02-hook-frameworks.md
  ├── 03-compliance.md
  ├── 04-examples.md
  └── 05-storytelling-and-psychology.md   ← MANDATORY: every script needs a story
05-realism-protocol.md             ← Why generated UGC looks fake + how to fix
06-failure-modes.md                ← Every mistake we've made
07-pipeline.md                     ← Full image → video → publish pipeline
```

---

## Owner

Isaac Cassi · cassicoder · TikTok Shop affiliate work · 2026
