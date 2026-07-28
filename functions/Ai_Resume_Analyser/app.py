import streamlit as st
from extractor import extract_text
from analyzer import analyze_resume
from scorer import calculate_score
from recommender import recommend_skills

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -------------------- Custom CSS --------------------
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stButton>button {
    width:100%;
    border-radius:10px;
    height:45px;
    background:#4F46E5;
    color:white;
    font-size:16px;
    border:none;
}

.stButton>button:hover{
    background:#3730A3;
    color:white;
}

.card{
    background:#ffffff;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.big-font{
    font-size:32px;
    font-weight:bold;
}

.small-text{
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# -------------------- Header --------------------

st.markdown(
"""
<div class='card'>
<p class='big-font'>📄 AI Resume Analyzer</p>

<p class='small-text'>
Upload your resume and compare it against your desired job role.
Get ATS score, missing skills, and recommendations instantly.
</p>

</div>
""",
unsafe_allow_html=True
)

# -------------------- Sidebar --------------------

with st.sidebar:

    st.header("⚙️ Configuration")

    job_role = st.selectbox(
        "Select Job Role",
        [
            "Python Developer",
            "Java Developer",
            "Data Scientist",
            "Web Developer"
        ]
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    analyze = st.button("🚀 Analyze Resume")

# -------------------- Main --------------------

if analyze:

    if uploaded_file is None:
        st.warning("Please upload a resume first.")
        st.stop()

    with st.spinner("Analyzing your resume..."):

        resume_text = extract_text(uploaded_file)

        result = analyze_resume(
            resume_text,
            job_role
        )

        score = calculate_score(
            result["matched_skills"],
            result["total_skills"]
        )

        recommendations = recommend_skills(
            result["missing_skills"]
        )

    st.success("Resume analysis completed successfully!")

    # -------------------- Score --------------------

    st.subheader("📊 Resume Score")

    col1, col2 = st.columns([3,1])

    with col1:
        st.progress(score / 100)

    with col2:
        st.metric(
            "ATS Score",
            f"{score}%"
        )

    # -------------------- Skills --------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### ✅ Matched Skills")

        if result["matched_skills"]:
            for skill in result["matched_skills"]:
                st.success(skill)
        else:
            st.info("No matching skills found.")

    with col2:

        st.markdown("### ❌ Missing Skills")

        if result["missing_skills"]:
            for skill in result["missing_skills"]:
                st.error(skill)
        else:
            st.success("No missing skills.")

    # -------------------- Recommendations --------------------

    st.markdown("---")
    st.subheader("💡 Recommended Skills")

    if recommendations:

        for skill in recommendations:
            st.info(f"📌 {skill}")

    else:
        st.success("Great! No additional skills recommended.")

    # -------------------- Detailed Analysis --------------------

    with st.expander("📑 Detailed Analysis"):

        st.json(result)

# -------------------- Footer --------------------

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;color:gray;'>

Made By ❤️ Learn Build Share

</div>
""",
unsafe_allow_html=True
)