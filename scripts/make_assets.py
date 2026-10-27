#!/usr/bin/env python3
"""Generate the GitHub profile avatar and banner from the lightning artwork."""

from pathlib import Path
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
AVATAR_SRC = ROOT / "avatar-lightning.png"
AVATAR_ROUND = ROOT / "avatar.png"
BANNER = ROOT / "banner.png"


def load_font(candidates: list[str], size: int) -> ImageFont.FreeTypeFont:
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def make_round_avatar() -> Image.Image:
    avatar = Image.open(AVATAR_SRC).convert("RGBA")
    mask = Image.new("L", avatar.size, 0)
    ImageDraw.Draw(mask).ellipse([0, 0, avatar.width - 1, avatar.height - 1], fill=255)
    avatar.putalpha(mask)
    avatar.save(AVATAR_ROUND, optimize=True)
    return avatar


def make_banner(avatar: Image.Image) -> None:
    width, height = 1280, 420
    scale = 2
    w, h = width * scale, height * scale
    img = Image.new("RGB", (w, h), "#060a12")
    draw = ImageDraw.Draw(img)

    top, bottom = (6, 10, 20), (12, 24, 44)
    for y in range(h):
        t = y / (h - 1)
        color = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        draw.line([(0, y), (w, y)], fill=color)

    glow = Image.new("RGB", (w, h), "black")
    glow_draw = ImageDraw.Draw(glow)
    cx, cy = int(w * 0.80), int(h * 0.50)
    for i in range(70, 0, -1):
        radius = int(w * 0.40 * i / 70)
        alpha = int(60 * (1 - i / 70) ** 1.7)
        glow_draw.ellipse(
            [cx - radius, cy - radius, cx + radius, cy + radius],
            fill=(15 + alpha, 45 + alpha, 85 + alpha),
        )
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    img = Image.blend(img, glow, 0.55)

    draw = ImageDraw.Draw(img)
    random.seed(9)
    for _ in range(90):
        x, y = random.randint(0, w - 1), random.randint(0, h - 1)
        value = random.randint(30, 80)
        radius = random.choice([1, 1, 2])
        draw.ellipse(
            [x - radius, y - radius, x + radius, y + radius],
            fill=(value, value + 12, value + 30),
        )

    draw.rectangle([70 * scale, 300 * scale, 250 * scale, 303 * scale], fill=(110, 210, 255))

    font_bold = load_font(
        ["/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
        62 * scale,
    )
    font_role = load_font(
        ["/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
        27 * scale,
    )
    font_regular = load_font(
        ["/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"],
        20 * scale,
    )
    font_site = load_font(
        ["/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"],
        17 * scale,
    )

    x0 = 70 * scale
    draw.text((x0, 92 * scale), "ДАНИИЛ СМИРНОВ", font=font_bold, fill=(245, 250, 255))
    draw.text(
        (x0, 190 * scale),
        "Fullstack QA  ·  Senior Automation QA",
        font=font_role,
        fill=(127, 220, 255),
    )
    draw.text(
        (x0, 240 * scale),
        "UI  ·  API  ·  БД  ·  CI/CD  ·  4000+ автотестов в проде",
        font=font_regular,
        fill=(160, 176, 198),
    )
    draw.text(
        (x0, 345 * scale),
        "github.com/Mirtalll",
        font=font_site,
        fill=(120, 138, 160),
    )

    size = 270 * scale
    avatar_big = avatar.resize((size, size), Image.LANCZOS)
    ax = int(w * 0.805 - size / 2)
    ay = int(h * 0.50 - size / 2)

    avatar_glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(avatar_glow).ellipse(
        [ax - 30 * scale, ay - 30 * scale, ax + size + 30 * scale, ay + size + 30 * scale],
        fill=(80, 190, 255, 120),
    )
    avatar_glow = avatar_glow.filter(ImageFilter.GaussianBlur(35 * scale))
    img = Image.alpha_composite(img.convert("RGBA"), avatar_glow).convert("RGB")

    ring = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    pad = 7 * scale
    ImageDraw.Draw(ring).ellipse(
        [ax - pad, ay - pad, ax + size + pad, ay + size + pad],
        outline=(120, 220, 255, 255),
        width=4 * scale,
    )
    ring = ring.filter(ImageFilter.GaussianBlur(1 * scale))
    img = Image.alpha_composite(img.convert("RGBA"), ring).convert("RGB")

    img.paste(avatar_big, (ax, ay), avatar_big)
    img.resize((width, height), Image.LANCZOS).save(BANNER, optimize=True)


if __name__ == "__main__":
    make_banner(make_round_avatar())
    print(f"Generated {AVATAR_ROUND.name} and {BANNER.name}")
