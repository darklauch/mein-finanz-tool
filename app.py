python

import streamlit as st
import pandas as pd
import os

st.title("Debug: Finanz-App")

# Zeige an, welche Dateien GitHub im Ordner sieht
st.write("Dateien im Ordner:", os.listdir('.'))

filename = "Masterplan.xlsx"

if filename in os.listdir('.'):
    st.success(f"Gefunden! Lade {filename}...")
    try:
        # Wir laden das erste Blatt (Sheet) der Excel-Datei
        df = pd.read_excel(filename)
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Fehler beim Lesen der Excel-Datei: {e}")
else:
    st.error(f"Die Datei '{filename}' ist nicht im Hauptverzeichnis von GitHub!")
