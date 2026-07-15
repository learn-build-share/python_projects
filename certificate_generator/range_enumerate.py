"""
This script demonstrates the use of the range and enumerate functions in Python to generate dummy certificate numbers and enumerate student records.
Developed by © Learn Build Share
"""

students = [
        {"name": "Rahul", "course": "Python", "college": "ABC College"},
        {"name": "Sai", "course": "Data Science", "college": "XYZ University"},
        {"name": "Akhil", "course": "AI & ML", "college": "KMIT"},
        {"name": "Pooja", "course": "Python", "college": "VNR VJIET"},
        {"name": "Divya", "course": "Cyber Security", "college": "JNTU"},
    ]

print("Range example for dummy certificate numbers:")
for index in range(1, 6):
    print(f"DUMMY-2026-{index:03d}")

print("\nEnumerate example for certificate records:")
for serial, student in enumerate(students, start=1):
    certificate_number = f"CERT2026-{serial:03d}"
    print(f"{certificate_number} | {student['name']} | {student['course']} | {student['college']}")
