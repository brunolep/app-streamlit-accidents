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

def request_function(database, query_request) :
    
    try:
        con = duckdb.connect(database, read_only=False)
        results = con.execute(query_request).fetchdf()
        # st.dataframe(results, hide_index=True)

    except Exception as e:
        print(f"Erreur de connexion : {e}")
        
    finally:
        if 'con' in locals() and con:
            con.close()
    
    return results



# ==========
# DATA SOURCE
# ==========

duckdb_file = "./data/database_accidents_2024.duckdb" # Assurez-vous que c'est le bon nom de fichier



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

st.header('**ANALYSE DES ACCIDENTS 2024**')
st.markdown('')

with st.expander('Informations',expanded = False, icon ='ℹ️') :

    st.caption('Données issues du site https://www.data.gouv.fr :')
    st.caption('https://www.data.gouv.fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2024')



tab1 , tab2, tab3, tab4, tab5 = st.tabs(['Véhicules', 'Accidents', 'Localisations', 'Usagers', 'Requêtes'])

with tab1 :
    
    st.header("Dataset des véhicules")

    vehicules_results = request_function(database=duckdb_file, query_request = "SELECT * FROM vehicules LIMIT 10;")
    
    st.dataframe(vehicules_results, hide_index=True)


with tab2 :
    
    st.header("Dataset des accidents")

    accidents_results = request_function(database=duckdb_file, query_request = "SELECT * FROM accidents LIMIT 10;")
    
    st.dataframe(accidents_results, hide_index=True)


    
    
with tab3 :    
    
    st.header("Dataset des localisations")

    localisations_results = request_function(database=duckdb_file, query_request = "SELECT * FROM localisations LIMIT 10;")
    
    st.dataframe(localisations_results, hide_index=True)




with tab4 :
        
    st.header("Dataset des usagers")

    usagers_results = request_function(database=duckdb_file, query_request = "SELECT * FROM usagers LIMIT 10;")
    
    st.dataframe(usagers_results, hide_index=True)

            
            

with tab5 :
    
    sql_request = st.text_area(label= "Entrer la commande")

    if sql_request :
        
        st.write(f"La requête est la suivante : **{sql_request}**")
          
        results = request_function(database=duckdb_file, query_request = sql_request)
        
        st.dataframe(results, hide_index=True)

            
