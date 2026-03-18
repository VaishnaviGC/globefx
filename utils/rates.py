import streamlit as st
import requests

@st.cache_data(ttl=300)
def fetch_rates():
    try:
        res = requests.get(
            "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/inr.json",
            timeout=8
        )
        data = res.json()
        raw = data["inr"]

        # Store BOTH lowercase and uppercase keys
        r = {}
        for code, val in raw.items():
            if val and val > 0:
                r[code.lower()] = val
                r[code.upper()] = val
        r["INR"] = 1.0
        r["inr"] = 1.0
        return r, data.get("date", "N/A")
    except Exception as e:
        return None, None