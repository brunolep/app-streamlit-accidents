# app.py


# ==========
# Librairies
# ==========

import streamlit as st
import pandas as pd
import numpy as np
import duckdb
# import openpyxl
import re


# ==========
# Functions
# ==========
def get_column_names_from_duckdb(db_file: str, table_name: str):
    """
    Se connecte à un fichier DuckDB et récupère les noms des colonnes d'une table spécifiée.

    Args:
        db_file (str): Le chemin vers le fichier DuckDB.
        table_name (str): Le nom de la table dont on veut récupérer les noms de colonnes.

    Returns:
        list: Une liste des noms de colonnes de la table, ou None en cas d'erreur.
    """
    try:
        con = duckdb.connect(database=db_file, read_only=True)
        query = f"PRAGMA table_info('{table_name}');"
        result = con.execute(query).fetchdf()

        if not result.empty:
            column_names = result["name"].tolist()
            return column_names
        else:
            st.write(f"La table '{table_name}' est vide ou n'existe pas.")
            return None

    except duckdb.Error as e:
        print(f"Une erreur DuckDB est survenue : {e}")
        return None
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")
        return None
    finally:
        if "con" in locals() and con:
            con.close()


def request_function(database, query_request) :

    try:
        con = duckdb.connect(database, read_only=False)
        results = con.execute(query_request).fetchdf()

    except Exception as e:
        print(f"Erreur de connexion : {e}")

    finally:
        if 'con' in locals() and con:
            con.close()

    return results


def get_table_names_from_duckdb(db_file: str):
    """
    Se connecte à un fichier DuckDB et récupère les noms de toutes les tables.

    Args:
        db_file (str): Le chemin vers le fichier DuckDB.

    Returns:
        list: Une liste des noms de tables, ou None en cas d'erreur.
    """
    try:
        con = duckdb.connect(database=db_file, read_only=True)
        # La requête SHOW TABLES; retourne une table avec une colonne 'name'
        result = con.execute("SHOW TABLES;").fetchdf()

        if not result.empty:
            table_names = result["name"].tolist()
            return table_names
        else:
            print("Aucune table trouvée dans la base de données.")
            return []  # Retourne une liste vide si aucune table n'est trouvée

    except duckdb.Error as e:
        print(
            f"Une erreur DuckDB est survenue lors de la récupération des tables : {e}"
        )
        return None
    except Exception as e:
        print(
            f"Une erreur inattendue est survenue lors de la récupération des tables : {e}"
        )
        return None
    finally:
        if "con" in locals() and con:
            con.close()


# ==========
# DATA SOURCE
# ==========

duckdb_file = "./data/database_accidents_2024.duckdb" # Assurez-vous que c'est le bon nom de fichier


st.title("Bienvenue sur l'Application d'Analyse des Accidents Corporels de la Route")


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
    # DESCRIBE usagers;

    usagers_results = request_function(database=duckdb_file, query_request = "SELECT * FROM usagers LIMIT 10;")

    st.dataframe(usagers_results, hide_index=True)


with tab5 :

    col1, col2, col3, col4 = st.columns(4)

    tables_to_check = ["vehicules", "accidents", "localisations", "usagers"]



    with st.sidebar :
        
        theme_selected = st.selectbox(
            label = "Selection du type de review ?",
            options = ('Joins','GroupBy','Windows Functions'),
            index = None,
            placeholder = 'Select a theme',
        )
    
        st.write(f"Theme sélectionné : {theme_selected}")
    
    
    
    
    
    # Appel de la nouvelle fonction pour obtenir les noms des tables
    table_names_list = get_table_names_from_duckdb(duckdb_file)

    if table_names_list:
        st.subheader("Noms de toutes les tables dans le fichier DuckDB :")
        st.write(table_names_list)  # Affiche la liste des noms de tables
    else:
        st.write("Impossible de récupérer les noms des tables ou aucune table trouvée.")

    # for table_name in tables_to_check:
    #     st.subheader(f"Table : {table_name}")
    #     raw_column_data = get_column_names_from_duckdb(duckdb_file, table_name)

    # if raw_column_data is not None:
    #     # Assurez-vous que c'est une liste de chaînes
    #     final_column_names_list = []
    #     if isinstance(raw_column_data, list):
    #         final_column_names_list = raw_column_data
    #     elif hasattr(raw_column_data, "tolist"):
    #         final_column_names_list = raw_column_data.tolist()
    #     elif hasattr(raw_column_data, "values"):
    #         final_column_names_list = list(raw_column_data.values())
    #     else:
    #         final_column_names_list = list(raw_column_data)

    #     df_horizontal_names = pd.DataFrame([final_column_names_list])
    #     st.dataframe(df_horizontal_names)
    # else:
    #     st.write(
    #         f"Impossible de récupérer les noms des colonnes pour la table '{table_name}'."
    #     )

    sql_request = st.text_area(label= "Entrer la commande")

    if sql_request :

        st.write(f"La requête est la suivante : **{sql_request}**")

        results = request_function(database=duckdb_file, query_request = sql_request)

        st.dataframe(results, hide_index=True)
