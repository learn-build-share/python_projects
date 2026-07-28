# skills
skills_database = {

"Python Developer":[
"python",
"django",
"flask",
"sql",
"git",
"numpy",
"pandas"
],

"Java Developer":[
"java",
"spring",
"hibernate",
"sql",
"git"
],

"Data Scientist":[
"python",
"machine learning",
"deep learning",
"tensorflow",
"pandas",
"numpy",
"statistics"
],

"Web Developer":[
"html",
"css",
"javascript",
"react",
"nodejs"
]

}

def clean_text(text):

    return text.lower()

def extract_skills(text, role):

    text = clean_text(text)

    skills = skills_database[role]

    matched = []

    missing = []

    for skill in skills:

        if skill in text:

            matched.append(skill)

        else:

            missing.append(skill)

    return matched, missing


def detect_experience(text):

    years = 0

    for i in range(16):

        if str(i) + " year" in text:

            years = i

    return years

def analyze_resume(
        resume_text,
        role
):

    matched, missing = extract_skills(
        resume_text,
        role
    )

    experience = detect_experience(
        resume_text.lower()
    )

    return {

        "matched_skills": matched,

        "missing_skills": missing,

        "experience": experience,

        "total_skills": len(
            skills_database[role]
        )

    }