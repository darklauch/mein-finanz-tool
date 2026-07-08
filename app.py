import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mein Finanz-Dashboard", layout="wide")
st.title("💰 Finanz-Cockpit")

# Hilfsfunktion zum Laden der Daten
@st.cache_data
def load_data():
    haushalt = pd.read_csv("Masterplan.xlsx - Haushalt (Cash).csv")
    finanz = pd.read_csv("Masterplan.xlsx - Finanzierung&Mietkalkulation.csv")
    prognose = pd.read_csv("Masterplan.xlsx - (SOLL) Prognosekurve.csv")
    return haushalt, finanz, prognose

haushalt, finanz, prognose = load_data()

# Tabs erstellen
tab1, tab2, tab3 = st.tabs(["Übersicht", "Haushalt", "Prognose"])

with tab1:
    st.header("Aktueller Status")
    # Hier ziehen wir Werte aus deinen CSVs
    st.metric("Kontostand", "46.419 €") # Beispielwert aus deinem CSV-Snippet
    st.dataframe(finanz.head(5))

with tab2:
    st.header("Haushalt & Cashflow")
    st.dataframe(haushalt)

with tab3:
    st.header("Langfristige Entwicklung")
    st.line_chart(prognose.select_dtypes(include=['number']))
