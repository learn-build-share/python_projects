import streamlit as st

st.set_page_config(
    page_title="Break vs Continue Quiz",
    page_icon="🐍",
    layout="centered"
)

st.markdown("""
<style>

html, body, [data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #13213f 0%, #020617 60%);
}

.main {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    max-width: 980px;
    margin: 0 auto;
}

.title {
    text-align: center;
    font-size: 2.9rem;
    font-weight: 900;
    color: #86efac;
    margin-bottom: 0.3rem;
    text-shadow: 0 0 20px rgba(134, 239, 172, 0.18);
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 1.12rem;
    margin-bottom: 1.5rem;
}

.concept-card {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin: 0 auto 1.9rem auto;
    max-width: 900px;
}

.concept-pill {
    background: rgba(15, 23, 42, 0.92);
    border: 1px solid rgba(134, 239, 172, 0.35);
    border-radius: 999px;
    padding: 0.7rem 1rem;
    color: #f8fafc;
    font-weight: 700;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.24);
}

.stCodeBlock {
    background: #09111f;
    border-radius: 16px;
    border: 1px solid #334155;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.28);
}

div[data-testid="stVerticalBlock"] > div {
    margin-bottom: 0.9rem;
}

div[data-testid="stSubheader"] {
    text-align: center;
    color: #f8fafc;
    font-size: 1.4rem !important;
}

div[data-testid="stRadio"] > div {
    gap: 0.55rem;
}

div[data-testid="stRadio"] label {
    background: #0f172a;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 0.75rem 0.9rem;
    color: #e2e8f0;
    transition: 0.2s ease;
}

div[data-testid="stRadio"] label:hover {
    border-color: #86efac;
    transform: translateY(-1px);
}

.stButton > button {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    border: none;
    border-radius: 999px;
    padding: 0.7rem 1.2rem;
    font-weight: 800;
    box-shadow: 0 8px 18px rgba(34, 197, 94, 0.25);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #4ade80, #22c55e);
    color: white;
}

.stAlert {
    border-radius: 14px;
}

[data-testid="stMetricValue"] {
    color: #86efac;
}

[data-testid="stExpander"] {
    background: rgba(15, 23, 42, 0.95);
    border: 1px solid rgba(148, 163, 184, 0.25);
    border-radius: 14px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🐍Python QUIZ</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Practice how <b>break</b> stops a loop and <b>continue</b> skips just one step.</div>", unsafe_allow_html=True)
st.markdown("""
<div class='concept-card'>
    <div class='concept-pill'>break → stops the loop at once</div>
    <div class='concept-pill'>continue → skips only the current step</div>
</div>
""", unsafe_allow_html=True)

examples = [

{
"title":"Question 1",
"code":'''for i in range(5):
    if i==3:
        break
    print(i)

print("Done")''',

"question":"Choose the correct output.",
"options":[
"0 1 2 Done",
"0 1 2 3 Done",
"1 2 3 Done",
"0 1 Done"
],
"answer":"0 1 2 Done",
"explanation":
"""break immediately stops the loop.

Execution:

i=0 -> print

i=1 -> print

i=2 -> print

i=3 -> break

Loop ends

Done prints outside the loop.
"""
},

{
"title":"Question 2",
"code":'''for i in range(5):
    if i==3:
        continue
    print(i)

print("Done")''',

"question":"Output?",
"options":[
"0 1 2 4 Done",
"0 1 2 3 4 Done",
"0 1 2 Done",
"4 Done"
],
"answer":"0 1 2 4 Done",
"explanation":
"""continue skips only one iteration.

3 is skipped.

The loop continues with 4.
"""
},

{
"title":"Question 3",
"code":'''for i in range(1,6):
    if i%2==0:
        continue
    print(i)''',

"question":"Output?",
"options":[
"1 3 5",
"2 4",
"1 2 3 4 5",
"None"
],
"answer":"1 3 5",
"explanation":
"Even numbers are skipped because continue jumps to the next iteration."
},

{
"title":"Question 4",
"code":'''for i in range(1,6):
    if i==4:
        break
    print(i)''',

"question":"Output?",
"options":[
"1 2 3",
"1 2 3 4",
"4",
"1 2"
],
"answer":"1 2 3",
"explanation":
"Loop stops before printing 4."
},

{
"title":"Question 5",
"code":'''numbers=[2,4,7,8,10]

for n in numbers:
    if n==7:
        break
    print(n)''',

"question":"Output?",
"options":[
"2 4",
"2 4 7",
"7",
"2 4 8"
],
"answer":"2 4",
"explanation":
"Loop ends when 7 is found."
},

{
"title":"Question 6",
"code":'''numbers=[2,4,7,8,10]

for n in numbers:
    if n==7:
        continue
    print(n)''',

"question":"Output?",
"options":[
"2 4 8 10",
"2 4",
"7",
"2 4 7 8"
],
"answer":"2 4 8 10",
"explanation":
"Only 7 is skipped."
},

{
"title":"Question 7",
"code":'''for letter in "PYTHON":
    if letter=="T":
        break
    print(letter)''',

"question":"Output?",
"options":[
"P Y",
"P Y T",
"P Y H",
"Nothing"
],
"answer":"P Y",
"explanation":
"Loop stops when T appears."
},

{
"title":"Question 8",
"code":'''for letter in "PYTHON":
    if letter=="T":
        continue
    print(letter)''',

"question":"Output?",
"options":[
"P Y H O N",
"P Y",
"P Y T H O N",
"H O N"
],
"answer":"P Y H O N",
"explanation":
"T is skipped."
},

{
"title":"Question 9",
"code":'''i=1

while i<=5:

    if i==4:
        break

    print(i)
    i+=1''',

"question":"Output?",
"options":[
"1 2 3",
"1 2 3 4",
"5",
"Infinite loop"
],
"answer":"1 2 3",
"explanation":
"When i becomes 4, break stops the loop."
},

{
"title":"Question 10",
"code":'''for i in range(6):

    if i%3==0:
        continue

    print(i)''',

"question":"Output?",
"options":[
"1 2 4 5",
"0 3",
"1 2 3 4 5",
"0 1 2"
],
"answer":"1 2 4 5",
"explanation":
"0 and 3 are multiples of 3, so they are skipped."
},

{
"title":"Question 11",
"code":'''for i in range(5):

    print(i)

    if i==2:
        break

print("Finished")''',

"question":"Output?",
"options":[
"0 1 2 Finished",
"0 1 Finished",
"0 1 2 3 4 Finished",
"Finished"
],
"answer":"0 1 2 Finished",
"explanation":
"2 is printed before break executes."
},

{
"title":"Question 12",
"code":'''for i in range(5):

    if i==2:
        continue

    print(i)

print("Done")''',

"question":"Output?",
"options":[
"0 1 3 4 Done",
"0 1 2 3 4 Done",
"2 Done",
"Done"
],
"answer":"0 1 3 4 Done",
"explanation":
"Iteration 2 is skipped."
}

]

if "score" not in st.session_state:
    st.session_state.score=0

if "answered" not in st.session_state:
    st.session_state.answered={}

for idx,item in enumerate(examples):

    left, center, right = st.columns([1, 5, 1])

    with center:
        st.markdown("---")

        st.subheader(item["title"])

        st.code(item["code"],language="python")

        choice=st.radio(
            item["question"],
            item["options"],
            key=f"radio{idx}"
        )

        if st.button("Check My Answer",key=f"btn{idx}"):

            if idx not in st.session_state.answered:

                if choice==item["answer"]:
                    st.success("✅ Nice work — that answer is correct!")
                    st.session_state.score+=1
                else:
                    st.error("❌ That one missed the mark.")
                    st.info(f"Correct Answer: **{item['answer']}**")

                st.session_state.answered[idx]=True

            with st.expander("💡 See explanation", expanded=True):
                st.write(item["explanation"])

st.markdown("---")

st.metric("🏆 Score",f"{st.session_state.score}/{len(examples)}")

if st.button("🔄 Restart Practice"):
    st.session_state.score=0
    st.session_state.answered={}
    st.rerun()

st.markdown("---")

st.header("🎯 Quick Mini Demo")

st.write("Try entering **skip** or **exit** to see how the little Python example responds.")

questions=[
    "What is Python?",
    "What is Variable?",
    "What is Loop?"
]

for q in questions:

    ans=st.text_input(q,key=q)

    if ans:

        if ans.lower()=="exit":
            st.error("Quiz Ended 👋")
            st.stop()

        elif ans.lower()=="skip":
            st.warning("Question Skipped")
            continue

        else:
            st.success("Answer Submitted ✅")

st.success("Quiz Completed 🎉")