import io
import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(
    page_title="Certificate Generator",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Certificate Generator")
st.write("Generate Certificate Numbers using **enumerate()**")

# -----------------------------
# Student Data (Dictionary)
# -----------------------------

students = [
    {
        "name": "Rahul",
        "course": "Python",
        "college": "ABC College"
    },
    {
        "name": "Sai",
        "course": "Data Science",
        "college": "XYZ University"
    },
    {
        "name": "Akhil",
        "course": "AI & ML",
        "college": "KMIT"
    },
    {
        "name": "Pooja",
        "course": "Python",
        "college": "VNR VJIET"
    },
    {
        "name": "Divya",
        "course": "Cyber Security",
        "college": "JNTU"
    }
]

st.subheader("Student Details")

st.dataframe(pd.DataFrame(students), use_container_width=True)

# ----------------------------------
# Generate Dummy Certificate for a Student
# ----------------------------------

student_names = [student["name"] for student in students]
selected_name = st.selectbox("Select a student to generate a dummy certificate:", student_names)
selected_student = next(student for student in students if student["name"] == selected_name)

st.markdown(
    f"**Selected Student:** {selected_student['name']}  \
    Course: {selected_student['course']}  \
    College: {selected_student['college']}"
)


def get_font(font_name, size):
    fonts = [font_name, "arial.ttf", "SegoeUI.ttf", "DejaVuSans.ttf"]
    for font in fonts:
        try:
            return ImageFont.truetype(font, size)
        except Exception:
            continue
    return ImageFont.load_default()


def create_certificate_image(student, certificate_no):
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

    # Outer frame
    draw.rectangle([30, 30, width - 30, height - 30], outline=border_color, width=12)
    draw.rectangle([70, 70, width - 70, height - 70], outline=border_color, width=4)

    # Accent bar
    draw.rectangle([90, 90, width - 90, 190], fill=highlight_color)
    draw.text((width // 2, 140), "Certificate of Achievement", font=title_font, fill=accent_color, anchor="mm")

    # Main content
    draw.text((width // 2, 260), "This is to certify that", font=subtitle_font, fill=text_color, anchor="mm")
    draw.text((width // 2, 350), student["name"], font=name_font, fill=accent_color, anchor="mm")
    draw.text((width // 2, 430), "has successfully completed the", font=body_font, fill=text_color, anchor="mm")
    draw.text((width // 2, 490), f"{student['course']} course", font=body_font, fill=accent_color, anchor="mm")
    draw.text((width // 2, 550), f"at {student['college']}", font=body_font, fill=text_color, anchor="mm")

    # Decorative divider
    draw.line([(200, 620), (width - 200, 620)], fill=border_color, width=6)
    draw.text((width // 2, 690), "Awarded in recognition of effort, learning, and achievement.", font=subtitle_font, fill=text_color, anchor="mm")

    # Signature block
    sign_y = height - 250
    draw.line([(width // 2 - 320, sign_y), (width // 2 + 320, sign_y)], fill=accent_color, width=4)
    draw.text((width // 2, sign_y + 30), "Authorized Signature", font=small_font, fill=accent_color, anchor="mm")

    # Footer details
    draw.text((120, height - 130), f"Certificate No: {certificate_no}", font=small_font, fill=text_color)
    from datetime import date
    issue_date = date.today().strftime("%d %B %Y")
    draw.text((width - 120, height - 130), f"Date: {issue_date}", font=small_font, fill=text_color, anchor="rm")
    draw.text((width - 120, height - 90), "Learn Build Share", font=small_font, fill=accent_color, anchor="rm")

    return image


if st.button("Generate Dummy Certificate"):
    certificate_no = f"DUMMY-2026-{selected_name[:3].upper()}-{student_names.index(selected_name)+1:03d}"
    certificate_image = create_certificate_image(selected_student, certificate_no)
    st.success("Dummy Certificate Generated Successfully!")
    st.image(certificate_image, caption="Dummy Certificate Preview", use_column_width=True)

    buffered = io.BytesIO()
    certificate_image.save(buffered, format="PNG")
    st.download_button(
        label="📥 Download Certificate PNG",
        data=buffered.getvalue(),
        file_name=f"{selected_name.replace(' ', '_')}_certificate.png",
        mime="image/png"
    )

# ----------------------------------
# Generate Certificates
# ----------------------------------

if st.button("Generate Certificates"):

    certificate_data = []

    # enumerate() automatically gives serial numbers
    for serial, student in enumerate(students, start=1):

        certificate_number = f"CERT2026-{serial:03d}"

        certificate_data.append(
            {
                "Certificate No": certificate_number,
                "Student Name": student["name"],
                "Course": student["course"],
                "College": student["college"]
            }
        )

    result = pd.DataFrame(certificate_data)

    st.success("Certificates Generated Successfully!")

    st.dataframe(result, use_container_width=True)

    csv = result.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="certificates.csv",
        mime="text/csv"
    )

# ----------------------------------
# range() Demo
# ----------------------------------

st.divider()

st.subheader("Learn range()")

numbers = list(range(1, 11))

st.write("Numbers generated using `range(1, 11)`")

st.code(numbers)