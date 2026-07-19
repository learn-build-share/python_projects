"""
Made by Learn Build Share
Instagram Followers Cleaner - production-quality Streamlit dashboard.

This file contains the complete front-end experience for an Instagram-inspired
followers cleanup workflow. It includes demo data loading, CSV upload handling,
duplicate detection, analytics, cleaning actions, reporting, and downloads.
"""

from __future__ import annotations

import io
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Instagram Followers Cleaner",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded",
)


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
DEMO_DATA_PATH = DATA_DIR / "demo_followers.csv"


def load_css() -> None:
    """Injects the app's custom dashboard styling."""
    css = """
    <style>
    :root {
        color-scheme: dark;
        --bg: #060816;
        --card: rgba(15, 23, 42, 0.78);
        --card-2: rgba(30, 41, 59, 0.72);
        --line: rgba(255,255,255,0.12);
        --text: #f8fafc;
        --muted: #94a3b8;
        --accent: #8b5cf6;
        --accent-2: #ec4899;
        --accent-3: #fb923c;
    }
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, rgba(139,92,246,0.18) 0%, transparent 38%),
                    radial-gradient(circle at top right, rgba(236,72,153,0.16) 0%, transparent 35%),
                    linear-gradient(135deg, #060816 0%, #111827 48%, #0f172a 100%);
        color: var(--text);
    }
    [data-testid="stSidebar"] {
        background: rgba(2, 6, 23, 0.8);
        border-right: 1px solid var(--line);
        backdrop-filter: blur(20px);
    }
    .hero-card {
        padding: 22px 24px;
        border-radius: 24px;
        background: linear-gradient(135deg, rgba(139,92,246,0.24), rgba(236,72,153,0.24), rgba(251,146,60,0.24));
        border: 1px solid rgba(255,255,255,0.16);
        box-shadow: 0 18px 45px rgba(0,0,0,0.25);
        margin-bottom: 18px;
        animation: floatIn 0.8s ease;
    }
    .hero-card h1 {
        font-size: 2.25rem;
        margin: 0.2rem 0 0.4rem;
        font-weight: 800;
        letter-spacing: -0.03em;
    }
    .hero-card p {
        color: #e2e8f0;
        margin: 0;
        font-size: 1rem;
    }
    .pill {
        display: inline-block;
        padding: 0.4rem 0.75rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.14);
        color: #f8fafc;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.45rem;
    }
    .metric-card {
        padding: 18px 20px;
        border-radius: 20px;
        background: linear-gradient(145deg, rgba(15,23,42,0.82), rgba(30,41,59,0.72));
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 12px 30px rgba(0,0,0,0.16);
        backdrop-filter: blur(16px);
        transition: transform 180ms ease, box-shadow 180ms ease;
    }
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 14px 34px rgba(0,0,0,0.24);
    }
    .metric-card .value {
        font-size: 1.4rem;
        font-weight: 800;
        margin-top: 0.4rem;
    }
    .metric-card .label {
        color: var(--muted);
        font-size: 0.9rem;
        font-weight: 600;
    }
    .glass-card {
        padding: 18px;
        border-radius: 22px;
        background: rgba(15,23,42,0.74);
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 12px 30px rgba(0,0,0,0.2);
        backdrop-filter: blur(18px);
    }
    .stButton > button {
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-2) 100%);
        color: white;
        border: 0;
        border-radius: 999px;
        padding: 0.65rem 1.2rem;
        font-weight: 700;
        transition: all 180ms ease;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 10px 24px rgba(236,72,153,0.24);
    }
    .big-button > button {
        width: 100%;
        padding: 0.9rem 1.2rem;
        font-size: 1rem;
        animation: pulse 1.7s infinite;
    }
    .sidebar .block-container {
        padding-top: 1rem;
    }
    .footer {
        margin-top: 1.4rem;
        text-align: center;
        color: var(--muted);
        font-size: 0.92rem;
        letter-spacing: 0.02em;
    }
    @keyframes floatIn {
        from { transform: translateY(10px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.01); }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def load_demo_data() -> pd.DataFrame:
    """Loads demo follower data from disk or creates realistic in-memory data."""
    if DEMO_DATA_PATH.exists():
        try:
            return pd.read_csv(DEMO_DATA_PATH)
        except Exception:
            st.warning("Demo CSV could not be read. Creating a fallback sample dataset.")

    np.random.seed(7)
    usernames = [
        "alex.morgan",
        "sophia_lee",
        "mariah.dev",
        "david.chen",
        "nina.khan",
        "james.wilson",
        "olivia.turner",
        "noah.hall",
        "mia.rodriguez",
        "liam.smith",
        "ava.garcia",
        "ethan.brown",
        "isabella.moore",
        "logan.davis",
        "amelia.jackson",
        "lucas.white",
        "charlotte.harris",
        "henry.martin",
        "harper.thompson",
        "jackson.gonzalez",
    ]
    rows: List[Dict[str, object]] = []
    for index in range(320):
        username = np.random.choice(usernames)
        rows.append(
            {
                "username": username,
                "full_name": f"{username.replace('.', ' ').title()}",
                "followers_count": int(np.random.randint(1000, 30000)),
                "engagement_rate": round(float(np.random.uniform(1.5, 6.8)), 2),
                "source": np.random.choice(["organic", "referred", "paid"], p=[0.7, 0.2, 0.1]),
            }
        )
    df = pd.DataFrame(rows)
    return df


def detect_username_column(df: pd.DataFrame) -> Optional[str]:
    """Finds the most likely username column from a CSV dataframe."""
    candidates = [
        "username",
        "Username",
        "user",
        "User",
        "followers",
        "instagram_username",
        "account",
    ]
    normalized_columns = {col.lower(): col for col in df.columns}
    for candidate in candidates:
        if candidate.lower() in normalized_columns:
            return normalized_columns[candidate.lower()]
    for column in df.columns:
        if "user" in str(column).lower() or "name" in str(column).lower():
            return column
    return None


def find_duplicates(df: pd.DataFrame, username_col: str) -> pd.DataFrame:
    """Builds a summary table of duplicated usernames and counts."""
    if df.empty or username_col not in df.columns:
        return pd.DataFrame(columns=["Username", "Occurrences"])
    normalized = df[username_col].fillna("").astype(str).str.strip().str.lower()
    counts = normalized.value_counts()
    duplicates = counts[counts > 1].sort_values(ascending=False)
    return pd.DataFrame({"Username": duplicates.index, "Occurrences": duplicates.values}).reset_index(drop=True)


def remove_duplicates(df: pd.DataFrame, username_col: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Removes duplicate followers using Python set logic and returns clean and duplicate datasets."""
    if df.empty or username_col not in df.columns:
        return df.copy(), pd.DataFrame(columns=df.columns)

    seen: set[str] = set()
    clean_rows: List[Dict[str, object]] = []
    duplicate_rows: List[Dict[str, object]] = []
    for _, row in df.iterrows():
        username_value = str(row[username_col]).strip().lower() if pd.notna(row[username_col]) else ""
        if username_value in seen:
            duplicate_rows.append(row.to_dict())
        else:
            seen.add(username_value)
            clean_rows.append(row.to_dict())
    clean_df = pd.DataFrame(clean_rows, columns=df.columns)
    duplicate_df = pd.DataFrame(duplicate_rows, columns=df.columns)
    return clean_df, duplicate_df


def generate_report(df: pd.DataFrame, clean_df: pd.DataFrame, duplicate_df: pd.DataFrame, username_col: str) -> str:
    """Creates a text report summarizing the duplicate-cleaning results."""
    duplicates = len(df) - len(clean_df)
    duplicates_pct = round((duplicates / len(df) * 100), 2) if len(df) else 0.0
    top_duplicates = find_duplicates(df, username_col).head(10)
    top_lines = []
    for _, row in top_duplicates.iterrows():
        top_lines.append(f"- {row['Username']}: {row['Occurrences']} occurrences")
    report = []
    report.append("Instagram Followers Cleaning Report")
    report.append("=" * 36)
    report.append(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    report.append(f"Time: {datetime.now().strftime('%H:%M:%S')}")
    report.append(f"Rows: {len(df)}")
    report.append(f"Duplicates: {duplicates}")
    report.append(f"Unique: {len(clean_df)}")
    report.append("Top duplicates:")
    report.extend(top_lines or ["- None"])
    report.append(f"Duplicate %: {duplicates_pct}%")
    return "\n".join(report)


def summary_statistics(df: pd.DataFrame, clean_df: pd.DataFrame, duplicate_df: pd.DataFrame, username_col: str) -> Dict[str, object]:
    """Builds a dictionary of cleanup metrics for cards and summaries."""
    duplicate_count = len(duplicate_df)
    most_repeated = "None"
    most_count = 0
    if not df.empty and username_col in df.columns:
        counts = df[username_col].fillna("").astype(str).str.strip().str.lower().value_counts()
        if not counts.empty:
            most_repeated = counts.index[0]
            most_count = int(counts.iloc[0])
    return {
        "original_rows": int(len(df)),
        "duplicates_removed": int(duplicate_count),
        "final_rows": int(len(clean_df)),
        "most_repeated_username": str(most_repeated),
        "most_repeated_count": int(most_count),
    }


def create_pie_chart(df: pd.DataFrame, clean_df: pd.DataFrame) -> px.pie:
    """Returns the pie chart showing unique versus duplicate follower counts."""
    labels = ["Unique", "Duplicates"]
    values = [len(clean_df), max(len(df) - len(clean_df), 0)]
    fig = px.pie(
        values=values,
        names=labels,
        color=labels,
        color_discrete_map={"Unique": "#8b5cf6", "Duplicates": "#fb923c"},
    )
    fig.update_traces(textinfo="percent+value", hole=0.55)
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig


def create_bar_chart(df: pd.DataFrame, username_col: str) -> px.bar:
    """Returns a bar chart of the top duplicated usernames."""
    duplicate_summary = find_duplicates(df, username_col).head(15)
    fig = px.bar(
        duplicate_summary,
        x="Username",
        y="Occurrences",
        color="Occurrences",
        color_continuous_scale=px.colors.sequential.Magma,
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


def highlight_duplicate_rows(df: pd.DataFrame, username_col: str):
    """Highlights duplicate rows with a light red background in a dataframe."""
    if df.empty or username_col not in df.columns:
        return df

    counts = df[username_col].fillna("").astype(str).str.strip().str.lower().value_counts()
    duplicate_usernames = set(counts[counts > 1].index)

    def style_rows(row):
        username = str(row[username_col]).strip().lower()
        return ["background-color: #ffe4e6; color: #7f1d1d;" if username in duplicate_usernames else ""] * len(row)

    return df.style.apply(style_rows, axis=1)


def render_metric_card(title: str, value: str | int, subtitle: str, accent: str) -> None:
    """Renders a polished stat card using custom HTML."""
    st.markdown(
        f"""
        <div class="metric-card" style="border-top: 4px solid {accent};">
            <div class="label">{title}</div>
            <div class="value">{value}</div>
            <div class="label" style="margin-top: 0.3rem;">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def initialize_session_state() -> None:
    """Initializes Streamlit session variables for app state."""
    defaults = {
        "data_loaded": False,
        "df": pd.DataFrame(),
        "clean_df": pd.DataFrame(),
        "duplicate_df": pd.DataFrame(),
        "username_col": None,
        "dark_mode": True,
        "active_page": "Home",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def set_data_state(df: pd.DataFrame, username_col: str | None) -> None:
    """Stores the loaded dataframe and derived data in session state."""
    st.session_state.df = df.copy()
    st.session_state.username_col = username_col
    st.session_state.data_loaded = True
    st.session_state.clean_df = pd.DataFrame(columns=df.columns)
    st.session_state.duplicate_df = pd.DataFrame(columns=df.columns)


def main() -> None:
    """Runs the main Streamlit application."""
    initialize_session_state()
    load_css()

    st.sidebar.markdown("<div class='glass-card' style='margin-bottom: 1rem;'><h3 style='margin:0;'>📸 Instagram Cleaner</h3></div>", unsafe_allow_html=True)
    nav = st.sidebar.radio(
        "Navigation",
        ["🏠 Home", "📂 Demo Export", "📤 Upload CSV", "📊 Analytics", "📥 Download", "ℹ About"],
        index=0,
        key="nav",
    )
    st.session_state.active_page = nav

    st.sidebar.markdown("---")
    st.session_state.dark_mode = st.sidebar.checkbox("🌙 Dark mode", value=st.session_state.dark_mode)
    st.sidebar.caption("Modern Instagram-inspired dashboard")

    if nav == "📂 Demo Export":
        if st.sidebar.button("Use Demo Instagram Export", use_container_width=True):
            demo_df = load_demo_data()
            username_col = detect_username_column(demo_df) or "username"
            set_data_state(demo_df, username_col)
            st.sidebar.success(f"Loaded {len(demo_df)} rows from demo export")

    if nav == "📤 Upload CSV":
        uploaded_file = st.sidebar.file_uploader("Drag and drop your CSV", type=["csv"], key="uploader")
        if uploaded_file is not None:
            try:
                uploaded_df = pd.read_csv(uploaded_file)
            except Exception as exc:
                st.sidebar.error(f"Unable to read CSV: {exc}")
                uploaded_df = pd.DataFrame()
            if not uploaded_df.empty:
                detected_col = detect_username_column(uploaded_df)
                if detected_col is None:
                    selected_col = st.sidebar.selectbox("Choose username column", options=uploaded_df.columns.tolist())
                    username_col = selected_col
                else:
                    username_col = detected_col
                set_data_state(uploaded_df, username_col)
                st.sidebar.success(f"Loaded {len(uploaded_df)} rows")

    if nav == "🏠 Home":
        st.markdown("<div class='hero-card'><span class='pill'>made by ❤️ Learn Build Share</span><h1>Instagram Followers Cleaner</h1><p>Remove duplicate Instagram followers using Python Sets.</p></div>", unsafe_allow_html=True)
        col_a, col_b = st.columns([1.4, 0.8])
        with col_a:
            st.markdown("<div class='glass-card'><h3 style='margin-top:0;'>⚡ Quick start</h3><p>Load the built-in demo export or upload your own Instagram follower CSV.</p></div>", unsafe_allow_html=True)
            if st.button("Load Demo Data", use_container_width=True):
                demo_df = load_demo_data()
                username_col = detect_username_column(demo_df) or "username"
                set_data_state(demo_df, username_col)
                st.success(f"Loaded {len(demo_df)} demo rows")
            if st.button("Upload CSV", use_container_width=True):
                st.session_state.active_page = "📤 Upload CSV"
                st.rerun()
        with col_b:
            st.markdown("<div class='glass-card'><h3 style='margin-top:0;'>✨ What this app does</h3><ul><li>Detects usernames automatically</li><li>Finds duplicates with Python sets</li><li>Shows analytics and reports</li><li>Downloads clean CSV and reports</li></ul></div>", unsafe_allow_html=True)

    if st.session_state.data_loaded and not st.session_state.df.empty:
        df = st.session_state.df.copy()
        username_col = st.session_state.username_col or detect_username_column(df) or df.columns[0]
        st.session_state.username_col = username_col

        if nav in {"🏠 Home", "📊 Analytics", "📥 Download", "ℹ About"}:
            st.markdown("<div class='glass-card' style='margin-bottom: 14px;'><h3 style='margin-top:0;'>✅ Data loaded successfully</h3><p><b>Rows loaded:</b> {}</p><p><b>Detected username column:</b> {}</p></div>".format(len(df), username_col), unsafe_allow_html=True)

        if nav in {"🏠 Home", "📊 Analytics"}:
            dup_summary = find_duplicates(df, username_col)
            metric_cols = st.columns(4)
            with metric_cols[0]:
                render_metric_card("Total Followers", len(df), "Original rows", "#8b5cf6")
            with metric_cols[1]:
                render_metric_card("Unique Followers", len(df[username_col].dropna().astype(str).str.strip().unique()), "Distinct names", "#ec4899")
            with metric_cols[2]:
                duplicates_count = len(df) - len(df[username_col].dropna().astype(str).str.strip().unique())
                render_metric_card("Duplicate Followers", duplicates_count, "Repeated entries", "#fb923c")
            with metric_cols[3]:
                duplicate_pct = round((duplicates_count / len(df) * 100), 2) if len(df) else 0.0
                render_metric_card("Duplicate %", f"{duplicate_pct}%", "Relative duplicates", "#06b6d4")

            col_left, col_right = st.columns(2)
            with col_left:
                st.markdown("<div class='glass-card'><h3 style='margin-top:0;'>📊 Duplicate summary</h3></div>", unsafe_allow_html=True)
                st.dataframe(dup_summary.sort_values("Occurrences", ascending=False).head(30), use_container_width=True)
            with col_right:
                st.markdown("<div class='glass-card'><h3 style='margin-top:0;'>🥧 Distribution</h3></div>", unsafe_allow_html=True)
                st.plotly_chart(create_pie_chart(df, df.drop_duplicates(subset=[username_col])), use_container_width=True)

            st.markdown("<div class='glass-card' style='margin-top: 14px;'><h3 style='margin-top:0;'>📈 Top duplicated usernames</h3></div>", unsafe_allow_html=True)
            st.plotly_chart(create_bar_chart(df, username_col), use_container_width=True)

        if nav == "📥 Download":
            if st.button("✨ Remove Duplicates", use_container_width=True, type="primary"):
                progress = st.progress(0, text="Preparing your clean dataset...")
                for step in range(100):
                    progress.progress(step + 1)
                with st.spinner("Cleaning followers ..."):
                    clean_df, duplicate_df = remove_duplicates(df, username_col)
                st.session_state.clean_df = clean_df.copy()
                st.session_state.duplicate_df = duplicate_df.copy()
                st.success("Duplicates removed successfully")
                st.balloons()

            if not st.session_state.clean_df.empty:
                clean_df = st.session_state.clean_df.copy()
                duplicate_df = st.session_state.duplicate_df.copy()
                stats = summary_statistics(df, clean_df, duplicate_df, username_col)
                st.markdown("<div class='glass-card'><h3 style='margin-top:0;'>📋 Summary</h3></div>", unsafe_allow_html=True)
                summary_cols = st.columns(4)
                with summary_cols[0]:
                    st.metric("Original rows", stats["original_rows"])
                with summary_cols[1]:
                    st.metric("Duplicates removed", stats["duplicates_removed"])
                with summary_cols[2]:
                    st.metric("Final rows", stats["final_rows"])
                with summary_cols[3]:
                    st.metric("Most repeated", f"{stats['most_repeated_username']} ({stats['most_repeated_count']})")
                report_text = generate_report(df, clean_df, duplicate_df, username_col)
                st.text_area("Report preview", report_text, height=220)
                buffer = io.StringIO()
                clean_df.to_csv(buffer, index=False)
                clean_bytes = buffer.getvalue().encode("utf-8")
                st.download_button("Download Clean CSV", clean_bytes, file_name="clean_followers.csv", mime="text/csv")
                buffer_dup = io.StringIO()
                duplicate_df.to_csv(buffer_dup, index=False)
                dup_bytes = buffer_dup.getvalue().encode("utf-8")
                st.download_button("Download Duplicate Report CSV", dup_bytes, file_name="duplicate_report.csv", mime="text/csv")
                st.download_button("Download TXT Summary", report_text, file_name="cleaning_report.txt")
            else:
                st.info("Click the button above to remove duplicates and enable downloads.")

        if nav == "ℹ About":
            st.markdown("<div class='glass-card'><h3 style='margin-top:0;'>About this project</h3><p>This dashboard demonstrates a modern workflow for cleaning duplicate Instagram follower exports using Python sets and Streamlit.</p></div>", unsafe_allow_html=True)

        if nav == "📊 Analytics" or nav == "🏠 Home":
            search_query = st.text_input("🔍 Search username")
            if search_query:
                matches = df[df[username_col].fillna("").astype(str).str.contains(search_query, case=False, na=False)]
                st.markdown("<div class='glass-card'><h4 style='margin-top:0;'>Search Results</h4></div>", unsafe_allow_html=True)
                st.dataframe(matches, use_container_width=True)

        if nav == "🏠 Home":
            st.markdown("<div class='glass-card' style='margin-top: 14px;'><h3 style='margin-top:0;'>🧾 Preview</h3></div>", unsafe_allow_html=True)
            st.dataframe(df.head(12), use_container_width=True)

        if nav == "📊 Analytics":
            tab_original, tab_clean = st.tabs(["Original Followers", "Clean Followers"])
            with tab_original:
                st.dataframe(highlight_duplicate_rows(df, username_col), use_container_width=True)
            with tab_clean:
                if not st.session_state.clean_df.empty:
                    st.dataframe(st.session_state.clean_df, use_container_width=True)
                else:
                    st.info("Remove duplicates first to preview the clean dataset.")

    else:
        st.info("Choose a data source from the sidebar to begin cleaning your followers.")

    st.markdown("<div class='footer'>Made by ❤️ Learn Build Share</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
