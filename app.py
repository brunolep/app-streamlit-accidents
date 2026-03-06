# app.py


# ==========
# Librairies
# ==========

import streamlit as st
import pandas as pd
import numpy as np
import duckdb
import openpyxl
import re


# ==========
# APP
# ==========

st.set_page_config(
    page_title="Accidents 2024",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.data.gouv.fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2024',
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


pg = st.navigation(
    [
        st.Page("home.py", title="Accueil", icon="1️⃣"),
        st.Page("view_datasets.py", title="View Dataset", icon="2️⃣"),
        st.Page("dashboard.py", title="Dashboard", icon ="3️⃣"),
    ],
    position="top",
)


pg.run()
