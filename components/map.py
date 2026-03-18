import streamlit as st
import pandas as pd
import plotly.express as px
from data.countries import COUNTRY_CURRENCY, COUNTRY_ISO3

def render_map(rates):
    st.markdown('<div class="section-header">🗺️ World Currency Map — Hover over any country</div>', unsafe_allow_html=True)

    map_data = []
    for country, (code, cname, flag) in COUNTRY_CURRENCY.items():
        iso3 = COUNTRY_ISO3.get(country)
        code_lower = code.lower()
        if iso3 and code_lower in rates:
            units_per_inr = rates[code_lower]
            inr_per_unit = round(1 / units_per_inr, 4) if units_per_inr else None
            map_data.append({
                "country": country,
                "iso3": iso3,
                "currency_code": code,
                "currency_name": cname,
                "flag": flag,
                "inr_per_unit": inr_per_unit,
            })
        elif iso3:
            map_data.append({
                "country": country,
                "iso3": iso3,
                "currency_code": code,
                "currency_name": cname,
                "flag": flag,
                "inr_per_unit": None,
            })

    df_map = pd.DataFrame(map_data)
    df_rated = df_map[df_map["inr_per_unit"].notna()].copy()
    df_unrated = df_map[df_map["inr_per_unit"].isna()].copy()

    fig = px.choropleth(
        df_rated,
        locations="iso3",
        color="inr_per_unit",
        hover_name="country",
        custom_data=["currency_code", "currency_name", "inr_per_unit", "flag"],
        color_continuous_scale=[
            [0, "#0d1f3c"], [0.1, "#0a4a6e"], [0.3, "#0077a8"],
            [0.6, "#00b4d8"], [0.85, "#00e5ff"], [1.0, "#ffd166"],
        ],
        labels={"inr_per_unit": "INR per unit"},
    )

    if not df_unrated.empty:
        fig.add_trace(
            px.choropleth(
                df_unrated,
                locations="iso3",
                color_discrete_sequence=["#2a2a3d"],
                hover_name="country",
                custom_data=["currency_code", "currency_name", "flag"],
            ).data[0]
        )

    fig.update_geos(
        showframe=False,
        showcoastlines=True, coastlinecolor="rgba(0,229,255,0.2)",
        showland=True, landcolor="#1a1a2e",
        showocean=True, oceancolor="#0a0e1a",
        showcountries=True, countrycolor="rgba(0,229,255,0.15)",
        showlakes=False, bgcolor="#0a0e1a",
        projection_type="natural earth",
    )

    fig.update_layout(
        paper_bgcolor="#0a0e1a", plot_bgcolor="#0a0e1a",
        margin=dict(l=0, r=0, t=0, b=0), height=440,
        coloraxis_colorbar=dict(
            title="₹ per unit",
            title_font=dict(color="#6b7a99", size=11),
            tickfont=dict(color="#6b7a99", size=10),
            bgcolor="rgba(17,24,39,0.8)",
            bordercolor="rgba(0,229,255,0.2)",
            len=0.6,
        ),
        font=dict(family="DM Mono"),
        showlegend=False,
    )

    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>Currency: %{customdata[0]} — %{customdata[1]}<br>Rate: ₹%{customdata[2]:,.4f} per unit<extra></extra>",
        selector=dict(type="choropleth")
    )

    st.plotly_chart(fig, use_container_width=True)