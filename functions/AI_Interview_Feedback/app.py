import os
from datetime import datetime

import pdfplumber
import streamlit as st
from docx import Document
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY"),
)
st.set_page_config(
    page_title="AI Interview Feedback Generator",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Interview Feedback Generator")

st.markdown(
"""
Upload your resume and get AI powered interview feedback.

Made with ❤️ by **Learn Build Share**
"""
)

st.divider()

left, right = st.columns([2,1])

with left:

    uploaded_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf","docx","txt"]
    )

    job_role = st.text_input(
        "💼 Target Job Role",
        placeholder="Python Developer"
    )

    experience = st.selectbox(
        "👨‍💻 Experience",
        [
            "Fresher",
            "0-2 Years",
            "2-5 Years",
            "5+ Years"
        ]
    )

with right:

    st.info(
        """
### Process

✅ Upload Resume

⬇️

🤖 Analyze Resume

⬇️

📊 Calculate Score

⬇️

💬 Generate Feedback
"""
    )

st.divider()

generate = st.button(
    "🚀 Generate Interview Feedback",
    use_container_width=True
)

def extract_resume_text(uploaded_file):

    uploaded_file.seek(0)
    filename = uploaded_file.name.lower()

    if filename.endswith(".txt"):
        return uploaded_file.read().decode("utf-8", errors="ignore")

    if filename.endswith(".pdf"):
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    if filename.endswith(".docx"):
        document = Document(uploaded_file)
        return "\n".join(para.text for para in document.paragraphs)

    return ""

def analyze_resume(resume_text, job_role, experience):

    prompt = ChatPromptTemplate.from_template(
        """
You are an expert technical interviewer.

Analyze the following resume.

Target Role:
{role}

Experience:
{experience}

Resume:
{resume}

Return your analysis in this format.

Technical Skills:
- ...

Projects:
- ...

Strengths:
- ...

Weaknesses:
- ...

Missing Skills:
- ...

Overall Summary:
...
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "resume": resume_text,
            "role": job_role,
            "experience": experience,
        }
    )

    return response.content

if generate:

    if uploaded_file is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_role:
        st.error("Please enter target job role.")
        st.stop()

    with st.spinner("Analyzing Resume..."):

        resume_text = extract_resume_text(uploaded_file)

        analysis = analyze_resume(
            resume_text,
            job_role,
            experience,
        )

    st.success("Resume Analysis Completed")

    st.subheader("AI Resume Analysis")

    st.write(analysis)