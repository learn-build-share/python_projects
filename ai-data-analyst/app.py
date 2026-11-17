import streamlit as st

from analyst import HELP, answer

st.set_page_config(page_title="DataSense AI · Data Analyst", page_icon="🤖", layout="wide")

with st.sidebar:
    st.header("📂 Upload your data")
    st.caption("CSV file (order_id, item, qty, price, city)")
    file = st.file_uploader("Upload CSV", type=["csv"])
    if file is not None:
        st.success(f"{file.name} uploaded · {file.size / 1_000_000:.1f} MB")
    st.divider()
    st.markdown(HELP)

st.title("DataSense AI 🤖")
st.caption("Your AI Data Analyst · ask anything about your data")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

q = st.chat_input("Ask about your data...")

if q:
    st.session_state.messages.append({"role": "user", "content": q})
    with st.chat_message("user"):
        st.markdown(q)

    with st.chat_message("assistant"):
        if file is None:
            reply = "Please upload a CSV file first 📂"
            st.markdown(reply)
        else:
            with st.spinner("Analyzing lazily, one row at a time..."):
                result = answer(q, file)
            reply = result["text"].replace("\n", "  \n")
            st.markdown(reply)
            if result["intent"] != "help":
                c1, c2 = st.columns(2)
                c1.metric("Peak memory", f"{result['peak_mb']:.2f} MB")
                c2.metric("Time taken", f"{result['seconds']:.2f} s")
    st.session_state.messages.append({"role": "assistant", "content": reply})
