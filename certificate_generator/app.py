from pathlib import Path

import pandas as pd
import streamlit as st

try:
    from .data import get_students
    from .certificate_utils import build_certificate_rows, create_certificate_image, image_to_bytes
except ImportError:
    from data import get_students
    from certificate_utils import build_certificate_rows, create_certificate_image, image_to_bytes

ASSETS_DIR = Path(__file__).resolve().parent / "assets"


def load_asset(file_name):
    """Load a text asset from the assets directory."""
    asset_path = ASSETS_DIR / file_name
    try:
        return asset_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def load_css():
    """Inject the custom CSS styles into the Streamlit page."""
    css = load_asset("styles.css")
    if css:
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def load_intro_html():
    """Render the introductory HTML section from the assets folder."""
    html = load_asset("hero.html")
    if html:
        st.markdown(html, unsafe_allow_html=True)


def main():
    """Run the Streamlit certificate generator app."""
    st.set_page_config(page_title="Certificate Generator", page_icon="🏆", layout="wide")
    load_css()
    load_intro_html()

    # Keep the layout simple and easy to follow for first-time users.
    st.title("🏆 Certificate Generator")
    st.write("Generate certificate numbers and preview a polished certificate image.")

    uploaded_file = st.file_uploader(
        "Upload a CSV file with name, course, and college columns",
        type=["csv"],
    )

    try:
        students = get_students(uploaded_file)
    except ValueError as exc:
        st.error(str(exc))
        return

    student_names = [student["name"] for student in students]

    if uploaded_file is not None:
        st.caption("Loaded student data from the uploaded CSV file.")
    else:
        st.caption("Using the built-in sample student list.")

    st.subheader("Student details")
    st.dataframe(pd.DataFrame(students), use_container_width=True)

    selected_name = st.selectbox("Select a student to generate a dummy certificate:", student_names)
    selected_student = next(student for student in students if student["name"] == selected_name)

    st.markdown(
        f"""
        <div class="card">
            <p><strong>Selected student:</strong> {selected_student['name']}</p>
            <p><strong>Course:</strong> {selected_student['course']}</p>
            <p><strong>College:</strong> {selected_student['college']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Generate Dummy Certificate", use_container_width=True):
        certificate_no = f"DUMMY-2026-{selected_name[:3].upper()}-{student_names.index(selected_name) + 1:03d}"
        certificate_image = create_certificate_image(selected_student, certificate_no)
        png_bytes = image_to_bytes(certificate_image)

        st.success("Dummy certificate generated successfully.")
        st.image(certificate_image, caption="Dummy Certificate Preview", use_container_width=True)
        st.download_button(
            label="📥 Download Certificate PNG",
            data=png_bytes,
            file_name=f"{selected_name.replace(' ', '_')}_certificate.png",
            mime="image/png",
        )

    if st.button("Generate Certificates", use_container_width=True):
        rows = build_certificate_rows(students)
        result = pd.DataFrame(rows)

        st.success("Certificates generated successfully.")
        st.dataframe(result, use_container_width=True)

        csv_data = result.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download CSV",
            data=csv_data,
            file_name="certificates.csv",
            mime="text/csv",
        )

    st.divider()
    st.subheader("Learn range()")
    numbers = list(range(1, 11))
    st.write("Numbers generated using `range(1, 11)`")
    st.code(numbers)

    st.markdown("<div class='footer'>© Learn Build Share</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
