import random
import time
import streamlit as st

# Copyright (c) LearnBuildShare
# Simple OTP verification example using Python Tuple


def generate_otp():
    otp = random.randint(100000, 999999)
    return otp, (otp,)


def verify_otp(entered_otp, stored_otp):
    if entered_otp == "":
        return False, "Please enter the OTP before verifying."
    if entered_otp == str(stored_otp):
        return True, "OTP verified successfully."
    return False, "Incorrect OTP. Please try again."


st.set_page_config(page_title="OTP Verification", page_icon="🔐", layout="centered")
st.title("🔐 OTP Verification")
st.write("This app shows how an OTP can be stored safely inside a Python tuple.")


if "otp" not in st.session_state:
    st.session_state.otp = None
if "otp_created_at" not in st.session_state:
    st.session_state.otp_created_at = None
if "verified" not in st.session_state:
    st.session_state.verified = False
if "message" not in st.session_state:
    st.session_state.message = ""


def start_new_otp():
    otp, otp_tuple = generate_otp()
    st.session_state.otp = otp
    st.session_state.otp_created_at = time.time()
    st.session_state.verified = False
    st.session_state.message = ""


if st.session_state.otp is None or st.session_state.otp_created_at is None:
    start_new_otp()

remaining = int((st.session_state.otp_created_at + 60) - time.time())
remaining = max(0, remaining)

if remaining <= 0:
    st.session_state.message = "OTP expired. Please generate a new one."
    st.warning(st.session_state.message)
    start_new_otp()
    remaining = 60

st.info(f"Generated OTP: {st.session_state.otp}")
st.caption(f"OTP expires in {remaining} seconds")

otp_value = st.text_input("Enter the OTP", max_chars=6, key="otp_input", type="password")

col1, col2 = st.columns(2)
with col1:
    if st.button("Verify OTP"):
        if otp_value == "":
            st.session_state.message = "Please enter the OTP before verifying."
            st.warning(st.session_state.message)
        elif remaining <= 0:
            st.session_state.message = "OTP expired. Please generate a new one."
            st.error(st.session_state.message)
        else:
            is_valid, message = verify_otp(otp_value, st.session_state.otp)
            st.session_state.message = message
            if is_valid:
                st.session_state.verified = True
                st.success(message)
            else:
                st.error(message)

with col2:
    if st.button("Generate New OTP"):
        start_new_otp()
        st.success("New OTP created. Please verify again.")

if st.session_state.verified:
    st.success("Verification complete. The OTP was checked safely.")
