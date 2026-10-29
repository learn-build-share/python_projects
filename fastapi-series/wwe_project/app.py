
import requests
import streamlit as st
import pandas as pd

# ---------------- CONFIGURATION ----------------
API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="WWE Universe | Player Hub",
    page_icon="🥊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM UI ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(168, 85, 247, 0.20), transparent 28%),
        radial-gradient(circle at bottom right, rgba(251, 146, 60, 0.18), transparent 30%),
        linear-gradient(135deg, #030712 0%, #0b1020 45%, #151827 100%);
    color: #f8fafc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1020 0%, #111827 100%);
    border-right: 1px solid rgba(148, 163, 184, 0.2);
}

.hero {
    padding: 30px;
    border-radius: 22px;
    background: linear-gradient(120deg, rgba(124, 58, 237, 0.25), rgba(15, 23, 42, 0.95) 62%, rgba(30, 41, 59, 0.85));
    border: 1px solid rgba(167, 139, 250, 0.28);
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.35);
    margin-bottom: 24px;
}

.hero h1 {
    font-size: 38px;
    font-weight: 800;
    margin: 0;
    color: #f8fafc;
}

.hero p {
    color: #cbd5e1;
    font-size: 15px;
    margin-bottom: 0;
}

.section-title {
    font-size: 22px;
    font-weight: 800;
    margin: 20px 0 14px;
    color: #f8fafc;
}

.player-card {
    background: linear-gradient(145deg, rgba(18, 24, 38, 0.96), rgba(8, 12, 23, 0.98));
    padding: 22px;
    border: 1px solid rgba(148, 163, 184, 0.28);
    border-radius: 18px;
    margin-bottom: 12px;
    min-height: 210px;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.28);
}

.player-card h3 {
    margin: 8px 0 4px;
    font-size: 21px;
    color: #ffffff;
}

.nickname {
    color: #a5b4cf;
    font-size: 13px;
}

.brand-tag {
    display: inline-block;
    padding: 6px 10px;
    background: linear-gradient(135deg, #f59e0b, #f97316);
    color: #1f2937;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 800;
}

.stat-number {
    font-size: 27px;
    font-weight: 800;
    color: #fbbf24;
}

.stat-label {
    color: #cbd5e1;
    font-size: 12px;
}

div.stButton > button {
    border-radius: 10px;
    font-weight: 700;
    min-height: 42px;
    border: 1px solid #f59e0b;
    background: linear-gradient(135deg, #f59e0b, #f97316);
    color: #111827;
    transition: 0.2s;
}

div.stButton > button:hover {
    border-color: #fcd34d;
    color: #111827;
    box-shadow: 0 12px 20px rgba(245, 158, 11, 0.25);
}

div[data-testid="stForm"] {
    background: rgba(17, 24, 39, 0.95);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 10px 18px rgba(15, 23, 42, 0.18);
}

div[data-testid="stMetric"] {
    background: rgba(17, 24, 39, 0.88);
    border: 1px solid rgba(148, 163, 184, 0.18);
    padding: 18px;
    border-radius: 14px;
}

hr {
    border-color: rgba(148, 163, 184, 0.2);
}
</style>
""", unsafe_allow_html=True)


# ---------------- API HELPERS ----------------
def api_get(endpoint, params=None):
    try:
        response = requests.get(
            f"{API_URL}{endpoint}",
            params=params,
            timeout=5
        )
        
        return response.json() if response.status_code == 200 else None
    except requests.RequestException as exc:
        st.error(f"Could not connect to FastAPI: {exc}")
        return None


def api_post(endpoint, payload):
    try:
        response = requests.post(
            f"{API_URL}{endpoint}",
            json=payload,
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        try:
            detail = response.json().get("detail", str(exc))
        except (ValueError, UnboundLocalError):
            detail = str(exc)

        st.error(f"Request failed: {detail}")
        return None


def api_patch(endpoint, payload):
    try:
        response = requests.patch(
            f"{API_URL}{endpoint}",
            json=payload,
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        try:
            detail = response.json().get("detail", str(exc))
        except (ValueError, UnboundLocalError):
            detail = str(exc)

        st.error(f"Update failed: {detail}")
        return None


def api_delete(endpoint):
    try:
        response = requests.delete(
            f"{API_URL}{endpoint}",
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        try:
            detail = response.json().get("detail", str(exc))
        except (ValueError, UnboundLocalError):
            detail = str(exc)

        st.error(f"Delete failed: {detail}")
        return None


def refresh_data():
    st.session_state.refresh += 1


if "refresh" not in st.session_state:
    st.session_state.refresh = 0


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 🥊 WWE UNIVERSE")
    st.caption("PLAYER MANAGEMENT HUB")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Dashboard",
            "🔎 Explore Players",
            "➕ Add Player",
            "📊 Manage Stats",
            "🏆 Match Records"
        ]
    )

    st.divider()
    st.caption("Built with Python + FastAPI + Streamlit")


# ---------------- LOAD DATA ----------------
all_players = api_get("/players") or []

player_by_id = {
    player["id"]: player for player in all_players
}


# ---------------- HERO HEADER ----------------
st.markdown("""
<div class="hero">
    <h1>🥊 WWE PLAYER HUB</h1>
    <p>Your fan-made wrestling database. Explore player profiles,
    championships, career stats and match records.</p>
</div>
""", unsafe_allow_html=True)


# ---------------- DASHBOARD ----------------
if page == "🏠 Dashboard":

    total_players = len(all_players)
    total_titles = sum(p["championships"] for p in all_players)
    total_wins = sum(p["wins"] for p in all_players)
    total_matches = sum(len(p["matches"]) for p in all_players)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Players", total_players)
    col2.metric("🏆 Championships", total_titles)
    col3.metric("🔥 Career Wins", total_wins)
    col4.metric("📋 Recorded Matches", total_matches)

    st.markdown('<div class="section-title">⭐ Featured Superstars</div>',
                unsafe_allow_html=True)

    if not all_players:
        st.info("No players available. Add your first player!")
    else:
        cols = st.columns(3)

        for index, player in enumerate(all_players):
            with cols[index % 3]:
                st.markdown(f"""
                <div class="player-card">
                    <span class="brand-tag">{player['brand']}</span>
                    <h3>{player['name']}</h3>
                    <div class="nickname">{player['nickname']}</div>
                    <hr>
                    <div style="display:flex;justify-content:space-between;">
                        <div>
                            <div class="stat-number">{player['championships']}</div>
                            <div class="stat-label">TITLES</div>
                        </div>
                        <div>
                            <div class="stat-number">{player['wins']}</div>
                            <div class="stat-label">WINS</div>
                        </div>
                        <div>
                            <div class="stat-number">{len(player['matches'])}</div>
                            <div class="stat-label">RECORDS</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button(
                    f"View Profile · {player['name']}",
                    key=f"profile_{player['id']}",
                    use_container_width=True
                ):
                    st.session_state.selected_player = player["id"]
                    st.session_state.open_profile = True
                    st.rerun()

    # Profile details opened from a dashboard card
    if st.session_state.get("open_profile"):
        selected_id = st.session_state.get("selected_player")
        profile = api_get(f"/players/{selected_id}")

        if profile:
            st.divider()
            st.subheader(f"📌 {profile['name']} — Complete Profile")
            st.json(profile)

            if st.button("Close Profile"):
                st.session_state.open_profile = False
                st.rerun()


# ---------------- EXPLORE PLAYERS ----------------
elif page == "🔎 Explore Players":

    st.subheader("🔎 Find Your Superstar")

    search_name = st.text_input(
        "Search by player name",
        placeholder="Try John Cena..."
    )

    if search_name.strip():
        results = api_get(
            "/players/search",
            params={"name": search_name.strip()}
        )
        results = results if isinstance(results, list) else []
    else:
        results = all_players

    if not results:
        st.info("No matching players found.")
    else:
        for player in results:
            with st.expander(
                f"🥊 {player['name']} · {player['nickname']}"
            ):
                left, right = st.columns([1, 2])

                with left:
                    st.metric("Championships", player["championships"])
                    st.metric("Career Wins", player["wins"])
                    st.metric("Career Losses", player["losses"])

                with right:
                    st.markdown(f"**Brand:** {player['brand']}")
                    st.markdown("**Match History**")

                    if player["matches"]:
                        st.dataframe(
                            pd.DataFrame(player["matches"]),
                            use_container_width=True,
                            hide_index=True
                        )
                    else:
                        st.info("No match records added yet.")

                    st.download_button(
                        "⬇️ Download Player Profile",
                        data=pd.Series(player).to_json(indent=2),
                        file_name=f"player_{player['id']}.json",
                        mime="application/json",
                        key=f"download_{player['id']}"
                    )


# ---------------- ADD PLAYER ----------------
elif page == "➕ Add Player":

    st.subheader("➕ Sign a New Superstar")
    st.caption("Add a player to your demo WWE database.")

    with st.form("add_player_form"):
        name = st.text_input("Player Name", placeholder="e.g. Seth Rollins")
        nickname = st.text_input(
            "Nickname",
            placeholder="e.g. The Visionary"
        )
        brand = st.selectbox(
            "Brand",
            ["Raw", "SmackDown", "NXT", "Free Agent"]
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            championships = st.number_input(
                "Championships", min_value=0, value=0, step=1
            )
        with col2:
            wins = st.number_input(
                "Career Wins", min_value=0, value=0, step=1
            )
        with col3:
            losses = st.number_input(
                "Career Losses", min_value=0, value=0, step=1
            )

        submitted = st.form_submit_button(
            "🔥 Add Superstar",
            use_container_width=True
        )

        if submitted:
            if not name.strip() or not nickname.strip():
                st.warning("Please enter both the player name and nickname.")
            else:
                result = api_post(
                    "/players",
                    {
                        "name": name.strip(),
                        "nickname": nickname.strip(),
                        "brand": brand,
                        "championships": int(championships),
                        "wins": int(wins),
                        "losses": int(losses)
                    }
                )

                if result:
                    st.success(result["message"])
                    st.json(result["player"])
                    refresh_data()


# ---------------- MANAGE STATS ----------------
elif page == "📊 Manage Stats":

    st.subheader("📊 Update Superstar Stats")

    if not all_players:
        st.info("Add a player before updating stats.")
    else:
        player_options = {
            f"{p['name']} (ID: {p['id']})": p["id"]
            for p in all_players
        }

        selected_label = st.selectbox(
            "Select Player",
            list(player_options.keys())
        )
        selected_id = player_options[selected_label]
        selected_player = player_by_id[selected_id]

        st.info(
            f"Current stats: {selected_player['championships']} titles · "
            f"{selected_player['wins']} wins · "
            f"{selected_player['losses']} losses"
        )

        with st.form("update_stats_form"):
            nickname = st.text_input(
                "Nickname",
                value=selected_player["nickname"]
            )
            brand = st.selectbox(
                "Brand",
                ["Raw", "SmackDown", "NXT", "Free Agent"],
                index=(
                    ["Raw", "SmackDown", "NXT", "Free Agent"].index(
                        selected_player["brand"]
                    )
                    if selected_player["brand"] in
                    ["Raw", "SmackDown", "NXT", "Free Agent"]
                    else 0
                )
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                championships = st.number_input(
                    "Championships",
                    min_value=0,
                    value=int(selected_player["championships"]),
                    step=1
                )
            with col2:
                wins = st.number_input(
                    "Wins",
                    min_value=0,
                    value=int(selected_player["wins"]),
                    step=1
                )
            with col3:
                losses = st.number_input(
                    "Losses",
                    min_value=0,
                    value=int(selected_player["losses"]),
                    step=1
                )

            update_clicked = st.form_submit_button(
                "💾 Save Changes",
                use_container_width=True
            )

            if update_clicked:
                result = api_patch(
                    f"/players/{selected_id}",
                    {
                        "nickname": nickname,
                        "brand": brand,
                        "championships": int(championships),
                        "wins": int(wins),
                        "losses": int(losses)
                    }
                )

                if result:
                    st.success(result["message"])
                    refresh_data()


# ---------------- MATCH RECORDS ----------------
elif page == "🏆 Match Records":

    st.subheader("🏆 Match Record Center")

    if not all_players:
        st.info("Add a player before recording matches.")
    else:
        player_options = {
            f"{p['name']} (ID: {p['id']})": p["id"]
            for p in all_players
        }

        selected_label = st.selectbox(
            "Select Superstar",
            list(player_options.keys()),
            key="match_player"
        )
        selected_id = player_options[selected_label]
        selected_player = player_by_id[selected_id]

        st.markdown(f"### 🥊 {selected_player['name']}")

        tab1, tab2 = st.tabs(["➕ Add Match", "📜 Match History"])

        with tab1:
            with st.form("add_match_form"):
                opponent = st.text_input(
                    "Opponent",
                    placeholder="e.g. Randy Orton"
                )
                event = st.text_input(
                    "Event",
                    placeholder="e.g. SummerSlam"
                )
                result_value = st.selectbox(
                    "Match Result",
                    ["Win", "Loss", "Draw", "No Contest"]
                )

                match_submitted = st.form_submit_button(
                    "🏆 Save Match Record",
                    use_container_width=True
                )

                if match_submitted:
                    if not opponent.strip() or not event.strip():
                        st.warning("Please enter both opponent and event.")
                    else:
                        result = api_post(
                            f"/players/{selected_id}/matches",
                            {
                                "opponent": opponent.strip(),
                                "event": event.strip(),
                                "result": result_value
                            }
                        )

                        if result:
                            st.success(result["message"])
                            refresh_data()

        with tab2:
            history = api_get(
                f"/players/{selected_id}/matches"
            )

            if history:
                st.dataframe(
                    pd.DataFrame(history),
                    use_container_width=True,
                    hide_index=True
                )
            elif history is not None:
                st.info("No match records available for this player.")


# ---------------- FOOTER ----------------
st.divider()
st.caption(
    "WWE Player Hub · Educational fan project · "
    "Python + FastAPI (Learn Build Share)"
)
