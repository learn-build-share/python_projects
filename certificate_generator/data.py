import pandas as pd


def get_students(uploaded_file=None):
    """Return sample students or load records from a CSV upload."""
    if uploaded_file is not None:
        return load_students_from_csv(uploaded_file)

    return [
        {"name": "Rahul", "course": "Python", "college": "ABC College"},
        {"name": "Sai", "course": "Data Science", "college": "XYZ University"},
        {"name": "Akhil", "course": "AI & ML", "college": "KMIT"},
        {"name": "Pooja", "course": "Python", "college": "VNR VJIET"},
        {"name": "Divya", "course": "Cyber Security", "college": "JNTU"},
    ]


def load_students_from_csv(uploaded_file):
    """Read student data from a CSV file upload."""
    try:
        frame = pd.read_csv(uploaded_file)
    except Exception as exc:
        raise ValueError(f"Unable to read CSV data: {exc}") from exc

    frame.columns = [str(column).strip().lower() for column in frame.columns]
    required_columns = ["name", "course", "college"]
    missing_columns = [column for column in required_columns if column not in frame.columns]

    if missing_columns:
        raise ValueError(f"CSV must include these columns: {', '.join(required_columns)}")

    students = []
    for _, row in frame[required_columns].iterrows():
        student = {
            "name": str(row["name"]).strip() if pd.notna(row["name"]) else "",
            "course": str(row["course"]).strip() if pd.notna(row["course"]) else "",
            "college": str(row["college"]).strip() if pd.notna(row["college"]) else "",
        }
        if student["name"]:
            students.append(student)

    if not students:
        raise ValueError("No valid student rows were found in the uploaded CSV file.")

    return students
