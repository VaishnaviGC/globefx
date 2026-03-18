import streamlit as st
from styles.css import load_css
from utils.rates import fetch_rates
from components.map import render_map
from components.converter import render_converter
from components.table import render_table

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="GlobeFX — Currency Explorer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── Load CSS ────────────────────────────────────────────────────────────────
load_css()

# ─── Header ──────────────────────────────────────────────────────────────────
col_title, col_badge = st.columns([3, 1])
with col_title:
    st.markdown('<div class="main-title">GLOBE<span>FX</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">🌍 Interactive Currency Explorer · Base: Indian Rupee ₹</div>', unsafe_allow_html=True)

rates, rate_date = fetch_rates()

with col_badge:
    st.markdown("<br/>", unsafe_allow_html=True)
    if rates:
        st.markdown(f'<div class="live-badge">🟢 &nbsp; Live rates · {rate_date}</div>', unsafe_allow_html=True)
    else:
        st.error("⚠️ Could not fetch live rates")

st.markdown("---")
if not rates:
    st.stop()

# ─── Popular Currencies ───────────────────────────────────────────────────────
st.markdown('<div class="section-header">📊 Popular Currencies — INR per 1 unit</div>', unsafe_allow_html=True)

highlights = [
    ("United States", "USD", "🇺🇸"), ("United Kingdom", "GBP", "🇬🇧"),
    ("European Union", "EUR", "🇪🇺"), ("Japan", "JPY", "🇯🇵"),
    ("China", "CNY", "🇨🇳"), ("United Arab Emirates", "AED", "🇦🇪"),
    ("Australia", "AUD", "🇦🇺"), ("Singapore", "SGD", "🇸🇬"),
]

cols = st.columns(len(highlights))
for i, (country, code, flag) in enumerate(highlights):
    if code in rates:
        inr_val = 1 / rates[code]
        with cols[i]:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-flag">{flag}</div>
                <div class="metric-country">{country}</div>
                <div class="metric-code">{code}</div>
                <div class="metric-rate">₹{inr_val:.2f}<br/><small>per 1 {code}</small></div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

# ─── Map + Converter ──────────────────────────────────────────────────────────
map_col, right_col = st.columns([3, 2], gap="large")

with map_col:
    render_map(rates)

with right_col:
    render_converter(rates)

st.markdown("---")

# ─── Table ────────────────────────────────────────────────────────────────────
render_table(rates, rate_date)