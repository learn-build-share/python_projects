from datetime import date
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


def get_font(font_name, size):
    """Return a font object, falling back gracefully when a font is missing."""
    font_candidates = [font_name, "arial.ttf", "SegoeUI.ttf", "DejaVuSans.ttf"]
    for candidate in font_candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except Exception:
            # Use the next candidate if the preferred font is unavailable.
            continue
    return ImageFont.load_default()


def create_certificate_image(student, certificate_no):
    """Create a certificate image for one student."""
    width, height = 1500, 1000
    image = Image.new("RGB", (width, height), "#fbf7ef")
    draw = ImageDraw.Draw(image)

    title_font = get_font("arialbd.ttf", 72)
    subtitle_font = get_font("arial.ttf", 42)
    name_font = get_font("arialbd.ttf", 64)
    body_font = get_font("arial.ttf", 40)
    small_font = get_font("arial.ttf", 28)

    border_color = "#b78b22"
    accent_color = "#2e4a6f"
    text_color = "#2f2f2f"
    highlight_color = "#d4b56f"

    draw.rectangle([30, 30, width - 30, height - 30], outline=border_color, width=12)
    draw.rectangle([70, 70, width - 70, height - 70], outline=border_color, width=4)
    draw.rectangle([90, 90, width - 90, 190], fill=highlight_color)

    draw.text(
        (width // 2, 140),
        "Certificate of Achievement",
        font=title_font,
        fill=accent_color,
        anchor="mm",
    )
    draw.text((width // 2, 260), "This is to certify that", font=subtitle_font, fill=text_color, anchor="mm")
    draw.text((width // 2, 350), student["name"], font=name_font, fill=accent_color, anchor="mm")
    draw.text((width // 2, 430), "has successfully completed the", font=body_font, fill=text_color, anchor="mm")
    draw.text((width // 2, 490), f"{student['course']} course", font=body_font, fill=accent_color, anchor="mm")
    draw.text((width // 2, 550), f"at {student['college']}", font=body_font, fill=text_color, anchor="mm")

    draw.line([(200, 620), (width - 200, 620)], fill=border_color, width=6)
    draw.text(
        (width // 2, 690),
        "Awarded in recognition of effort, learning, and achievement.",
        font=subtitle_font,
        fill=text_color,
        anchor="mm",
    )

    sign_y = height - 250
    draw.line([(width // 2 - 320, sign_y), (width // 2 + 320, sign_y)], fill=accent_color, width=4)
    draw.text((width // 2, sign_y + 30), "Authorized Signature", font=small_font, fill=accent_color, anchor="mm")

    draw.text((120, height - 130), f"Certificate No: {certificate_no}", font=small_font, fill=text_color)
    issue_date = date.today().strftime("%d %B %Y")
    draw.text((width - 120, height - 130), f"Date: {issue_date}", font=small_font, fill=text_color, anchor="rm")
    draw.text((width - 120, height - 90), "© Learn Build Share", font=small_font, fill=accent_color, anchor="rm")

    return image


def build_certificate_rows(students):
    """Return certificate metadata rows for a list of students."""
    rows = []
    for serial, student in enumerate(students, start=1):
        rows.append(
            {
                "Certificate No": f"CERT2026-{serial:03d}",
                "Student Name": student["name"],
                "Course": student["course"],
                "College": student["college"],
            }
        )
    return rows


def image_to_bytes(image):
    """Convert a PIL image to PNG bytes."""
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()
