# Certificate Generator

This folder contains a small Streamlit app for generating certificate preview images and downloadable CSV records.

## Features
- Generate a sample certificate preview for one student.
- Generate a full CSV export of certificate metadata.
- Upload a custom CSV file with `name`, `course`, and `college` columns.

## How to get started locally

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd python_projects
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run certificate_generator/app.py
   ```

## CSV format
Use a file with these columns:

```csv
name,course,college
Rahul,Python,ABC College
Sai,Data Science,XYZ University
```

## Simple example script
You can also run a small example script for `range()` and `enumerate()` without starting the Streamlit app:

```bash
python certificate_generator/range_enumerate.py
```

This script mirrors the certificate example by generating dummy certificate numbers with `range()` and listing certificate-style rows with `enumerate()`.

## Notes
- The app keeps the design simple and readable.
- Error messages are shown clearly if the uploaded CSV is missing required columns or has no valid rows.

## Copyright
© Learn Build Share
