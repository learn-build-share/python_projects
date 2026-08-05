import streamlit as st
import time

st.set_page_config(page_title="AI Study Notes Generator", page_icon="🤖")

st.title("🤖 AI Study Notes Generator")
st.write("Watch how each function's output becomes the next function's input.")

# ---------- Functions ----------

def receive_topic(topic):
    return topic

def extract_keywords(topic):
    return topic.split()

def generate_summary(topic, keywords):
    return f"{topic} is an important concept that covers {', '.join(keywords)}."

def create_notes(summary):
    return f"""
### 📚 Study Notes

**Overview**
{summary}

**Key Points**
- Learn the fundamentals
- Understand the core concepts
- Practice examples

**Quick Revision**
✅ Revise keywords
✅ Read the summary once
"""

# ---------- Input ----------

topic = st.text_input("📥 Enter Topic", placeholder="Machine Learning")

if st.button("Generate Study Notes"):

    if not topic.strip():
        st.warning("Please enter a topic.")
        st.stop()

    # STEP 1
    status = st.status("📥 Step 1 : Receiving Topic...", expanded=True)
    time.sleep(1)

    received = receive_topic(topic)

    status.write(f"**Output:** `{received}`")
    status.update(label="✅ Step 1 Completed", state="complete")

    st.markdown("### ⬇️ Output ➜ Input")

    time.sleep(1)

    # STEP 2
    status = st.status("🔍 Step 2 : Extracting Keywords...", expanded=True)
    time.sleep(1.5)

    keywords = extract_keywords(received)

    cols = st.columns(len(keywords))

    for col, word in zip(cols, keywords):
        time.sleep(0.3)
        col.success(word)

    status.write(f"**Output:** `{keywords}`")
    status.update(label="✅ Step 2 Completed", state="complete")

    st.markdown("### ⬇️ Output ➜ Input")

    time.sleep(1)

    # STEP 3
    status = st.status("📝 Step 3 : Generating Summary...", expanded=True)
    time.sleep(2)

    summary = generate_summary(received, keywords)

    placeholder = st.empty()

    text = ""
    for ch in summary:
        text += ch
        placeholder.markdown(text + "▌")
        time.sleep(0.02)

    placeholder.markdown(summary)

    status.write("**Output:** Summary Generated")
    status.update(label="✅ Step 3 Completed", state="complete")

    st.markdown("### ⬇️ Output ➜ Input")

    time.sleep(1)

    # STEP 4
    status = st.status("📚 Step 4 : Creating Study Notes...", expanded=True)
    time.sleep(2)

    notes = create_notes(summary)

    st.success("🎉 Study Notes Ready!")

    st.markdown(notes)

    status.update(label="✅ Step 4 Completed", state="complete")