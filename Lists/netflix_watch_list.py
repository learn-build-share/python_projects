import streamlit as st

st.set_page_config(
    page_title="Netflix Watchlist - Python Lists",
    page_icon="🍿",
    layout="wide"
)

st.title("🍿 Netflix Watchlist")
st.subheader("Python Lists Mini Project made by © Learn Build Share")

if "watchlist" not in st.session_state:
    st.session_state.watchlist = [
        "Interstellar",
        "Inception",
        "Avengers"
    ]

watchlist = st.session_state.watchlist

left, right = st.columns([1,1])

with left:

    st.header("🎬 Perform Operations")

    movie = st.text_input("Movie Name")

    c1,c2,c3 = st.columns(3)

    with c1:
        if st.button("➕ Add Movie"):
            if movie:
                watchlist.append(movie)
                st.success(f'{movie} Added')
                st.code(f'watchlist.append("{movie}")')

    with c2:
        if st.button("🗑 Remove"):
            if movie in watchlist:
                watchlist.remove(movie)
                st.success(f'{movie} Removed')
                st.code(f'watchlist.remove("{movie}")')
            else:
                st.warning("Movie not found")

    position = st.number_input(
        "Insert Position",
        0,
        len(watchlist),
        0
    )

    if st.button("📍 Insert Movie"):
        if movie:
            watchlist.insert(position, movie)
            st.success("Movie Inserted")
            st.code(f'watchlist.insert({position},"{movie}")')

with right:

    st.header("📺 Your Watchlist")

    for i,movie in enumerate(watchlist,start=1):
        st.markdown(f"**{i}. {movie}**")

    st.divider()

    st.subheader("📦 Current Python List")

    st.code(watchlist)

    st.metric("Length", len(watchlist))

st.divider()

st.header("🔁 For Loop Traversal")

code = """for movie in watchlist:
    print(movie)"""

st.code(code,language="python")

for movie in watchlist:
    st.write("🎥",movie)

st.divider()

st.header("💡 Why List?")

st.success("""
✔ Ordered

✔ Mutable

✔ Add Items

✔ Remove Items

✔ Update Items

✔ Best for Dynamic Data
""")