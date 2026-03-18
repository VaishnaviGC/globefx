import streamlit as st

def load_css():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Mono', monospace; }
.stApp { background: #0a0e1a; color: #e8edf5; }
#MainMenu, footer, header { visibility: hidden; }

.main-title {
    font-family: 'Syne', sans-serif; font-size: 2.2rem;
    font-weight: 800; color: #e8edf5; letter-spacing: -0.03em; margin-bottom: 0;
}
.main-title span { color: #00e5ff; }
.subtitle { font-size: 0.75rem; color: #6b7a99; margin-top: 4px; letter-spacing: 0.05em; }

.metric-card {
    background: #111827; border: 1px solid rgba(0,229,255,0.15);
    border-radius: 14px; padding: 18px 20px; text-align: center;
}
.metric-card:hover { border-color: rgba(0,229,255,0.4); }
.metric-flag { font-size: 1.6rem; }
.metric-country {
    font-family: 'Syne', sans-serif; font-size: 0.85rem;
    font-weight: 700; color: #e8edf5; margin: 6px 0 2px;
}
.metric-code { font-size: 0.65rem; color: #6b7a99; text-transform: uppercase; letter-spacing: 0.1em; }
.metric-rate {
    font-family: 'Syne', sans-serif; font-size: 1.25rem;
    font-weight: 700; color: #00e5ff; margin-top: 8px;
}
.metric-rate small { font-size: 0.65rem; color: #6b7a99; font-weight: 400; }

.section-header {
    font-family: 'Syne', sans-serif; font-size: 0.7rem; text-transform: uppercase;
    letter-spacing: 0.15em; color: #6b7a99; margin-bottom: 12px;
    border-bottom: 1px solid rgba(0,229,255,0.1); padding-bottom: 8px;
}
.converter-box {
    background: #111827; border: 1px solid rgba(0,229,255,0.15);
    border-radius: 14px; padding: 24px;
}
.result-big {
    font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800;
    color: #00e5ff; text-align: center; padding: 16px 0;
}
.result-big small { font-size: 0.9rem; color: #6b7a99; }
.live-badge {
    display: inline-flex; align-items: center; gap: 6px; font-size: 0.65rem;
    color: #00e676; border: 1px solid rgba(0,230,118,0.3); padding: 4px 12px;
    border-radius: 20px; background: rgba(0,230,118,0.05);
}
.stSelectbox > div > div {
    background: #111827 !important; border: 1px solid rgba(0,229,255,0.2) !important;
    color: #e8edf5 !important; border-radius: 10px !important;
}
.stNumberInput > div > div > input {
    background: #111827 !important; border: 1px solid rgba(0,229,255,0.2) !important;
    color: #e8edf5 !important; font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem !important; border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)