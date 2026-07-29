import streamlit as st
from datetime import datetime

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="AI Prompt Generator",
    page_icon="🤖",
    layout="centered"
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(180deg,#f8fbff,#eef5ff);
}

.title {
    text-align:center;
    font-size:42px;
    font-weight:700;
    color:#1f4ed8;
}

.subtitle {
    text-align:center;
    color:#555;
    margin-bottom:25px;
}

.prompt-box {
    background:#ffffff;
    padding:20px;
    border-radius:12px;
    border-left:6px solid #2563eb;
    color:#111;
    font-size:17px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.08);
}

.metric-box{
    background:white;
    padding:15px;
    border-radius:12px;
    text-align:center;
    box-shadow:0px 2px 10px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Built-in Function Example
# -------------------------
def word_count(text):
    return len(text.split())


# -------------------------
# User-defined Function
# -------------------------
def generate_prompt(topic, tone, level, purpose):
    prompt = f"""
You are an expert {topic} mentor.

Create a detailed response for the following requirements:

Topic: {topic}

Purpose:
{purpose}

Difficulty Level:
{level}

Tone:
{tone}

Instructions:
- Explain concepts clearly.
- Include real-world examples.
- Give step-by-step guidance.
- Mention common interview questions if applicable.
- End with a concise summary.

Output should be professional, well-structured, and easy to understand.
"""
    return prompt.strip()


# -------------------------
# Header
# -------------------------
st.markdown("<div class='title'>🤖 AI Prompt Generator</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>Python Mini Project using Built-in & User-defined Functions</div>",
    unsafe_allow_html=True,
)

# -------------------------
# Sidebar
# -------------------------
st.sidebar.header("⚙️ Prompt Settings")

tone = st.sidebar.selectbox(
    "Select Tone",
    [
        "Professional",
        "Friendly",
        "Formal",
        "Creative",
        "Technical"
    ]
)

level = st.sidebar.selectbox(
    "Difficulty Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

purpose = st.sidebar.text_area(
    "Purpose",
    "Prepare for technical interviews."
)

# -------------------------
# Input
# -------------------------
topic = st.text_input(
    "📌 Enter Topic",
    placeholder="Example: Python Interview"
)

generate = st.button("🚀 Generate Prompt", use_container_width=True)

# -------------------------
# Output
# -------------------------
if generate:

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:

        prompt = generate_prompt(topic, tone, level, purpose)

        st.markdown("### ✅ Generated Prompt")

        st.markdown(
            f"<div class='prompt-box'>{prompt.replace(chr(10),'<br>')}</div>",
            unsafe_allow_html=True,
        )

        st.markdown("")

        words = word_count(prompt)
        chars = len(prompt)
        lines = len(prompt.splitlines())

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("📝 Words", words)

        with c2:
            st.metric("🔠 Characters", chars)

        with c3:
            st.metric("📄 Lines", lines)

        st.download_button(
            "📥 Download Prompt",
            prompt,
            file_name=f"{topic.replace(' ','_')}_prompt.txt",
            mime="text/plain",
            use_container_width=True,
        )

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.caption(
    f"Made By ❤️ Learn • Build • Share"
)