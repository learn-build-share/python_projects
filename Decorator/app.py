import streamlit as st
from streamlit.components.v1 import html as components_html

# ============================================================
# VIP ENTRY SYSTEM
# Rajamouli Movie Pre-Release Event
# © Learn Build Share
# ============================================================

st.set_page_config(
    page_title="VIP Entry System",
    page_icon="🎬",
    layout="wide",
)

# -----------------------------
# DATA
# -----------------------------
VALID_VIP_PASSES = {
    "VIP1001", "VIP1002", "VIP1003", "VIP1004", "VIP1005",
    "VIP1006", "VIP1007", "VIP1008", "VIP1009", "VIP1010",
}

SPECIAL_GUEST_PASSES = {
    "VIP1001", "VIP1003", "VIP1005", "VIP1008"
}

if "verified" not in st.session_state:
    st.session_state.verified = set()

if "logs" not in st.session_state:
    st.session_state.logs = []

# -----------------------------
# SIMPLE CSS
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background:
        radial-gradient(circle at top left, #3b0000 0%, #090909 35%, #050505 100%);
    }

    .hero {
        background: linear-gradient(90deg, #450000, #090909);
        border: 2px solid #d6a400;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin-bottom: 20px;
    }

    .hero-title {
        color: #ffd447;
        font-size: 42px;
        font-weight: 900;
        margin: 0;
    }

    .hero-sub {
        color: white;
        font-size: 21px;
        font-weight: 700;
        margin-top: 8px;
    }

    .story {
        background: #111111;
        border-left: 5px solid #d6a400;
        border-radius: 12px;
        padding: 20px;
        color: #dddddd;
        font-size: 17px;
        line-height: 1.8;
        margin-bottom: 25px;
    }

    .tile-header {
        font-size: 25px;
        font-weight: 900;
        color: #ffd447;
    }

    .tile-description {
        color: #aaaaaa;
        font-size: 14px;
    }

    .event-card {
        background: linear-gradient(135deg, #350000, #090909);
        border: 1px solid #a50000;
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        min-height: 240px;
    }

    .security-card {
        background: linear-gradient(135deg, #241900, #090909);
        border: 1px solid #d6a400;
        border-radius: 18px;
        padding: 25px;
        min-height: 240px;
    }

    .result-success {
        background: #06351d;
        border: 2px solid #00c76a;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }

    .result-warning {
        background: #382b00;
        border: 2px solid #e0ae00;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }

    .result-error {
        background: #350000;
        border: 2px solid #d40000;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }

    .result-title {
        color: white;
        font-size: 25px;
        font-weight: 900;
    }

    .result-text {
        color: #dddddd;
        margin-top: 8px;
    }

    .footer {
        text-align: center;
        color: #777777;
        padding: 30px;
    }

    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #9b0000, #e00000);
        color: white;
        border: 1px solid #ffd447;
        border-radius: 10px;
        min-height: 50px;
        font-weight: 800;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">🎬 RAJAMOULI MOVIE PRE-RELEASE EVENT</div>
        <div class="hero-sub">🔥 EVENT IS LIVE • VIP ENTRY OPEN 🔥</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# STORY
# ============================================================

# ============================================================
# TILE 1 + TILE 2
# ============================================================

event_col, security_col = st.columns(2)

# -----------------------------
# TILE 1
# -----------------------------
with event_col:

    st.markdown("### 🎬 MOVIE EVENT")

    st.markdown(
        """
        <div class="event-card">
            <div style="font-size:65px;">🎥🔥🎤</div>
            <h2 style="color:#ffd447;">MOVIE PRE-RELEASE EVENT</h2>
            <p style="color:#cccccc;">
                Lights are ON • Fans are READY • Stage is LIVE
            </p>
            <br>
            <div style="font-size:42px;">👑</div>
            <h3 style="color:white;">FRONT ROW</h3>
            <p style="color:#aaaaaa;">
                Only verified Special Guests can enter.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# TILE 2
# -----------------------------
with security_col:

    st.markdown("### 🛡️ SECURITY VALIDATION")

    # SECURITY VALIDATION tile — match the event-card structure for consistent styling
    st.markdown(
        """
        <div class="security-card">
            <div style="font-size:65px;">🛡️🔐</div>
            <h2 style="color:#ffd447;">SECURITY VALIDATION</h2>
            <p style="color:#cccccc;">Checks and decisions for VIP entry</p>
            <br>
            <div style="font-size:42px;">👮‍♂️</div>
            <h3 style="color:white;">VERIFICATION STEPS</h3>
            <p style="color:#aaaaaa;line-height:1.8;">
                🎟️ <b>1.</b> Check VIP Pass<br>
                🔍 <b>2.</b> Validate Pass<br>
                ⭐ <b>3.</b> Verify Special Guest<br>
                🚨 <b>4.</b> Check if pass was already used<br>
                👑 <b>5.</b> Decide Front Row Access
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

# ============================================================
# SECURITY CHECKPOINT
# ============================================================

st.markdown("## 🛡️ SECURITY CHECKPOINT")

st.info(
    "Security team: Enter the VIP pass first. "
    "Then verify whether the guest is a Special Guest."
)

left, right = st.columns(2)

with left:

    pass_id = st.text_input(
        "🎟️ VIP Pass ID",
        placeholder="Example: VIP1001",
    )

    guest_name = st.text_input(
        "👤 Guest Name",
        placeholder="Example: Rahul",
    )

with right:

    st.markdown("### ⭐ Special Guest Verification")

    special_guest = st.checkbox(
        "Guest is claiming Special Guest status"
    )

    st.caption(
        "This checkbox is only the guest's claim. "
        "The system also checks the registered Special Guest pass list."
    )

st.write("")

# ============================================================
# VALIDATION
# ============================================================

if st.button("🛡️ VERIFY PASS & DECIDE ACCESS"):

    pid = pass_id.strip().upper()
    name = guest_name.strip() or "Guest"

    # STEP 1
    if not pid:

        st.markdown(
            """
            <div class="result-error">
                <div class="result-title">🚨 NO VIP PASS</div>
                <div class="result-text">
                    Security cannot allow entry without a VIP Pass.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # STEP 2
    elif pid not in VALID_VIP_PASSES:

        st.markdown(
            """
            <div class="result-error">
                <div class="result-title">❌ INVALID VIP PASS</div>
                <div class="result-text">
                    Security validation failed. Front Row Access denied.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # STEP 3
    elif pid in st.session_state.verified:

        st.markdown(
            """
            <div class="result-warning">
                <div class="result-title">⚠️ PASS ALREADY VERIFIED</div>
                <div class="result-text">
                    This pass has already entered the event.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # STEP 4
    elif pid in SPECIAL_GUEST_PASSES and special_guest:

        st.session_state.verified.add(pid)

        st.session_state.logs.append(
            {
                "Guest": name,
                "Pass ID": pid,
                "VIP Pass": "VALID",
                "Special Guest": "YES",
                "Decision": "FRONT ROW ACCESS",
            }
        )

        st.markdown(
            f"""
            <div class="result-success">
                <div class="result-title">👑 FRONT ROW ACCESS GRANTED</div>
                <div class="result-text">
                    Welcome {name}!<br><br>
                    VIP Pass ✓ &nbsp; Special Guest ✓ &nbsp; Security ✓
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.balloons()

    # STEP 5
    elif pid in SPECIAL_GUEST_PASSES and not special_guest:

        st.markdown(
            """
            <div class="result-warning">
                <div class="result-title">
                    ⭐ SPECIAL GUEST VERIFICATION REQUIRED
                </div>
                <div class="result-text">
                    The VIP Pass belongs to a Special Guest.
                    Confirm Special Guest status to continue.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # STEP 6
    else:

        st.session_state.logs.append(
            {
                "Guest": name,
                "Pass ID": pid,
                "VIP Pass": "VALID",
                "Special Guest": "NO",
                "Decision": "FRONT ROW DENIED",
            }
        )

        st.markdown(
            """
            <div class="result-error">
                <div class="result-title">
                    🚫 FRONT ROW ACCESS DENIED
                </div>
                <div class="result-text">
                    VIP Pass is valid, but this guest is not registered
                    as a Special Guest.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# DECISION FLOW
# ============================================================

st.markdown("---")
st.markdown("## 🔄 SECURITY DECISION FLOW")

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.markdown("### 🎟️ 01")
    st.write("**VIP Pass**")
    st.caption("Is a pass entered?")

with f2:
    st.markdown("### 🔍 02")
    st.write("**Validate**")
    st.caption("Is the pass valid?")

with f3:
    st.markdown("### ⭐ 03")
    st.write("**Special Guest**")
    st.caption("Is the guest verified?")

with f4:
    st.markdown("### 👑 04")
    st.write("**Decision**")
    st.caption("Front Row or Denied?")

# ============================================================
# LIVE DASHBOARD
# ============================================================

st.markdown("---")
st.markdown("## 📊 LIVE EVENT DASHBOARD")

a, b, c, d = st.columns(4)

with a:
    st.metric("Total VIP Passes", len(VALID_VIP_PASSES))

with b:
    st.metric("Verified Entries", len(st.session_state.verified))

with c:
    st.metric("Special Guest Passes", len(SPECIAL_GUEST_PASSES))

with d:
    st.metric(
        "Remaining Passes",
        len(VALID_VIP_PASSES) - len(st.session_state.verified),
    )

# ============================================================
# LOG
# ============================================================

if st.session_state.logs:

    st.markdown("## 📋 SECURITY ENTRY LOG")

    st.dataframe(
        list(reversed(st.session_state.logs)),
        use_container_width=True,
        hide_index=True,
    )

# ============================================================
# RESET
# ============================================================

if st.session_state.verified:

    if st.button("🔄 RESET EVENT SECURITY"):

        st.session_state.verified.clear()
        st.session_state.logs.clear()

        st.rerun()

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🎬 Rajamouli Movie Pre-Release Event<br><br>
        Security → VIP Pass → Special Guest → Front Row Decision<br><br>
        © Learn Build Share
    </div>
    """,
    unsafe_allow_html=True,
)

