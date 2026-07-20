import random
import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Frozen Set | Event Pass Verification",
    page_icon="🎟️",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------
st.markdown("""
<style>

.main {
    background:#0E1117;
}

.title{
    font-size:42px;
    font-weight:bold;
    color:#4FC3F7;
}

.subtitle{
    font-size:20px;
    color:#B0BEC5;
}

.box{
    background:#1C2333;
    padding:20px;
    border-radius:15px;
    border:1px solid #3949AB;
}

.footer{
    text-align:center;
    color:gray;
    padding-top:40px;
    font-size:14px;
}

.watermark{
    position:fixed;
    bottom:12px;
    right:18px;
    opacity:0.18;
    font-size:24px;
    font-weight:bold;
    color:white;
    pointer-events:none;
}

.hero{
    border-radius:18px;
    padding:25px;
    background:linear-gradient(90deg,#1E3C72,#2A5298);
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Watermark
# ---------------------------------------------------
st.markdown(
    """
<div class="watermark">
© LearnBuildShare
</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# Hero Section
# ---------------------------------------------------
st.markdown("""
<div class="hero">

# 🎟️ LearnBuildShare TechConnect 2026

## Event Pass Verification System

Secure Event Entry using **Python Frozen Set**

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------
# Event Banner
# ---------------------------------------------------

st.image(
    "https://images.unsplash.com/photo-1511578314322-379afb476865?w=1600",
    use_container_width=True,
)

# ---------------------------------------------------
# Introduction
# ---------------------------------------------------

st.info("""
### Scenario

Imagine you are organizing **TechConnect 2026**.

Before the event begins, all visitor Pass IDs are generated.

Once generated,

✅ New Pass IDs should NOT be created

✅ Existing Pass IDs should NOT be removed

✅ Pass IDs should NOT be modified

Only verification should be allowed.

This is exactly where **Frozen Set** is useful.
""")

st.divider()

# ---------------------------------------------------
# Generate Pass IDs
# ---------------------------------------------------

st.header("🎫 Step 1 : Generate Event Pass IDs")

TOTAL_PASSES = 500

if "generated" not in st.session_state:

    ids = []

    for i in range(1001, 1001 + TOTAL_PASSES):
        ids.append(f"PASS-{i}")

    st.session_state.generated = frozenset(ids)

passes = st.session_state.generated

st.success(f"✅ {len(passes)} Event Pass IDs Generated Successfully")

st.write("Sample Pass IDs")

st.code(
"\n".join(list(sorted(passes))[:20])+"\n..."
)

st.success("🔒 These Pass IDs are now LOCKED using Frozen Set.")

st.divider()

# ---------------------------------------------------
# Verify
# ---------------------------------------------------

st.header("✅ Step 2 : Verify Visitor")

verify = st.text_input("Enter Visitor Pass ID")

if st.button("Verify Pass"):

    if verify in passes:

        st.success(f"""
✅ {verify}

Valid Event Pass.

Welcome to TechConnect 2026.
Enjoy the Event!
""")

    else:

        st.error(f"""
❌ {verify}

Invalid Pass ID.

Entry Denied.
""")

st.divider()

# ---------------------------------------------------
# Try Add
# ---------------------------------------------------

st.header("➕ Step 3 : Generate New Pass")

new_id = st.text_input("New Pass ID", placeholder="Example : PASS-1501")

if st.button("Generate Pass"):

    if new_id in passes:

        st.warning(f"""
⚠️ {new_id} has already been generated.

Every Event Pass ID must be unique.
""")

    else:

        st.error(f"""
🔒 Pass Generation Locked

{new_id} cannot be generated.

All Event Pass IDs were generated before the event started.

New Pass IDs cannot be created until TechConnect 2026 is completed.
""")

st.divider()

# ---------------------------------------------------
# Remove Pass
# ---------------------------------------------------

st.header("🗑️ Step 4 : Remove Existing Pass")

remove_id = st.text_input("Pass ID to Remove")

if st.button("Remove Pass"):

    if remove_id in passes:

        st.error(f"""
🔒 Removal Not Allowed

{remove_id} has already been issued.

Issued Event Pass IDs remain unchanged until the event is completed.

Removal is not permitted.
""")

    else:

        st.warning("Pass ID does not exist.")

st.divider()

# ---------------------------------------------------
# Modify Pass
# ---------------------------------------------------

st.header("✏️ Step 5 : Modify Pass ID")

col1,col2=st.columns(2)

with col1:
    old=st.text_input("Existing Pass")

with col2:
    new=st.text_input("New Pass")

if st.button("Update Pass"):

    if old in passes:

        st.error(f"""
🔒 Update Not Allowed

{old}

cannot be changed to

{new}

Reason

Event Pass IDs are immutable once generated.

To issue new passes,

Create a NEW EVENT.
""")

    else:

        st.warning("Existing Pass ID not found.")

st.divider()

# ---------------------------------------------------
# Why Frozen Set
# ---------------------------------------------------

st.header("💡 Why Frozen Set?")

st.markdown("""
Imagine **5,000 visitors** entering the venue.

If someone could...

❌ Add fake passes

❌ Delete issued passes

❌ Modify existing passes

The entire verification system would become unreliable.

Instead, Python provides **Frozen Set**.

Frozen Set guarantees

- ✅ Unique Pass IDs
- ✅ Immutable Data
- ✅ Fast Lookup
- ✅ Secure Verification
- ✅ No Duplicate Passes

That's why it is perfect for systems like

- 🎟️ Event Passes
- 🔑 API Keys
- 🪪 Employee IDs
- 🎫 Movie Tickets
- 🎓 Exam Hall Tickets
""")

st.divider()

# ---------------------------------------------------
# Comparison
# ---------------------------------------------------

st.header("⚖️ Set vs Frozen Set")

c1,c2=st.columns(2)

with c1:

    st.success("""
### Set

✔ Mutable

✔ Add Values

✔ Remove Values

✔ Update Values

✔ Unique Values
""")

with c2:

    st.info("""
### Frozen Set

✔ Immutable

❌ Cannot Add

❌ Cannot Remove

❌ Cannot Modify

✔ Unique Values
""")

st.divider()

# ---------------------------------------------------
# Code Preview
# ---------------------------------------------------

st.header("🐍 Actual Python Code")

st.code(
"""
valid_passes = frozenset({
    "PASS-1001",
    "PASS-1002",
    "PASS-1003"
})

if "PASS-1002" in valid_passes:
    print("Valid Visitor")
""",
language="python"
)

st.divider()

# ---------------------------------------------------
# Interview Tips
# ---------------------------------------------------

st.header("🎯 Interview Question")

st.success("""
Q. Why would you use Frozen Set instead of Set?

Answer:

Use Frozen Set whenever data should never change after creation.

Examples

• Event Pass IDs

• Employee IDs

• API Tokens

• Country Codes

• Configuration Values
""")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.markdown("""
<div class='footer'>

Built by ❤️ Learn Build Share

<b>© LearnBuildShare</b>

Follow for more Python Mini Projects 🚀

</div>
""", unsafe_allow_html=True)