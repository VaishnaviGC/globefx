import streamlit as st
from data.countries import COUNTRY_CURRENCY

def render_converter(rates):
    st.markdown('<div class="section-header">🔍 Search & Convert</div>', unsafe_allow_html=True)

    country_list = sorted(COUNTRY_CURRENCY.keys())
    selected_country = st.selectbox(
        "Select a country",
        country_list,
        index=country_list.index("United States"),
        label_visibility="collapsed"
    )

    code, cname, flag = COUNTRY_CURRENCY[selected_country]
    code_lower = code.lower()

    if code_lower in rates:
        units_per_inr = rates[code_lower]
        inr_per_unit = 1 / units_per_inr if units_per_inr else 0

        st.markdown(f"""
        <div class="converter-box">
            <div style="display:flex; align-items:center; gap:14px; margin-bottom:18px;">
                <span style="font-size:2.4rem">{flag}</span>
                <div>
                    <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#e8edf5">{selected_country}</div>
                    <div style="font-size:0.7rem; color:#6b7a99">{cname} &nbsp;·&nbsp; {code}</div>
                </div>
            </div>
            <div style="background:rgba(0,229,255,0.05); border:1px solid rgba(0,229,255,0.2); border-radius:10px; padding:14px; text-align:center;">
                <div style="font-size:0.6rem; text-transform:uppercase; letter-spacing:0.12em; color:#6b7a99; margin-bottom:6px;">Live Rate</div>
                <div style="font-family:'Syne',sans-serif; font-size:1.6rem; font-weight:700; color:#00e5ff;">₹ {inr_per_unit:,.4f}</div>
                <div style="font-size:0.7rem; color:#6b7a99;">per 1 {code}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown('<div class="section-header">💱 Converter</div>', unsafe_allow_html=True)

        direction = st.radio(
            "Direction",
            [f"{code} → INR ₹", f"INR ₹ → {code}"],
            horizontal=True,
            label_visibility="collapsed"
        )

        if f"{code} → INR" in direction:
            amount = st.number_input(f"Amount in {code}", min_value=0.0, value=1.0, step=1.0, format="%.4f")
            result = amount * inr_per_unit
            st.markdown(f"""
            <div class="result-big">
                {amount:,.2f} {code}<br/>
                <span style="color:#6b7a99; font-size:1.2rem">=</span><br/>
                ₹ {result:,.2f}<br/><small>Indian Rupee</small>
            </div>""", unsafe_allow_html=True)
        else:
            amount = st.number_input("Amount in INR ₹", min_value=0.0, value=100.0, step=10.0, format="%.2f")
            result = amount * units_per_inr
            st.markdown(f"""
            <div class="result-big">
                ₹ {amount:,.2f}<br/>
                <span style="color:#6b7a99; font-size:1.2rem">=</span><br/>
                {result:,.4f} {code}<br/><small>{cname}</small>
            </div>""", unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ {cname} ({code}) rate not available.")