#!/usr/bin/env python3
"""
verify_compare.py — Build side-by-side comparison images for post-fire verification.

The Step 4 verification in `workflows/image-accuracy-v1.md` requires comparing each
generated image against its reference. This script automates the layout so the
comparison fits on one screen and the eye can scan color, silhouette, texture, and
features quickly.

Usage:
    python verify_compare.py --ref refs/product.png --gen generated/product.png --out compare/product.png
    python verify_compare.py --pairs pairs.json --out_dir compare/

pairs.json format:
    [
      {"name": "01_SANSI", "ref": "refs/01.png", "gen": "generated/01.png"},
      {"name": "02_AMERLIFE", "ref": "refs/02.png", "gen": "generated/02.png"}
    ]

Outputs are PNG, ref on the left, generated on the right, both fit to the same
height with a 40px white gap between them. Final width is capped at 1500px so it
fits in a standard view tool without aggressive downscaling.

Requires: Pillow (pip install Pillow).
"""

import argparse
import json
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("ERROR: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)


TARGET_HEIGHT = 1200
GAP_PX = 40
MAX_WIDTH = 1500
# The product photo in a TikTok Shop iPhone screenshot lives roughly between
# y=180 and y=1320 on a 2556px-tall screenshot. Crop to that region before
# fitting, so the comparison ignores the iOS status bar and the listing text.
TIKTOK_CROP_TOP = 180
TIKTOK_CROP_BOTTOM = 1320


def fit_height(img: Image.Image, h: int) -> Image.Image:
    ratio = h / img.height
    return img.resize((int(img.width * ratio), h), Image.LANCZOS)


def crop_tiktok_product(img: Image.Image) -> Image.Image:
    """If the image looks like a full-screen iPhone screenshot, crop to product area."""
    if img.height >= 2400 and img.width <= 1300:
        return img.crop((0, TIKTOK_CROP_TOP, img.width, TIKTOK_CROP_BOTTOM))
    return img


def build_comparison(ref_path: str, gen_path: str, out_path: str) -> None:
    ref = Image.open(ref_path).convert("RGB")
    gen = Image.open(gen_path).convert("RGB")

    ref = crop_tiktok_product(ref)

    ref_r = fit_height(ref, TARGET_HEIGHT)
    gen_r = fit_height(gen, TARGET_HEIGHT)

    canvas = Image.new(
        "RGB",
        (ref_r.width + GAP_PX + gen_r.width, TARGET_HEIGHT),
        (255, 255, 255),
    )
    canvas.paste(ref_r, (0, 0))
    canvas.paste(gen_r, (ref_r.width + GAP_PX, 0))

    if canvas.width > MAX_WIDTH:
        new_h = int(canvas.height * MAX_WIDTH / canvas.width)
        canvas = canvas.resize((MAX_WIDTH, new_h), Image.LANCZOS)

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    canvas.save(out_path, "PNG", optimize=True)
    print(f"  wrote {out_path} ({canvas.size[0]}x{canvas.size[1]})")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", help="Path to reference image")
    parser.add_argument("--gen", help="Path to generated image")
    parser.add_argument("--out", help="Output path for the comparison PNG")
    parser.add_argument("--pairs", help="Path to JSON file describing multiple pairs")
    parser.add_argument(
        "--out_dir",
        help="Output directory when using --pairs (defaults to ./compare)",
        default="./compare",
    )
    args = parser.parse_args()

    if args.pairs:
        with open(args.pairs) as f:
            pairs = json.load(f)
        print(f"Building {len(pairs)} comparisons into {args.out_dir}/")
        for p in pairs:
            out = os.path.join(args.out_dir, f"{p['name']}.png")
            build_comparison(p["ref"], p["gen"], out)
    elif args.ref and args.gen and args.out:
        print("Building comparison")
        build_comparison(args.ref, args.gen, args.out)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
