import re
import streamlit as st


# -----------------------------
# Password Validation Functions
# -----------------------------

def check_password_length(password: str) -> bool:
    """Check whether password contains at least 8 characters."""
    return len(password) >= 8


def check_special_character(password: str) -> bool:
    """Check whether password contains at least one special character."""
    return bool(re.search(r"[^A-Za-z0-9]", password))


def check_number(password: str) -> bool:
    """Check whether password contains at least one number."""
    return bool(re.search(r"\d", password))


def validate_password(password: str) -> dict:
    """Run all password validation checks."""

    return {
        "length": check_password_length(password),
        "special": check_special_character(password),
        "number": check_number(password),
    }


# -----------------------------
# Streamlit UI
# -----------------------------

st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered",
)

st.title("🔐 Password Strength Checker")
st.write("Enter a password to check its strength.")

st.divider()

password = st.text_input(
    "Enter Password",
    type="password",
    placeholder="Enter your password..."
)


if password:

    results = validate_password(password)

    st.subheader("🔍 Password Validation")

    # Password Length
    if results["length"]:
        st.success("✅ Password Length: Valid (8+ characters)")
    else:
        st.error("❌ Password Length: Invalid (Minimum 8 characters)")

    # Special Character
    if results["special"]:
        st.success("✅ Special Character: FOUND")
    else:
        st.error("❌ Special Character: NOT FOUND")

    # Number
    if results["number"]:
        st.success("✅ Number: FOUND")
    else:
        st.error("❌ Number: NOT FOUND")

    st.divider()

    # Final validation
    if all(results.values()):
        st.success("🎉 Password is VALID and STRONG!")
    else:
        st.warning("⚠️ Password is NOT VALID. Please fix the requirements above.")

else:
    st.info("👆 Please enter a password to check.")

