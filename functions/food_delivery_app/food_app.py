"""
Made by Learn Build Share

This example demonstrates how functions work by separating
each task into its own reusable function with food delivery App.
"""
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Learn Build Share - Food Delivery",
    page_icon="🍔",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.stApp{
    background:#f8f8f8;
}

.hero{
    background:linear-gradient(135deg,#FC8019,#ff9f43);
    padding:30px;
    border-radius:20px;
    color:white;
    text-align:center;
}

.food-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,.1);
    text-align:center;
    margin-bottom:20px;
}

.price{
    font-size:22px;
    color:#FC8019;
    font-weight:bold;
}

.title{
    color:#282C3F;
    font-size:24px;
    font-weight:bold;
}

.small{
    color:gray;
}

.bill{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,.1);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Functions
# -----------------------------
def login(name):
    return f"👋 Welcome {name}"


def show_menu():
    return {
        "🍕 Veg Pizza": 199,
        "🍔 Burger": 149,
        "🍗 Chicken Biryani": 249,
        "🥪 Sandwich": 129,
        "🌮 Wrap": 159,
        "🥤 Cold Drink": 49,
        "🍟 French Fries": 99,
        "🥘 Dosa": 119
    }


def take_order(item, price):
    st.session_state.cart.append((item, price))
    st.toast(f"{item} Added")


def calculate_bill():
    subtotal = sum(price for _, price in st.session_state.cart)
    gst = subtotal * 0.05

    if subtotal > 0:
        delivery = 40
    else:
        delivery = 0

    total = subtotal + gst + delivery

    return subtotal, gst, delivery, total


def show_invoice():
    subtotal, gst, delivery, total = calculate_bill()

    st.success("🎉 Order Placed Successfully!")

    st.balloons()

    st.markdown("### 🧾 Invoice")

    for item, price in st.session_state.cart:
        st.write(f"✅ {item} - ₹{price}")

    st.divider()

    st.write(f"Subtotal : ₹{subtotal:.2f}")
    st.write(f"GST (5%) : ₹{gst:.2f}")
    st.write(f"Delivery : ₹{delivery:.2f}")

    st.markdown(f"## Grand Total : ₹{total:.2f}")

# -----------------------------
# Session State
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "name" not in st.session_state:
    st.session_state.name = ""

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class='hero'>
<h1>🍔 Learn Build Share</h1>
<h3>Food Delivery App</h3>
<p>Python Functions Explanations</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------
# Login
# -----------------------------
if not st.session_state.logged_in:

    st.subheader("🔐 Login")

    name = st.text_input("Enter Your Name")

    phone = st.text_input("Phone Number")

    if st.button("Login", use_container_width=True):

        if name and phone:

            st.session_state.logged_in = True
            st.session_state.name = name

            st.success(login(name))

            st.rerun()

        else:
            st.error("Please fill all fields.")

# -----------------------------
# Main App
# -----------------------------
else:

    st.success(login(st.session_state.name))

    menu = show_menu()

    st.write("## 🍽️ Today's Menu")

    cols = st.columns(4)

    index = 0

    for item, price in menu.items():

        with cols[index]:

            st.markdown(
                f"""
                <div class='food-card'>
                <h2>{item}</h2>
                <p class='small'>Fresh & Delicious</p>
                <p class='price'>₹{price}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button("Add", key=item):
                take_order(item, price)

        index += 1

        if index == 4:
            cols = st.columns(4)
            index = 0

    # -----------------------------
    # Sidebar Cart
    # -----------------------------
    with st.sidebar:

        st.title("🛒 Your Cart")

        if len(st.session_state.cart) == 0:

            st.info("No Items Added")

        else:

            subtotal, gst, delivery, total = calculate_bill()

            for item, price in st.session_state.cart:
                st.write(f"✅ {item}")
                st.write(f"₹{price}")
                st.divider()

            st.metric("Subtotal", f"₹{subtotal:.2f}")
            st.metric("GST", f"₹{gst:.2f}")
            st.metric("Delivery", f"₹{delivery:.2f}")

            st.success(f"Total : ₹{total:.2f}")

            st.progress(100)

            if st.button("🚀 Place Order", use_container_width=True):
                show_invoice()

            if st.button("🗑️ Clear Cart", use_container_width=True):
                st.session_state.cart = []
                st.rerun()