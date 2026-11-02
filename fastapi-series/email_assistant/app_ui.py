
import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Email Assistant",
    page_icon="📧"
)

st.title("📧 AI Email Assistant")
st.caption("Secure Email Management")


# Initialize session
if "token" not in st.session_state:
    st.session_state.token = None


# LOGIN PAGE
if st.session_state.token is None:

    st.subheader("🔐 Login")

    with st.form("login"):

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        login_button = st.form_submit_button("Login")

    if login_button:

        try:
            response = requests.post(
                f"{API_URL}/token",
                data={
                    "username": username,
                    "password": password
                },
                timeout=10
            )

            if response.status_code == 200:

                st.session_state.token = (
                    response.json()["access_token"]
                )

                st.success("Login successful!")
                st.rerun()

            else:
                st.error("Invalid username or password")

        except requests.RequestException:
            st.error("Unable to connect to FastAPI backend")


# DASHBOARD
else:

    headers = {
        "Authorization": (
            f"Bearer {st.session_state.token}"
        )
    }

    try:
        response = requests.get(
            f"{API_URL}/me",
            headers=headers,
            timeout=10
        )

    except requests.RequestException:
        st.error("Backend connection failed")
        st.stop()

    if response.status_code == 401:

        st.session_state.token = None
        st.warning("Session expired. Please login again.")
        st.rerun()

    elif response.status_code != 200:

        st.error("Unable to load user profile")
        st.stop()

    else:

        user = response.json()
        permissions = user["permissions"]

        st.success(f"Welcome, {user['username']}!")

        st.subheader("👤 User Information")

        st.write("Username:", user["username"])
        st.write("Permissions:", permissions)

        if st.button("Logout"):
            st.session_state.token = None
            st.rerun()

        st.divider()

        # READ EMAILS
        st.subheader("📥 Inbox")

        if st.button("Load Emails"):

            response = requests.get(
                f"{API_URL}/emails",
                headers=headers,
                timeout=10
            )

            if response.status_code == 200:

                emails = response.json()["emails"]

                for email in emails:

                    with st.expander(email["subject"]):

                        st.write("From:", email["sender"])
                        st.write(email["message"])

            elif response.status_code == 403:
                st.error("You don't have permission to read emails.")

            elif response.status_code == 401:
                st.error("Session expired. Please login again.")

            else:
                st.error("Unable to load emails")

        st.divider()

        # SEND EMAIL
        st.subheader("✉️ Compose Email")

        recipient = st.text_input("Recipient")
        subject = st.text_input("Subject")
        message = st.text_area("Message")

        if st.button("Send Email"):

            response = requests.post(
                f"{API_URL}/emails/send",
                headers=headers,
                json={
                    "recipient": recipient,
                    "subject": subject,
                    "message": message
                },
                timeout=10
            )

            if response.status_code == 200:
                st.success("Email sent successfully!")

            elif response.status_code == 403:
                st.error(
                    "403 Forbidden: You don't have permission to send emails."
                )

            elif response.status_code == 401:
                st.error("Session expired. Please login again.")

            else:
                st.error("Unable to send email")
