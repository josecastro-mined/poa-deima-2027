import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json

st.set_page_config(page_title="Tablero Ejecutivo POA 2027", layout="wide")

@st.cache_data(ttl=600)
def cargar_datos():
    try:
        scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
        if "gcp_service_account" in st.secrets:
            creds_json = json.loads(st.secrets["gcp_service_account"]["json_data"])
            creds = Credentials.from_service_account_info(creds_json, scopes=scope)
        else:
            st.error("No se encontraron las credenciales en st.secrets.")
            return pd.DataFrame()

        client = gspread.authorize(creds)
        sheet_id = "1So31pUIdsVC3F6emRZB9fphqeaUgXJrNoBltyWe_7wo"
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1So31pUIdsVC3F6emRZB9fphqeaUgXJrNoBltyWe_7wo/edit?gid=297853090#gid=297853090").worksheet("POA 2027")
        datos = sheet.get_all_records()
        df = pd.DataFrame(datos)
        return df.astype(str)
    except Exception as e:
        st.error(f"Error al conectar con Google Sheets: {e}")
        return pd.DataFrame()

st.title("📊 Tablero Ejecutivo POA 2027 - DEIMA")

df = cargar_datos()

if not df.empty:
    st.metric("Total de Registros POA", len(df))
    st.subheader("Vista de Datos")
    st.dataframe(df)
else:
    st.warning("No se pudieron cargar los datos o la hoja está vacía.")
