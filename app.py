import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mein Finanz-Dashboard", layout="wide")
st.title("💰 Mein Finanz-Dashboard")

# Lade die Excel-Datei einmal komplett
# Da es eine .xlsx Datei ist, brauchen wir pd.read_excel
try:
    # Lade die Excel-Datei
    xls = pd.ExcelFile("Masterplan.xlsx")
    
    # Liste aller Tabellenblätter anzeigen
    sheet_names = xls.sheet_names
    selected_sheet = st.selectbox("Wähle eine Tabelle aus:", sheet_names)
    
    # Zeige das gewählte Blatt an
    df = pd.read_excel("Masterplan.xlsx", sheet_name=selected_sheet)
    st.dataframe(df)
    
except Exception as e:
    st.error(f"Fehler beim Laden der Excel-Datei: {e}")
