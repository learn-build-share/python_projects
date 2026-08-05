"""
===========================================
Python Function Arguments Explained
Mini Project: AI Certificate Generator
Author : Learn Build Share
===========================================
"""


# ============================================
# 1. POSITIONAL ARGUMENTS
# ============================================

print("\n========== POSITIONAL ARGUMENTS ==========\n")


def student_details(name, course):
    print(f"Student : {name}")
    print(f"Course  : {course}")


student_details("Arun", "Python")

# Order is important
# student_details("Python", "Arun")  # Wrong Meaning


# ============================================
# 2. NAMED (KEYWORD) ARGUMENTS
# ============================================

print("\n========== NAMED ARGUMENTS ==========\n")


def employee(name, company):
    print(f"Name    : {name}")
    print(f"Company : {company}")


employee(company="Google", name="Rahul")

# Order doesn't matter because
# values are passed using parameter names.


# ============================================
# 3. DEFAULT ARGUMENTS
# ============================================

print("\n========== DEFAULT ARGUMENTS ==========\n")

def welcome(name, country="India"):
    print(f"Hello {name}")
    print(f"Country : {country}")


welcome("Kiran") #with name & default country

welcome("David", "USA") #with name & country


# ============================================
# MINI PROJECT STARTS
# AI CERTIFICATE GENERATOR
# ============================================

print("\n========== MINI PROJECT ==========\n")


# ============================================
# Without *args and **kwargs
# ============================================

def generate_certificate(student_name,
                         course_name,
                         college_name="Not Provided",
                         certificate_id="AUTO-GENERATED",
                         mentor_name="Learn Build Share"):

    print("=" * 40)
    print("      AI CERTIFICATE")
    print("=" * 40)

    print(f"Student Name   : {student_name}")
    print(f"Course Name    : {course_name}")
    print(f"College Name   : {college_name}")
    print(f"Certificate ID : {certificate_id}")
    print(f"Mentor Name    : {mentor_name}")

    print("=" * 40)


generate_certificate(
    "Arun",
    "Python with AI"
)


# ============================================
# Problem Statement
# ============================================

print("\nSometimes we don't know...")
print("- How many students are coming")
print("- How many extra details are coming")


# ============================================
# 4. *ARGS
# ============================================

print("\n========== *ARGS ==========\n")


def register_students(*students):
    print("Students Registered\n")

    for number, student in enumerate(students, start=1):
        print(f"{number}. {student}")


register_students(
    "Arun",
    "Rahul",
    "Kiran",
    "Sneha",
    "Priya",
    "Ravi"
)

"""
*args

Accepts multiple positional values.

Python stores them inside a tuple.
"""


# ============================================
# Another *args Example
# ============================================

print("\nMarks Example\n")


def total_marks(*marks):
    print("Marks :", marks)
    print("Total :", sum(marks))


total_marks(90, 88, 91, 95, 100)


# ============================================
# 5. **KWARGS
# ============================================

print("\n========== **KWARGS ==========\n")


def student_profile(**details):

    print("Student Profile\n")

    for key, value in details.items():
        print(f"{key} : {value}")


student_profile(
    Name="Arun",
    Course="Python",
    College="ABC Engineering College",
    City="Hyderabad",
    Batch="2026"
)

"""
**kwargs

Accepts unlimited key=value pairs.

Python stores them inside a dictionary.
"""


# ============================================
# AI Certificate using **kwargs
# ============================================

print("\nCertificate Extra Details\n")


def certificate(**details):

    print("=" * 40)

    for key, value in details.items():
        print(f"{key:15} : {value}")

    print("=" * 40)


certificate(
    Student="Arun",
    Course="Generative AI",
    College="XYZ College",
    Grade="A+",
    Mentor="Learn Build Share",
    Duration="30 Days",
    Project="AI Certificate Generator"
)


# ============================================
# 6. COMBINING EVERYTHING
# ============================================

print("\n========== EVERYTHING TOGETHER ==========\n")


def create_certificate(student_name,
                       course_name,
                       *skills,
                       certificate_type="AI",
                       **extra_details):

    print("=" * 50)

    print("CERTIFICATE")

    print("=" * 50)

    print("Student :", student_name)
    print("Course  :", course_name)

    print("\nSkills")

    for skill in skills:
        print("-", skill)

    print("\nCertificate Type :", certificate_type)

    print("\nExtra Details")

    for key, value in extra_details.items():
        print(f"{key} : {value}")

    print("=" * 50)


create_certificate(
    "Arun",
    "Python",

    "Functions",
    "OOP",
    "APIs",
    "AI",

    certificate_type="Professional",

    College="ABC College",
    Mentor="John",
    Duration="45 Days",
    Certificate_ID="AI-2026-001",
    Grade="A+"
)


# ============================================
# Interview Notes
# ============================================

print("\n========== INTERVIEW NOTES ==========\n")

print("Positional Arguments")
print("-> Order matters.\n")

print("Named Arguments")
print("-> Parameter name is used while calling.\n")

print("Default Arguments")
print("-> Uses default value if not provided.\n")

print("*args")
print("-> Accepts unlimited positional values.")
print("-> Stored as Tuple.\n")

print("**kwargs")
print("-> Accepts unlimited key=value pairs.")
print("-> Stored as Dictionary.\n")

print("Remember")
print("*args   -> Values")
print("**kwargs -> Key-Value Pairs")