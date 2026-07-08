import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Finanz-Pro", layout="wide")

st.title("🚀 Finanz-Dashboard")

# Daten professionell laden
@st.cache_data
def get_clean_data():
    # Wir laden nur die relevanten Spalten
    df_haushalt = pd.read_csv("Masterplan.xlsx - Haushalt (Cash).csv")
    df_prog = pd.read_csv("Masterplan.xlsx - (SOLL) Prognosekurve.csv", skiprows=30)
    return df_haushalt, df_prog

h, p = get_clean_data()

# KPI Row
col1, col2, col3 = st.columns(3)
col1.metric("Kontostand", "46.419 €")
col2.metric("Überschuss/Monat", "1.250 €")
col3.metric("Immobilien-Eigenkapital", "92.000 €")

# Visualisierung
st.subheader("Vermögens-Prognose")
fig = px.line(p, x="Datum", y="Kalkulation Wohnungskauf", title="Entwicklung deines Immobilien-Werts")
st.plotly_chart(fig, use_container_width=True)
