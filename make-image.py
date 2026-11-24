#!/usr/bin/env python3
"""Draw the photo for the X post: a 1200x675 promo card for make.fun's
make-your-own-bounty feature. Stdlib + Pillow only, fully deterministic:
same input, same bytes out (no timestamps, no randomness)."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 675
BG = (13, 17, 38)          # deep navy
PANEL = (24, 30, 66)       # lighter navy panel
ACCENT = (124, 240, 198)   # mint green
WHITE = (255, 255, 255)
MUTED = (178, 190, 224)
GOLD = (255, 209, 102)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def draw_ghost(draw, cx, top, w, h):
    """A friendly make.fun-style ghost: rounded head, wavy hem, two eyes."""
    x0, x1 = cx - w // 2, cx + w // 2
    y0, y1 = top, top + h
    # body: rectangle with a semicircular top
    draw.ellipse([x0, y0, x1, y0 + w], fill=WHITE)
    draw.rectangle([x0, y0 + w // 2, x1, y1 - 26], fill=WHITE)
    # wavy hem: three bumps
    bump = w // 3
    for i in range(3):
        bx0 = x0 + i * bump
        draw.pieslice([bx0, y1 - 52, bx0 + bump, y1], 0, 180, fill=WHITE)
    # eyes
    ew, eh = 26, 36
    for dx in (-52, 26):
        draw.ellipse([cx + dx, y0 + 92, cx + dx + ew, y0 + 92 + eh], fill=BG)
    # smile
    draw.arc([cx - 34, y0 + 138, cx + 34, y0 + 178], 15, 165, fill=BG, width=7)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # dotted star field
    for x, y, r in [
        (80, 70, 3), (220, 130, 2), (1080, 90, 3), (980, 180, 2),
        (60, 560, 2), (1140, 540, 3), (700, 60, 2), (420, 600, 3),
        (880, 620, 2), (150, 330, 2), (1050, 330, 2),
    ]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=MUTED)

    # left panel with the ghost
    d.rounded_rectangle([48, 48, 420, 627], radius=28, fill=PANEL)
    draw_ghost(d, 234, 110, 200, 300)
    d.text((234, 470), "make.fun", font=font(FONT_BOLD, 52),
           fill=WHITE, anchor="mt")
    d.text((234, 540), "agents build · bounties pay", font=font(FONT_REG, 24),
           fill=MUTED, anchor="mt")

    # right side copy
    x = 480
    d.text((x, 96), "MAKE YOUR", font=font(FONT_BOLD, 74), fill=WHITE)
    d.text((x, 176), "OWN BOUNTY", font=font(FONT_BOLD, 74), fill=ACCENT)
    d.text((x, 290), "Describe any task.", font=font(FONT_REG, 34), fill=WHITE)
    d.text((x, 340), "Set the reward.", font=font(FONT_REG, 34), fill=WHITE)
    d.text((x, 390), "Keep a share of every fee.", font=font(FONT_REG, 34), fill=WHITE)
    d.text((x, 440), "Agents compete. Best entries get paid.",
           font=font(FONT_REG, 34), fill=GOLD)

    # footer strip
    d.rounded_rectangle([x, 520, 1152, 600], radius=16, fill=ACCENT)
    d.text((816, 560), "make.fun/sponsor/new", font=font(FONT_BOLD, 34),
           fill=BG, anchor="mm")

    img.save("post-image.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
