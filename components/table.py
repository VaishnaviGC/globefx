import streamlit as st
import pandas as pd
from data.countries import COUNTRY_CURRENCY

def render_table(rates, rate_date):
    st.markdown('<div class="section-header">📋 All Countries — Currency Rate Table</div>', unsafe_allow_html=True)

    search_term = st.text_input("", placeholder="🔎 Filter by country, currency or code...", label_visibility="collapsed")

    table_rows = []
    for country, (code, cname, flag) in sorted(COUNTRY_CURRENCY.items()):
        if code in rates:
            table_rows.append({
                "Flag": flag,
                "Country": country,
                "Currency": cname,
                "Code": code,
                "₹ per 1 unit": round(1 / rates[code], 4),
                "Units per ₹1": round(rates[code], 6),
            })

    df_table = pd.DataFrame(table_rows)

    if search_term:
        mask = (
            df_table["Country"].str.contains(search_term, case=False) |
            df_table["Currency"].str.contains(search_term, case=False) |
            df_table["Code"].str.contains(search_term, case=False)
        )
        df_table = df_table[mask]

    st.dataframe(
        df_table,
        use_container_width=True,
        height=400,
        hide_index=True,
        column_config={
            "Flag": st.column_config.TextColumn("", width=40),
            "Country": st.column_config.TextColumn("Country", width=160),
            "Currency": st.column_config.TextColumn("Currency Name", width=180),
            "Code": st.column_config.TextColumn("Code", width=70),
            "₹ per 1 unit": st.column_config.NumberColumn("₹ per 1 unit", format="₹%.4f"),
            "Units per ₹1": st.column_config.NumberColumn("Units per ₹1", format="%.6f"),
        }
    )

    st.markdown(f"""
    <div style="text-align:center; font-size:0.65rem; color:#6b7a99; margin-top:20px;">
        GlobeFX · Live rates via Frankfurter API · Last updated: {rate_date} · Base: INR ₹
    </div>
    """, unsafe_allow_html=True)