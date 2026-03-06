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
# Functions
# ==========

# def request_function(database, query_request) :

#     try:
#         con = duckdb.connect(database, read_only=False)
#         results = con.execute(query_request).fetchdf()
#         # st.dataframe(results, hide_index=True)

#     except Exception as e:
#         print(f"Erreur de connexion : {e}")

#     finally:
#         if 'con' in locals() and con:
#             con.close()

#     return results


# # ==========
# # DATA SOURCE
# # ==========

# duckdb_file = "./data/database_accidents_2024.duckdb" # Assurez-vous que c'est le bon nom de fichier


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
        st.Page("home.py", title="Accueil", icon="🏠"),
        st.Page("view_datasets.py", title="View Dataset", icon="🔍"),
    ],
    position="top",
)


# pg = st.navigation(pages, postion = 'top')

pg.run()
