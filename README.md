# Application d'Analyse des Accidents Corporels de la Route (BAAC)

![Streamlit App Screenshot](https://via.placeholder.com/800x400?text=Capture+d%27écran+de+l%27application)
*(Remplacez l'image ci-dessus par une capture d'écran réelle de votre application)*

## Table des Matières
1.  [Introduction](#introduction)
2.  [Source des Données](#source-des-données)
3.  [Fonctionnalités](#fonctionnalités)
4.  [Structure du Projet](#structure-du-projet)
5.  [Comment Utiliser l'Application](#comment-utiliser-lapplication)
6.  [Installation et Lancement Local](#installation-et-lancement-local)
7.  [Contact](#contact)

## 1. Introduction

Cette application interactive, développée avec [Streamlit](https://streamlit.io/), a pour objectif d'offrir une exploration approfondie des données relatives aux accidents corporels de la circulation routière en France. En exploitant les données ouvertes du **Fichier BAAC (Bulletin d'Analyse des Accidents Corporels)**, issues de l'**Observatoire National Interministériel de la Sécurité Routière (ONISR)** et disponibles sur data.gouv.fr, cet outil puissant permet de visualiser, analyser et comprendre les dynamiques des accidents sur nos routes.

L'objectif est de fournir des insights pour les professionnels, chercheurs et citoyens intéressés par l'amélioration de la sécurité routière, en facilitant l'identification des tendances, des facteurs de risque et des zones à forte accidentologie.

## 2. Source des Données

L'application s'appuie sur les bases de données annuelles des accidents corporels de la circulation routière, couvrant la période de **2005 à 2024**. Ces données sont structurées en quatre fichiers distincts (initialement au format CSV) :

*   **Caractéristiques** : Circonstances générales de l'accident (date, heure, luminosité, conditions atmosphériques, type de collision, etc.).
*   **Lieux** : Détails sur le lieu de l'accident (catégorie de route, régime de circulation, profil en long, tracé en plan, état de la surface, infrastructures, etc.).
*   **Véhicules** : Informations sur les véhicules impliqués (catégorie, obstacles heurtés, manœuvres, type de motorisation, etc.).
*   **Usagers** : Détails sur les personnes impliquées (catégorie d'usager, gravité des blessures, sexe, âge, motif du déplacement, équipements de sécurité, etc.).

Pour une description détaillée de chaque variable, veuillez consulter la section "Description Détaillée des Variables" sur la page d'accueil de l'application.

**Lien vers les données :** [https://www.data.gouv.fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2024](https://www.data.gouv.fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2024)

## 3. Fonctionnalités

L'application est divisée en plusieurs sections pour une exploration complète :

### 3.1. Accueil
*   Présentation générale de l'application et de ses objectifs.
*   Description détaillée des variables présentes dans les fichiers BAAC.

### 3.2. Visualisation des Données
Cette section offre une exploration interactive des données à travers des graphiques et des cartes :
*   **Filtres dynamiques** : Permet de filtrer les données par année, département, type d'usager, gravité des blessures, conditions météorologiques, etc.
*   **Graphiques personnalisables** : Visualisation de la répartition des accidents, des tendances temporelles, des corrélations entre différentes variables.
*   **Cartographie des accidents** : Identification des zones à risque et visualisation spatiale des événements.

### 3.3. Requêtes SQL
Pour une analyse plus avancée et personnalisée, cette section intègre un moteur de requêtes SQL :
*   **Éditeur SQL** : Écrivez et exécutez vos propres requêtes directement sur la base de données des accidents.
*   **Accès aux tables** : Interrogez les tables `Caracteristiques`, `Lieux`, `Vehicules` et `Usagers`.
*   **Résultats tabulaires** : Affichez les résultats de vos requêtes sous forme de tableau.
*   **Exemples de requêtes** : Des exemples sont fournis pour aider les utilisateurs à démarrer.

## 4. Structure du Projet


## 5. Comment Utiliser l'Application

1.  **Navigation** : Utilisez le menu latéral (sidebar) pour naviguer entre les différentes sections : "Accueil", "Visualisation des Données", "Requêtes SQL".
2.  **Filtres** : Dans la section de visualisation, utilisez les filtres disponibles pour affiner les données affichées.
3.  **Requêtes SQL** : Dans la section SQL, saisissez vos requêtes dans l'éditeur et cliquez sur "Exécuter" pour voir les résultats.

## 6. Installation et Lancement Local

Pour lancer cette application sur votre machine locale :

1.  **Clonez le dépôt GitHub :**
    ```bash
    git clone https://github.com/brunolep/app-streamlit-accidents.git
    cd AppStreamlit
    ```

2.  **Créez un environnement virtuel (recommandé) :**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Linux/macOS
    # venv\Scripts\activate   # Sur Windows
    ```

3.  **Installez les dépendances Python :**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Lancez l'application Streamlit :**
    ```bash
    streamlit run home.py
    ```
    L'application s'ouvrira automatiquement dans votre navigateur web.

## 7. Contact

Pour toute question ou suggestion, n'hésitez pas à contacter [Votre Nom/Pseudo] ou à ouvrir une issue sur ce dépôt GitHub.

---
*Développé avec passion pour une meilleure sécurité routière.*