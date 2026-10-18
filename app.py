from datetime import datetime

import streamlit as st

st.set_page_config(
    page_title="VibhuA-ai | Fieldnotes",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #202b29;
        --paper: #f5f3eb;
        --muted: #68736d;
        --coral: #df6748;
        --teal: #28796e;
        --lime: #d6df72;
        --line: #d9ddd1;
    }

    .stApp {
        background: var(--paper);
        color: var(--ink);
        font-family: 'Manrope', sans-serif;
    }

    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stToolbar"] { right: 1.5rem; }
    h1, h2, h3, p, label { font-family: 'Manrope', sans-serif; }

    section[data-testid="stSidebar"] {
        background: var(--ink);
        border-right: 1px solid #35413c;
    }

    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3,
    section[data-testid="stSidebar"] label {
        color: #f5f3eb;
    }

    section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
        color: #a8b2aa;
    }

    section[data-testid="stSidebar"] [data-baseweb="select"] > div,
    section[data-testid="stSidebar"] [data-testid="stTextInput"] input {
        background: #2d3935;
        color: #f5f3eb;
        border-color: #45534c;
    }

    .brand-lockup {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin: 0.25rem 0 2.4rem;
    }

    .brand-mark {
        display: grid;
        place-items: center;
        width: 2.6rem;
        height: 2.6rem;
        border-radius: 50%;
        background: var(--lime);
        color: var(--ink);
        font-size: 0.9rem;
        font-weight: 800;
    }

    .brand-name { color: #f5f3eb; font-weight: 800; }
    .brand-subtitle {
        color: #a8b2aa;
        font-family: 'DM Mono', monospace;
        font-size: 0.62rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .eyebrow, .section-kicker {
        color: var(--teal);
        font-family: 'DM Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .hero-title {
        max-width: 850px;
        margin: 0.55rem 0 0.65rem;
        color: var(--ink);
        font-size: 4rem;
        font-weight: 800;
        line-height: 0.98;
    }

    @media (max-width: 640px) {
        .hero-title { font-size: 2.8rem; }
    }

    .hero-title span { color: var(--coral); }
    .hero-copy { max-width: 660px; color: var(--muted); font-size: 1rem; }
    .top-rule { border-top: 1px solid var(--line); margin: 1.7rem 0 1.1rem; }

    [data-testid="stMetric"] {
        padding: 1rem 1.15rem;
        border: 1px solid var(--line);
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.48);
    }

    [data-testid="stMetricLabel"] p {
        color: var(--muted);
        font-family: 'DM Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }

    [data-testid="stMetricValue"] { color: var(--ink); font-weight: 800; }
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: var(--line);
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.5);
    }

    div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
        min-height: 2.8rem;
        border: 0;
        border-radius: 5px;
        background: var(--coral);
        color: white;
        font-weight: 700;
    }

    div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        border: 0;
        background: #c85237;
        color: white;
    }

    [data-testid="stProgressBar"] > div > div { background: var(--teal); }
    [data-testid="stBaseButton-secondary"] { border-radius: 5px; }
    </style>
    """,
    unsafe_allow_html=True,
)

if "fieldnotes" not in st.session_state:
    st.session_state.fieldnotes = []
if "project_title" not in st.session_state:
    st.session_state.project_title = "A small, useful thing"
if "project_intention" not in st.session_state:
    st.session_state.project_intention = "Make one idea easier to use."
if "project_progress" not in st.session_state:
    st.session_state.project_progress = 35

with st.sidebar:
    st.markdown(
        """
        <div class="brand-lockup">
            <div class="brand-mark">VA</div>
            <div>
                <div class="brand-name">VibhuA-ai</div>
                <div class="brand-subtitle">Fieldnotes studio</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    page = st.radio(
        "STUDIO", ["The desk", "Fieldnotes", "About"], label_visibility="visible"
    )
    st.divider()
    lane = st.selectbox(
        "CURRENT LANE",
        ["Tiny tools", "Visual experiments", "Writing", "Learning"],
    )
    st.caption("A personal space for ideas in progress.")
    st.markdown("<div style='height: 2rem'></div>", unsafe_allow_html=True)
    st.caption(f"LOCAL TIME  /  {datetime.now().strftime('%H:%M')}")

if page == "The desk":
    st.markdown(
        f"<div class='eyebrow'>VIBHUA-AI &nbsp; / &nbsp; {datetime.now().strftime('%A, %B %d')}</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h1 class='hero-title'>A place for<br><span>good work.</span></h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p class='hero-copy'>A calm little workspace for shaping ideas, keeping momentum, and noticing what is worth building next.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<div class='top-rule'></div>", unsafe_allow_html=True)

    metric_columns = st.columns(3)
    metric_columns[0].metric("Current lane", lane)
    metric_columns[1].metric("In motion", f"{st.session_state.project_progress}%")
    metric_columns[2].metric("Notes kept", len(st.session_state.fieldnotes))

    st.markdown("<div style='height: 1rem'></div>", unsafe_allow_html=True)
    left, right = st.columns([1.55, 1], gap="large")

    with left:
        st.markdown(
            "<div class='section-kicker'>01 / The active idea</div>",
            unsafe_allow_html=True,
        )
        with st.container(border=True):
            with st.form("direction_form"):
                project_title = st.text_input(
                    "Working title", value=st.session_state.project_title
                )
                project_intention = st.text_area(
                    "What should this make easier?",
                    value=st.session_state.project_intention,
                    height=100,
                )
                project_progress = st.slider(
                    "How far along does it feel?",
                    min_value=0,
                    max_value=100,
                    value=st.session_state.project_progress,
                    format="%d%%",
                )
                saved = st.form_submit_button(
                    "Save today's direction", use_container_width=True
                )

            if saved:
                st.session_state.project_title = project_title
                st.session_state.project_intention = project_intention
                st.session_state.project_progress = project_progress
                st.success("Direction saved for this session.")

    with right:
        st.markdown(
            "<div class='section-kicker'>02 / A small next step</div>",
            unsafe_allow_html=True,
        )
        with st.container(border=True):
            st.markdown(f"### {st.session_state.project_title}")
            st.write(st.session_state.project_intention)
            st.progress(st.session_state.project_progress / 100)
            st.caption("Progress is a prompt, not a performance review.")
            if st.button("Add a fieldnote", use_container_width=True):
                st.session_state.open_note_form = True

    if st.session_state.get("open_note_form", False):
        with st.form("quick_note_form", clear_on_submit=True):
            note_text = st.text_input(
                "Capture a thought", placeholder="What did you notice?"
            )
            add_note = st.form_submit_button("Keep this note")
        if add_note and note_text.strip():
            st.session_state.fieldnotes.insert(
                0,
                {
                    "text": note_text.strip(),
                    "time": datetime.now().strftime("%H:%M"),
                },
            )
            st.session_state.open_note_form = False
            st.rerun()

    if st.session_state.fieldnotes:
        st.markdown("<div class='top-rule'></div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='section-kicker'>03 / Recent fieldnotes</div>",
            unsafe_allow_html=True,
        )
        note_columns = st.columns(min(len(st.session_state.fieldnotes), 3))
        for index, note in enumerate(st.session_state.fieldnotes[:3]):
            with note_columns[index]:
                with st.container(border=True):
                    st.caption(note["time"])
                    st.write(note["text"])

elif page == "Fieldnotes":
    st.markdown(
        "<div class='eyebrow'>VIBHUA-AI &nbsp; / &nbsp; FIELDNOTES</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h1 class='hero-title'>Keep the<br><span>good bits.</span></h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p class='hero-copy'>Loose observations belong somewhere. Save a thought now; decide what it means later.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<div class='top-rule'></div>", unsafe_allow_html=True)

    with st.form("fieldnote_form", clear_on_submit=True):
        note_text = st.text_area(
            "A thought worth keeping",
            placeholder="A tiny discovery, a question, a promising detail...",
            height=120,
        )
        add_note = st.form_submit_button("Save fieldnote", use_container_width=True)

    if add_note and note_text.strip():
        st.session_state.fieldnotes.insert(
            0,
            {
                "text": note_text.strip(),
                "time": datetime.now().strftime("%b %d · %H:%M"),
            },
        )
        st.rerun()

    st.markdown("<div class='top-rule'></div>", unsafe_allow_html=True)
    if not st.session_state.fieldnotes:
        st.info("No fieldnotes yet. Start with one thing you noticed today.")
    else:
        for note in st.session_state.fieldnotes:
            with st.container(border=True):
                st.caption(note["time"])
                st.write(note["text"])

else:
    st.markdown(
        "<div class='eyebrow'>A NOTE ON THE STUDIO</div>", unsafe_allow_html=True
    )
    st.markdown(
        "<h1 class='hero-title'>Built with<br><span>curiosity.</span></h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p class='hero-copy'>Fieldnotes is VibhuA-ai's small, personal build desk: a place to give one idea a name, track its momentum, and keep the details that might otherwise disappear.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<div class='top-rule'></div>", unsafe_allow_html=True)
    about_left, about_right = st.columns(2, gap="large")
    with about_left:
        st.markdown("### The approach")
        st.write(
            "Keep the interface quiet, make the next action obvious, and leave room for the work to change shape."
        )
    with about_right:
        st.markdown("### Made by")
        st.write("VibhuA-ai")
        st.caption("A personal Streamlit project. Ideas welcome; polish is optional.")

st.markdown("<div class='top-rule'></div>", unsafe_allow_html=True)
st.caption("VibhuA-ai  /  FIELDNOTES STUDIO  /  BUILT TO KEEP MOVING")
