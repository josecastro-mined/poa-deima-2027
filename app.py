import streamlit as st
import pandas as pd
import plotly.express as px
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(
    page_title="Tablero Ejecutivo POA 2027 - DEIMA",
    page_icon="📊",
    layout="wide"
)
