import os
import json
import random
import re
from datetime import datetime
from typing import Any

import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(page_title="AI Certificate Generator", layout="wide")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY"),
)

st.title("🏆 AI Certificate Generator")

st.markdown(
    """
    Build a polished certificate preview using a realistic course certificate template.
    Fill in the student and course details below, then generate a professional styled certificate.
    """
)

with st.form("certificate_form"):
    left, right = st.columns(2)
    with left:
        student_name = st.text_input("👤 Student Name *")
        course_name = st.text_input("📚 Course Name *")
        college_name = st.text_input("🏫 College / Institution (Optional)")
        certificate_id = st.text_input("🆔 Certificate ID (Optional)")
    with right:
        mentor_name = st.text_input("👨‍🏫 Mentor Name", value="Learn Build Share Team")
        completion_date = st.date_input("📅 Completion Date", value=datetime.today())
        grade = st.text_input("🏅 Grade / Score (Optional)")
        issuer_name = st.text_input("🏛️ Issuer Name", value="Learn Build Share")

    submitted = st.form_submit_button("Generate Certificate")

if submitted:

    if not student_name:
        st.error("Student Name is required.")
        st.stop()

    if not course_name:
        st.error("Course Name is required.")
        st.stop()

    if not certificate_id:
        certificate_id = f"LBS-{datetime.now().year}-{random.randint(10000,99999)}"

    if not mentor_name:
        mentor_name = "Learn Build Share Team"

    prompt = ChatPromptTemplate.from_template(
        """
You are an AI Certificate Writing Assistant.

Generate a professional certificate for an actual course completion.
Use the student, course, institution, mentor, completion date, grade, and issuer details.
Return ONLY a valid JSON object with these fields:
- title
- subtitle
- recipient
- course
- college
- completion_date
- certificate_id
- mentor
- grade
- issuer
- message

Example:
{{
  "title": "Certificate of Completion",
  "subtitle": "This is to certify that",
  "recipient": "Jane Doe",
  "course": "Artificial Intelligence Fundamentals",
  "college": "Innovate Tech Institute",
  "completion_date": "05 August 2026",
  "certificate_id": "LBS-2026-12345",
  "mentor": "Learn Build Share Team",
  "grade": "A+",
  "issuer": "Learn Build Share",
  "message": "Presented to Jane Doe for successfully completing the Artificial Intelligence Fundamentals course with distinction."
}}

Student Name: {student}
Course Name: {course}
College Name: {college}
Certificate ID: {cid}
Mentor Name: {mentor}
Completion Date: {completion_date}
Grade: {grade}
Issuer: {issuer}
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "student": student_name,
            "course": course_name,
            "college": college_name,
            "cid": certificate_id,
            "mentor": mentor_name,
            "completion_date": completion_date.strftime("%d %B %Y"),
            "grade": grade,
            "issuer": issuer_name,
        }
    )

    def parse_response(resp: Any) -> dict[str, Any]:
        if hasattr(resp, "content") and isinstance(resp.content, str):
            text = resp.content.strip()
        else:
            text = str(resp).strip()

        if not text:
            raise ValueError("Empty response received from the language model.")

        json_match = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if json_match:
            text = json_match.group(0)

        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise ValueError(
                "Unable to parse the language model response as JSON. Raw output:\n" + text
            ) from exc

    try:
        result = parse_response(response)
    except ValueError as exc:
        st.error(str(exc))
        if hasattr(response, "content"):
            st.write("Raw response:")
            st.code(response.content)
        else:
            st.write("Raw response:")
            st.code(str(response))
        st.stop()

    title = result.get("title", "Certificate of Completion")
    subtitle = result.get("subtitle", "This is to certify that")
    recipient = result.get("recipient", student_name)
    course = result.get("course", course_name)
    college = result.get("college", college_name)
    completion_date_text = result.get("completion_date", completion_date.strftime("%d %B %Y"))
    certificate_id_text = result.get("certificate_id", certificate_id)
    mentor = result.get("mentor", mentor_name)
    grade_text = result.get("grade", grade)
    issuer = result.get("issuer", issuer_name)
    message = result.get("message", "Presented for successfully completing this course.")

    def certificate_html(data: dict[str, str]) -> str:
        grade_section = (
            f"<div style=\"margin-top: 16px; font-size: 14px; color: #777;\">Grade</div>"
            f"<div style=\"font-size: 16px; margin-top: 6px;\">{data['grade']}</div>"
            if data["grade"]
            else ""
        )

        college_section = (
            f"<p style=\"margin: 0; font-size: 22px; font-weight: 600;\">{data['college']}</p>"
            if data["college"]
            else ""
        )

        return f"""
        <div style="background: linear-gradient(135deg, #f8f5ec 0%, #ffffff 100%); padding: 30px; display: flex; justify-content: center;">
            <div style="width: 100%; max-width: 960px; border: 12px solid #d4af37; padding: 40px; background: white; box-shadow: 0 14px 40px rgba(0,0,0,0.1);">
                <div style="text-align: center; font-family: 'Georgia', serif; color: #333;">
                    <div style="font-size: 16px; letter-spacing: 4px; color: #a67c00; text-transform: uppercase;">Certificate of Achievement</div>
                    <h1 style="margin: 24px 0 6px; font-size: 48px;">{data['title']}</h1>
                    <p style="margin: 0 0 24px; font-size: 18px; color: #555;">{data['subtitle']}</p>
                    <div style="margin: 24px 0; font-size: 34px; font-weight: 700; letter-spacing: 1px;">{data['recipient']}</div>
                    <p style="margin: 10px 0 4px; font-size: 18px; color: #444;">has successfully completed the</p>
                    <p style="margin: 0; font-size: 24px; font-weight: 600;">{data['course']}</p>
                    {college_section}
                    <div style="margin: 28px 0 16px; font-size: 18px; color: #333; line-height: 1.6;">{data['message']}</div>
                </div>
                <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 24px; font-family: 'Arial', sans-serif; color: #333; margin-top: 40px;">
                    <div style="flex: 1; min-width: 250px;">
                        <div style="font-size: 12px; color: #777; text-transform: uppercase; letter-spacing: 1px;">Issued by</div>
                        <div style="font-size: 18px; font-weight: 700; margin-top: 8px;">{data['issuer']}</div>
                        <div style="margin-top: 16px; font-size: 12px; color: #777;">Mentor</div>
                        <div style="font-size: 16px; margin-top: 6px;">{data['mentor']}</div>
                    </div>
                    <div style="flex: 1; min-width: 250px; text-align: right;">
                        <div style="font-size: 12px; color: #777; text-transform: uppercase; letter-spacing: 1px;">Completion Date</div>
                        <div style="font-size: 18px; font-weight: 700; margin-top: 8px;">{data['completion_date']}</div>
                        <div style="margin-top: 16px; font-size: 12px; color: #777; text-transform: uppercase; letter-spacing: 1px;">Certificate ID</div>
                        <div style="font-size: 16px; margin-top: 6px;">{data['certificate_id']}</div>
                        {grade_section}
                    </div>
                </div>
            </div>
        </div>
        """

    cert_data = {
        "title": title,
        "subtitle": subtitle,
        "recipient": recipient,
        "course": course,
        "college": college,
        "completion_date": completion_date_text,
        "certificate_id": certificate_id_text,
        "mentor": mentor,
        "grade": grade_text,
        "issuer": issuer,
        "message": message,
    }

    certificate_preview = certificate_html(cert_data)

    st.success("Certificate Generated Successfully")
    st.markdown(certificate_preview, unsafe_allow_html=True)

    download_name = f"certificate_{student_name.replace(' ', '_')}_{certificate_id_text}.html"
    st.download_button(
        "Download Certificate HTML",
        certificate_preview,
        file_name=download_name,
        mime="text/html",
    )

    with st.expander("Raw certificate JSON output"):
        st.json(result)
