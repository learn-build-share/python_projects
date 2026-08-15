"""
============================================================
    NETAJI - 80TH INDEPENDENCE DAY
    Progressive Digital Painting
    Copyright © Learn Build Share
============================================================

The program does NOT simply display an image.

It progressively paints:
    1. Paper / canvas texture
    2. Indian flag
    3. Atmospheric background
    4. Netaji portrait
    5. Military uniform
    6. Rifle/details from the reference portrait
    7. Quote
    8. Final paint highlights

Approximate painting time: 9 seconds
"""

import math
import random
import time

import cv2
import numpy as np
import pygame
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# ============================================================
# CONFIGURATION
# ============================================================

WIDTH = 1280
HEIGHT = 800

# Sidebar width for dialogues / info
SIDEBAR_WIDTH = 320

FPS = 60

PAINT_TIME = 9.0

REFERENCE_IMAGE = "bose.png"

random.seed(80)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(
    "Netaji Subhas Chandra Bose - 80th Independence Day"
)

clock = pygame.time.Clock()


# ============================================================
# COLORS
# ============================================================

PAPER = (226, 218, 198)

SAFFRON = (230, 108, 28)
SAFFRON_LIGHT = (246, 139, 45)

WHITE = (239, 235, 220)

GREEN = (35, 112, 58)
GREEN_DARK = (18, 72, 42)

NAVY = (22, 42, 54)

INK = (35, 31, 27)

GOLD = (184, 132, 48)

RED = (125, 45, 31)


# ============================================================
# HELPER
# ============================================================

def clamp(value, low, high):
    return max(low, min(high, value))


def lerp(a, b, amount):
    return a + (b - a) * amount


# ============================================================
# CREATE CANVAS
# ============================================================

canvas = Image.new(
    "RGB",
    (WIDTH, HEIGHT),
    PAPER
)

draw = ImageDraw.Draw(canvas)


# ============================================================
# PAPER TEXTURE
# ============================================================

def create_paper_texture():

    global canvas

    pixels = np.array(canvas).astype(np.int16)

    noise = np.random.normal(
        0,
        8,
        (HEIGHT, WIDTH, 1)
    )

    pixels = pixels + noise

    pixels = np.clip(
        pixels,
        0,
        255
    ).astype(np.uint8)

    canvas = Image.fromarray(pixels)

    texture = Image.new(
        "RGBA",
        (WIDTH, HEIGHT),
        (0, 0, 0, 0)
    )

    td = ImageDraw.Draw(texture)

    for _ in range(3500):

        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)

        size = random.randint(1, 3)

        alpha = random.randint(8, 25)

        td.ellipse(
            (
                x,
                y,
                x + size,
                y + size
            ),
            fill=(60, 48, 35, alpha)
        )

    canvas = Image.alpha_composite(
        canvas.convert("RGBA"),
        texture
    ).convert("RGB")


# ============================================================
# PAINT BRUSH
# ============================================================

def brush_stroke(
    image,
    start,
    end,
    color,
    width,
    opacity=180,
    roughness=0.35
):

    layer = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0)
    )

    d = ImageDraw.Draw(layer)

    x1, y1 = start
    x2, y2 = end

    dx = x2 - x1
    dy = y2 - y1

    distance = math.sqrt(
        dx * dx + dy * dy
    )

    steps = max(
        2,
        int(distance / 7)
    )

    points = []

    for i in range(steps + 1):

        t = i / steps

        x = lerp(x1, x2, t)
        y = lerp(y1, y2, t)

        # brush wobble
        offset = (
            math.sin(t * math.pi * 3)
            * width
            * roughness
        )

        length = math.sqrt(
            dx * dx + dy * dy
        ) or 1

        nx = -dy / length
        ny = dx / length

        x += nx * offset
        y += ny * offset

        points.append(
            (
                int(x),
                int(y)
            )
        )

    if len(points) >= 2:

        d.line(
            points,
            fill=(
                color[0],
                color[1],
                color[2],
                opacity
            ),
            width=max(1, int(width))
        )

    # Dry-brush fragments

    for _ in range(
        max(1, int(width / 5))
    ):

        t = random.random()

        x = int(
            lerp(x1, x2, t)
        )

        y = int(
            lerp(y1, y2, t)
        )

        r = random.randint(
            1,
            max(2, int(width / 5))
        )

        # choose an alpha value safely (opacity might be < 40)
        if opacity >= 40:
            alpha_val = random.randint(40, opacity)
        else:
            low = max(1, opacity // 2)
            alpha_val = random.randint(low, opacity)

        d.ellipse(
            (
                x - r,
                y - r,
                x + r,
                y + r
            ),
            fill=(
                color[0],
                color[1],
                color[2],
                alpha_val
            )
        )

    image.alpha_composite(layer)


# ============================================================
# FLAG
# ============================================================

def paint_flag():

    flag_x = 60
    flag_y = 90

    flag_w = 540
    stripe_h = 92

    # Pole

    draw.rectangle(
        (
            45,
            60,
            57,
            620
        ),
        fill=(74, 61, 48)
    )

    # Pole highlight

    draw.line(
        (
            49,
            65,
            49,
            615
        ),
        fill=(150, 132, 103),
        width=3
    )

    # Paint flag with hundreds of strokes

    colors = [
        SAFFRON,
        SAFFRON_LIGHT
    ]

    for _ in range(250):

        x = random.randint(
            flag_x,
            flag_x + flag_w
        )

        y = random.randint(
            flag_y,
            flag_y + stripe_h
        )

        wave = math.sin(
            x / 65
        ) * 16

        y += int(wave)

        length = random.randint(
            35,
            100
        )

        brush_stroke(
            canvas.convert("RGBA"),
            (x, y),
            (x + length, y + random.randint(-5, 5)),
            random.choice(colors),
            random.randint(8, 18),
            random.randint(80, 160)
        )


    # White stripe

    for _ in range(210):

        x = random.randint(
            flag_x,
            flag_x + flag_w
        )

        y = random.randint(
            flag_y + stripe_h,
            flag_y + stripe_h * 2
        )

        y += int(
            math.sin(x / 65) * 16
        )

        brush_stroke(
            canvas.convert("RGBA"),
            (x, y),
            (
                x + random.randint(30, 90),
                y
            ),
            (
                235,
                232,
                218
            ),
            random.randint(7, 16),
            random.randint(80, 160)
        )


    # Green stripe

    for _ in range(250):

        x = random.randint(
            flag_x,
            flag_x + flag_w
        )

        y = random.randint(
            flag_y + stripe_h * 2,
            flag_y + stripe_h * 3
        )

        y += int(
            math.sin(x / 65) * 16
        )

        brush_stroke(
            canvas.convert("RGBA"),
            (x, y),
            (
                x + random.randint(30, 100),
                y
            ),
            random.choice(
                [
                    GREEN,
                    GREEN_DARK,
                    (48, 128, 68)
                ]
            ),
            random.randint(8, 18),
            random.randint(80, 160)
        )


# ============================================================
# ASHOKA CHAKRA
# ============================================================

def paint_chakra():

    cx = 320
    cy = 275

    chakra = ImageDraw.Draw(canvas)

    radius = 55

    chakra.ellipse(
        (
            cx - radius,
            cy - radius,
            cx + radius,
            cy + radius
        ),
        outline=(25, 47, 80),
        width=6
    )

    for i in range(24):

        angle = (
            math.pi * 2
            * i
            / 24
        )

        x = cx + math.cos(angle) * radius
        y = cy + math.sin(angle) * radius

        chakra.line(
            (
                cx,
                cy,
                x,
                y
            ),
            fill=(25, 47, 80),
            width=3
        )


# ============================================================
# ATMOSPHERIC BACKGROUND
# ============================================================

def paint_atmosphere():

    global canvas

    layer = Image.new(
        "RGBA",
        (WIDTH, HEIGHT),
        (0, 0, 0, 0)
    )

    ld = ImageDraw.Draw(layer)

    # sunset glow

    for radius in range(
        420,
        40,
        -20
    ):

        alpha = int(
            3 +
            (420 - radius) / 100
        )

        ld.ellipse(
            (
                760 - radius,
                310 - radius,
                760 + radius,
                310 + radius
            ),
            fill=(
                196,
                101,
                40,
                alpha
            )
        )

    # smoke clouds

    for _ in range(80):

        x = random.randint(
            0,
            WIDTH
        )

        y = random.randint(
            300,
            700
        )

        r = random.randint(
            20,
            90
        )

        ld.ellipse(
            (
                x - r,
                y - r,
                x + r,
                y + r
            ),
            fill=(
                57,
                51,
                45,
                random.randint(
                    10,
                    35
                )
            )
        )

    layer = layer.filter(
        ImageFilter.GaussianBlur(18)
    )

    canvas = Image.alpha_composite(
        canvas.convert("RGBA"),
        layer
    )


# ============================================================
# LOAD BOSE
# ============================================================

def load_bose():

    image = cv2.imread(
        REFERENCE_IMAGE
    )

    if image is None:

        raise FileNotFoundError(
            f"""
Could not find:

{REFERENCE_IMAGE}

Place a clear Bose reference image
in the same folder as this program.
"""
        )

    image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    # Remove excessive background detail

    image = cv2.detailEnhance(
        image,
        sigma_s=10,
        sigma_r=0.15
    )

    # Painterly processing

    image = cv2.bilateralFilter(
        image,
        9,
        80,
        80
    )

    # Slight oil-paint effect

    try:

        image = cv2.xphoto.oilPainting(
            image,
            7,
            1
        )

    except Exception:

        # xphoto is optional
        pass

    return image


# ============================================================
# PAINTERLY BOSE
# ============================================================

def prepare_bose():

    image = load_bose()

    h, w = image.shape[:2]

    target_height = 620

    scale = (
        target_height / h
    )

    target_width = int(
        w * scale
    )

    image = cv2.resize(
        image,
        (
            target_width,
            target_height
        ),
        interpolation=cv2.INTER_AREA
    )

    # Create soft painted edges

    image = cv2.GaussianBlur(
        image,
        (3, 3),
        0
    )

    # Convert to PIL

    pil = Image.fromarray(
        image
    ).convert("RGBA")

    # Slight warm cinematic tone

    arr = np.array(pil).astype(
        np.float32
    )

    arr[:, :, 0] *= 1.05
    arr[:, :, 1] *= 0.98
    arr[:, :, 2] *= 0.88

    arr = np.clip(
        arr,
        0,
        255
    ).astype(np.uint8)

    pil = Image.fromarray(
        arr
    ).convert("RGBA")

    return pil


# ============================================================
# CREATE PAINT MASK FOR BOSE
# ============================================================

def create_paint_mask(bose):

    w, h = bose.size

    mask = Image.new(
        "L",
        (
            w,
            h
        ),
        0
    )

    md = ImageDraw.Draw(mask)

    # Large irregular brush regions

    for _ in range(550):

        x = random.randint(
            0,
            w
        )

        y = random.randint(
            0,
            h
        )

        rw = random.randint(
            20,
            100
        )

        rh = random.randint(
            15,
            80
        )

        md.ellipse(
            (
                x - rw,
                y - rh,
                x + rw,
                y + rh
            ),
            fill=random.randint(
                60,
                180
            )
        )

    mask = mask.filter(
        ImageFilter.GaussianBlur(4)
    )

    return mask


# ============================================================
# PAINT BOSE
# ============================================================

def paint_bose(bose_image):

    global canvas

    bose_w, bose_h = bose_image.size

    # Place Netaji toward right-center

    x = 560
    y = 155

    mask = create_paint_mask(
        bose_image
    )

    # Convert into layers

    for progress in np.linspace(
        0,
        1,
        160
    ):

        threshold = int(
            progress * 255
        )

        progressive_mask = mask.point(
            lambda p:
            255
            if p < threshold
            else 0
        )

        layer = Image.new(
            "RGBA",
            (WIDTH, HEIGHT),
            (0, 0, 0, 0)
        )

        layer.paste(
            bose_image,
            (
                x,
                y
            ),
            progressive_mask
        )

        canvas = Image.alpha_composite(
            canvas.convert("RGBA"),
            layer
        )

        draw_brush_highlights(
            x,
            y,
            bose_w,
            bose_h,
            progress
        )

        render()

        clock.tick(
            FPS
        )


# ============================================================
# BRUSH HIGHLIGHTS
# ============================================================

def draw_brush_highlights(
    x,
    y,
    w,
    h,
    progress
):

    global canvas

    if progress <= 0:
        return

    count = int(
        progress * 35
    )

    layer = canvas.convert(
        "RGBA"
    )

    for _ in range(count):

        bx = random.randint(
            x,
            x + w
        )

        by = random.randint(
            y,
            y + h
        )

        length = random.randint(
            15,
            55
        )

        brush_stroke(
            layer,
            (
                bx,
                by
            ),
            (
                bx + length,
                by + random.randint(
                    -5,
                    5
                )
            ),
            random.choice(
                [
                    (205, 185, 145),
                    (110, 90, 67),
                    (65, 55, 45)
                ]
            ),
            random.randint(
                2,
                7
            ),
            random.randint(
                25,
                70
            )
        )

    canvas = layer.convert(
        "RGB"
    )


# ============================================================
# TEXT
# ============================================================

def get_font(size, bold=True):

    paths = [
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/georgia.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
    ]

    for path in paths:

        try:

            return ImageFont.truetype(
                path,
                size
            )

        except Exception:
            pass

    return ImageFont.load_default()


def paint_text():

    global canvas
    d = ImageDraw.Draw(canvas)

    # Left-aligned, larger and brighter title and subtitle
    font_main = get_font(64)
    left_x = 1
    title_y = 30
    d.text((left_x, title_y), "HAPPY 80TH", font=font_main, fill=SAFFRON_LIGHT)

    font_sub = get_font(36)
    d.text((left_x, title_y + 70), "INDEPENDENCE DAY", font=font_sub, fill=GOLD)

    # Draw or load an India map on the left under the subtitle
    def draw_india_map(center_x, y_off, scale=1.0):
        pts = [
            (100, 140), (110, 120), (130, 110), (150, 115), (170, 140),
            (180, 170), (175, 200), (160, 220), (150, 260), (140, 300),
            (130, 320), (120, 330), (105, 335), (95, 330), (90, 320), (85, 300),
            (80, 270), (85, 240), (90, 210), (95, 180)
        ]
        scaled = [
            (center_x + int((px - 100) * scale), y_off + int((py - 140) * scale))
            for px, py in pts
        ]
        d.polygon(scaled, fill=SAFFRON_LIGHT, outline=SAFFRON)

    # Try to use an external india reference image if available, otherwise draw polygon
    try:
        india_img = Image.open("india.png").convert("RGBA")
        iw, ih = india_img.size
        target_w = 300
        scale = target_w / iw
        india_resized = india_img.resize((int(iw * scale), int(ih * scale)), Image.LANCZOS)

        # Ensure map doesn't overlap subtitle or portrait area
        subtitle_bbox = d.textbbox((left_x, title_y + 70), "INDEPENDENCE DAY", font=font_sub)
        subtitle_bottom = subtitle_bbox[3]
        map_y = subtitle_bottom + 12

        # Portrait placement (avoid overlapping); portrait is drawn at x=560,y=155
        portrait_left = 560
        portrait_top = 155

        # Adjust scale so map fits left of portrait and below subtitle
        w_map, h_map = india_resized.size
        max_width = portrait_left - 20 - left_x
        max_height = portrait_top - 10 - map_y
        new_scale = scale
        if max_width > 20 and w_map > max_width:
            new_scale = min(new_scale, max_width / iw)
        if max_height > 20 and h_map > max_height:
            new_scale = min(new_scale, max_height / ih)

        if new_scale != scale:
            india_resized = india_img.resize((int(iw * new_scale), int(ih * new_scale)), Image.LANCZOS)
            w_map, h_map = india_resized.size

        # Remove white/near-white background by setting alpha=0 where RGB is near 255
        try:
            arr = np.array(india_resized)
            if arr.shape[2] >= 3:
                r = arr[:, :, 0]
                g = arr[:, :, 1]
                b = arr[:, :, 2]
                # threshold for near-white (adjustable)
                mask = (r > 240) & (g > 240) & (b > 240)
                if arr.shape[2] == 4:
                    arr[mask, 3] = 0
                else:
                    alpha = np.full((arr.shape[0], arr.shape[1]), 255, dtype=np.uint8)
                    alpha[mask] = 0
                    arr = np.dstack((arr[:, :, :3], alpha))
                india_resized = Image.fromarray(arr)
        except Exception:
            # if numpy-based mask fails, continue with original
            pass

        canvas.paste(india_resized, (left_x, map_y), india_resized)
    except Exception:
        # fallback: draw stylized polygon map to the left below subtitle
        subtitle_bbox = d.textbbox((left_x, title_y + 70), "INDEPENDENCE DAY", font=font_sub)
        subtitle_bottom = subtitle_bbox[3]
        draw_india_map(left_x + 80, subtitle_bottom + 12, scale=1.1)

    # Quote on main canvas (right area)
    quote_font = get_font(32)
    lines = ['"Give me blood,', 'and I shall give you freedom!"']
    yq = 590
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=quote_font)
        tw = bbox[2] - bbox[0]
        d.text((300 - tw / 2, yq), line, font=quote_font, fill=SAFFRON_LIGHT, stroke_width=2, stroke_fill=(38, 31, 25))
        yq += 32

    # Attribution

    attribution_font = get_font(
        20
    )

    d.text(
        (
            820,
            655
        ),
        "— Netaji Subhas Chandra Bose",
        font=attribution_font,
        anchor="mm",
        fill=WHITE
    )

    # Bottom

    bottom_font = get_font(24)

    d.text(
        (
            WIDTH // 2,
            100
        ),
        "JAI HIND  •  VANDE MATARAM  •  AZAD HIND FAUJ",
        font=attribution_font,
        anchor="mm",
        fill=GREEN_DARK
    )


# ============================================================
# PAINT PARTICLES
# ============================================================

def paint_particles():

    global canvas

    layer = canvas.convert(
        "RGBA"
    )

    for _ in range(250):

        x = random.randint(
            0,
            WIDTH
        )

        y = random.randint(
            0,
            HEIGHT
        )

        radius = random.choice(
            [
                1,
                1,
                2,
                3
            ]
        )

        ImageDraw.Draw(
            layer
        ).ellipse(
            (
                x - radius,
                y - radius,
                x + radius,
                y + radius
            ),
            fill=random.choice(
                [
                    (230, 140, 50, 130),
                    (245, 190, 100, 100),
                    (80, 70, 55, 90)
                ]
            )
        )

    canvas = layer.convert(
        "RGB"
    )


# ============================================================
# VIGNETTE
# ============================================================

def add_vignette():

    global canvas

    overlay = Image.new(
        "RGBA",
        (
            WIDTH,
            HEIGHT
        ),
        (0, 0, 0, 0)
    )

    od = ImageDraw.Draw(
        overlay
    )

    for i in range(20):

        alpha = int(
            3 + i * 2
        )

        od.rectangle(
            (
                i * 8,
                i * 5,
                WIDTH - i * 8,
                HEIGHT - i * 5
            ),
            outline=(
                20,
                18,
                15,
                alpha
            ),
            width=4
        )

    overlay = overlay.filter(
        ImageFilter.GaussianBlur(10)
    )

    canvas = Image.alpha_composite(
        canvas.convert("RGBA"),
        overlay
    ).convert("RGB")


# ============================================================
# RENDER TO PYGAME
# ============================================================

def render():

    rgb = canvas.convert(
        "RGB"
    )

    data = rgb.tobytes()

    surface = pygame.image.fromstring(
        data,
        rgb.size,
        "RGB"
    )

    screen.blit(
        surface,
        (0, 0)
    )

    pygame.display.flip()


# ============================================================
# PAINTING SEQUENCE
# ============================================================

def main():

    global canvas

    print()
    print("=" * 60)
    print("   NETAJI - DIGITAL PAINTING")
    print("   Learn Build Share")
    print("=" * 60)
    print()

    start_time = time.time()

    # --------------------------------------------------------
    # STEP 1
    # Canvas
    # --------------------------------------------------------

    print("1/8  Preparing canvas...")

    create_paper_texture()

    render()

    time.sleep(
        0.5
    )

    # --------------------------------------------------------
    # STEP 2
    # Atmosphere
    # --------------------------------------------------------

    print("2/8  Painting atmosphere...")

    paint_atmosphere()

    render()

    time.sleep(
        0.6
    )

    # --------------------------------------------------------
    # STEP 3
    # Flag
    # --------------------------------------------------------

    print("3/8  Painting Indian flag...")

    paint_flag()

    render()

    time.sleep(
        0.5
    )

    # --------------------------------------------------------
    # STEP 4
    # Chakra
    # --------------------------------------------------------

    print("4/8  Painting Ashoka Chakra...")

    paint_chakra()

    render()

    time.sleep(
        0.5
    )

    # --------------------------------------------------------
    # STEP 5
    # Bose
    # --------------------------------------------------------

    print(
        "5/8  Painting Netaji portrait..."
    )

    bose = prepare_bose()

    paint_bose(
        bose
    )

    # --------------------------------------------------------
    # STEP 6
    # Paint particles
    # --------------------------------------------------------

    print(
        "6/8  Adding paint texture..."
    )

    paint_particles()

    render()

    time.sleep(
        0.5
    )

    # --------------------------------------------------------
    # STEP 7
    # Typography
    # --------------------------------------------------------

    print(
        "7/8  Painting typography..."
    )

    paint_text()

    render()

    time.sleep(
        0.5
    )

    # --------------------------------------------------------
    # STEP 8
    # Final finish
    # --------------------------------------------------------

    print(
        "8/8  Applying final painterly finish..."
    )

    add_vignette()

    render()

    elapsed = (
        time.time()
        - start_time
    )

    print()
    print(
        f"Painting completed in {elapsed:.1f} seconds."
    )
    print()
    print(
        "Press ESC or close the window."
    )

    # --------------------------------------------------------
    # Keep Window Open
    # --------------------------------------------------------

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
                running = False

        clock.tick(
            FPS
        )

    pygame.quit()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    main()