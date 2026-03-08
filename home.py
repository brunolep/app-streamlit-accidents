

import streamlit as st


# st.header('**ANALYSE DES ACCIDENTS 2024**')
# st.markdown('')

# with st.expander('Informations',expanded = False, icon ='ℹ️') :


st.title("Bienvenue sur l'Application d'Analyse des Accidents Corporels de la Route")

st.markdown("---") # Ligne de séparation pour une meilleure lisibilité

st.caption('Données issues du site https://www.data.gouv.fr :')
st.caption('https://www.data.gouv.fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2024')

st.header("Comprendre et Agir pour la Sécurité Routière")
st.write(
    """
    Cette application interactive, développée avec Streamlit, a pour objectif de vous offrir une exploration approfondie des données relatives aux accidents corporels de la circulation routière en France.
    En exploitant les données ouvertes du **Fichier BAAC (Bulletin d'Analyse des Accidents Corporels)**, issues de l'**Observatoire National Interministériel de la Sécurité Routière (ONISR)** et disponibles sur data.gouv.fr,
    nous mettons à votre disposition un outil puissant pour visualiser, analyser et comprendre les dynamiques des accidents sur nos routes.
    """
)

st.header("Source des Données : Le Fichier BAAC")
st.write(
    """
    Le Fichier BAAC compile les informations détaillées sur chaque accident corporel (impliquant au moins un véhicule et une victime nécessitant des soins)
    relevé par les forces de l'ordre. Ces données sont cruciales pour l'élaboration des politiques de sécurité routière et la prévention des risques.
    """
)
st.write(
    """
    Notre application s'appuie sur les bases de données annuelles, couvrant la période de **2005 à 2024**, et structurées en quatre fichiers distincts au format CSV :
    """
)
st.markdown(
    """
    *   **Caractéristiques** : Décrit les circonstances générales de l'accident (date, heure, luminosité, conditions atmosphériques, type de collision, etc.).
    *   **Lieux** : Fournit des détails sur le lieu de l'accident (catégorie de route, régime de circulation, profil en long, tracé en plan, état de la surface, infrastructures, etc.).
    *   **Véhicules** : Contient des informations sur les véhicules impliqués (catégorie, obstacles heurtés, manœuvres, type de motorisation, etc.).
    *   **Usagers** : Décrit les personnes impliquées dans l'accident (catégorie d'usager, gravité des blessures, sexe, âge, motif du déplacement, équipements de sécurité, localisation et action du piéton le cas échéant).
    """
)

st.header("Objectifs de l'Application")
st.markdown(
    """
    *   **Visualisation Intuitive** : Présenter les données complexes de manière graphique et facile à interpréter.
    *   **Analyse des Tendances** : Identifier les évolutions des accidents au fil des ans, par région, par type de véhicule ou d'usager.
    *   **Identification des Facteurs de Risque** : Mettre en lumière les conditions (météo, luminosité, type de route, manœuvres) et les comportements (usagers, véhicules) les plus fréquemment associés aux accidents.
    *   **Support à la Décision** : Fournir des insights pour les professionnels, chercheurs et citoyens intéressés par l'amélioration de la sécurité routière.
    """
)

st.header("Points d'Attention sur les Données")
st.write(
    """
    Il est important de noter que les données sont anonymisées pour protéger la vie privée des individus.
    Des modifications dans les processus de saisie ont eu lieu au fil des ans (notamment pour l'indicateur "blessé hospitalisé" à partir de 2018 et l'ajout des "usagers en fuite" à partir de 2021),
    ce qui peut influencer la comparabilité de certaines variables sur de longues périodes.
    L'application prendra en compte ces nuances pour une interprétation juste des résultats.
    """
)



st.header("Description Détaillée des Variables")
st.write("Explorez ci-dessous la signification de chaque variable présente dans les bases de données BAAC.")


with st.expander("Fichier CARACTERISTIQUES : Circonstances générales de l'accident", icon = "✍🏻"):
    st.markdown("""
    *   **`Num_Acc`** : Numéro d'identifiant de l'accident.
    *   **`jour`** : Jour de l'accident.
    *   **`mois`** : Mois de l'accident.
    *   **`an`** : Année de l'accident.
    *   **`hrmn`** : Heure et minutes de l'accident.
    *   **`lum`** : Lumière : conditions d'éclairage.
        *   1 - Plein jour
        *   2 - Crépuscule ou aube
        *   3 - Nuit sans éclairage public
        *   4 - Nuit avec éclairage public non allumé
        *   5 - Nuit avec éclairage public allumé
    *   **`dep`** : Département (Code INSEE).
    *   **`com`** : Commune (Code INSEE du département + 3 chiffres).
    *   **`agg`** : Localisation.
        *   1 - Hors agglomération
        *   2 - En agglomération
    *   **`int`** : Intersection.
        *   1 - Hors intersection
        *   2 - Intersection en X
        *   3 - Intersection en T
        *   4 - Intersection en Y
        *   5 - Intersection à plus de 4 branches
        *   6 - Giratoire
        *   7 - Place
        *   8 - Passage à niveau
        *   9 - Autre intersection
    *   **`atm`** : Conditions atmosphériques.
        *   -1 - Non renseigné
        *   1 - Normale
        *   2 - Pluie légère
        *   3 - Pluie forte
        *   4 - Neige - grêle
        *   5 - Brouillard - fumée
        *   6 - Vent fort - tempête
        *   7 - Temps éblouissant
        *   8 - Temps couvert
        *   9 - Autre
    *   **`col`** : Type de collision.
        *   -1 - Non renseigné
        *   1 - Deux véhicules - frontale
        *   2 - Deux véhicules - par l'arrière
        *   3 - Deux véhicules - par le coté
        *   4 - Trois véhicules et plus - en chaîne
        *   5 - Trois véhicules et plus - collisions multiples
        *   6 - Autre collision
        *   7 - Sans collision
    *   **`adr`** : Adresse postale (pour accidents en agglomération).
    *   **`lat`** : Latitude.
    *   **`long`** : Longitude.
    """)

# --- Rubrique LIEUX ---
with st.expander("Fichier LIEUX : Détails sur le lieu de l'accident", icon = "🛣"):
    st.markdown("""
    *   **`Num_Acc`** : Identifiant de l'accident (identique au fichier Caractéristiques).
    *   **`catr`** : Catégorie de route.
        *   1 - Autoroute
        *   2 - Route nationale
        *   3 - Route Départementale
        *   4 - Voie Communales
        *   5 - Hors réseau public
        *   6 - Parc de stationnement ouvert à la circulation publique
        *   7 - Routes de métropole urbaine
        *   9 - autre voie
    *   **`voie`** : Numéro de la route.
    *   **`v1`** : Indice numérique du numéro de route (ex: 2 bis).
    *   **`v2`** : Lettre indice alphanumérique de la route.
    *   **`circ`** : Régime de circulation.
        *   -1 - Non renseigné
        *   1 - A sens unique
        *   2 - Bidirectionnelle
        *   3 - A chaussées séparées
        *   4 - Avec voies d'affectation variable
    *   **`nbv`** : Nombre total de voies de circulation.
    *   **`vosp`** : Existence d'une voie réservée.
        *   -1 - Non renseigné
        *   0 - Sans objet
        *   1 - Piste cyclable
        *   2 - Bande cyclable
        *   3 - Voie réservée
    *   **`prof`** : Profil en long (déclivité de la route).
        *   -1 - Non renseigné
        *   1 - Plat
        *   2 - Pente
        *   3 - Sommet de côte
        *   4 - Bas de côte
    *   **`pr`** : Numéro du PR de rattachement.
    *   **`pr1`** : Distance en mètres au PR.
    *   **`plan`** : Tracé en plan.
        *   -1 - Non renseigné
        *   1 - Partie rectiligne
        *   2 - En courbe à gauche
        *   3 - En courbe à droite
        *   4 - En « S »
    *   **`lartpc`** : Largeur du terre-plein central (en m).
    *   **`larrout`** : Largeur de la chaussée affectée à la circulation (en m).
    *   **`surf`** : État de la surface.
        *   -1 - Non renseigné
        *   1 - Normale
        *   2 - Mouillée
        *   3 - Flaques
        *   4 - Inondée
        *   5 - Enneigée
        *   6 - Boue
        *   7 - Verglacée
        *   8 - Corps gras - huile
        *   9 - Autre
    *   **`infra`** : Aménagement - Infrastructure.
        *   -1 - Non renseigné
        *   0 - Aucun
        *   1 - Souterrain - tunnel
        *   2 - Pont - autopont
        *   3 - Bretelle d'échangeur ou de raccordement
        *   4 - Voie ferrée
        *   5 - Carrefour aménagé
        *   6 - Zone piétonne
        *   7 - Zone de péage
        *   8 - Chantier
        *   9 - Autres
    *   **`situ`** : Situation de l'accident.
        *   -1 - Non renseigné
        *   0 - Aucun
        *   1 - Sur chaussée
        *   2 - Sur bande d'arrêt d'urgence
        *   3 - Sur accotement
        *   4 - Sur trottoir
        *   5 - Sur piste cyclable
        *   6 - Sur autre voie spéciale
        *   8 - Autres
    *   **`vma`** : Vitesse maximale autorisée.
    """)

# --- Rubrique VEHICULES ---
with st.expander("Fichier VEHICULES : Informations sur les véhicules impliqués", icon = "🚗"):
    st.markdown("""
    *   **`Num_Acc`** : Identifiant de l'accident.
    *   **`id_vehicule`** : Identifiant unique du véhicule.
    *   **`num_Veh`** : Identifiant du véhicule (alphanumérique).
    *   **`senc`** : Sens de circulation.
        *   -1 - Non renseigné
        *   0 - Inconnu
        *   1 - PK ou PR ou numéro d'adresse postale croissant
        *   2 - PK ou PR ou numéro d'adresse postale décroissant
        *   3 - Absence de repère
    *   **`catv`** : Catégorie du véhicule.
        *   00 - Indéterminable
        *   01 - Bicyclette
        *   02 - Cyclomoteur <50cm3
        *   03 - Voiturette (Quadricycle à moteur carrossé)
        *   ... (liste complète dans le PDF, tronquée ici pour concision)
        *   99 - Autre véhicule
    *   **`obs`** : Obstacle fixe heurté.
        *   -1 - Non renseigné
        *   0 - Sans objet
        *   1 - Véhicule en stationnement
        *   2 - Arbre
        *   ... (liste complète dans le PDF)
        *   17 - Buse - tête d'aqueduc
    *   **`obsm`** : Obstacle mobile heurté.
        *   -1 - Non renseigné
        *   0 - Aucun
        *   1 - Piéton
        *   2 - Véhicule
        *   4 - Véhicule sur rail
        *   5 - Animal domestique
        *   6 - Animal sauvage
        *   9 - Autre
    *   **`choc`** : Point de choc initial.
        *   -1 - Non renseigné
        *   0 - Aucun
        *   1 - Avant
        *   2 - Avant droit
        *   ... (liste complète dans le PDF)
        *   9 - Chocs multiples (tonneaux)
    *   **`manv`** : Manœuvre principale avant l'accident.
        *   -1 - Non renseigné
        *   0 - Inconnue
        *   1 - Sans changement de direction
        *   ... (liste complète dans le PDF)
        *   26 - Autres manœuvres
    *   **`motor`** : Type de motorisation du véhicule.
        *   -1 - Non renseigné
        *   0 - Inconnue
        *   1 - Hydrocarbures
        *   2 - Hybride électrique
        *   3 - Electrique
        *   4 - Hydrogène
        *   5 - Humaine
        *   6 - Autre
    *   **`occutc`** : Nombre d'occupants dans le transport en commun.
    """)

# --- Rubrique USAGERS ---
with st.expander("Fichier USAGERS : Informations sur les personnes impliquées", icon = "🕵🏼"):
    st.markdown("""
    *   **`Num_Acc`** : Identifiant de l'accident.
    *   **`id_usager`** : Identifiant unique de l'usager.
    *   **`id_vehicule`** : Identifiant unique du véhicule auquel l'usager est rattaché.
    *   **`num_Veh`** : Identifiant du véhicule (alphanumérique).
    *   **`place`** : Place occupée dans le véhicule. (Détail graphique dans le PDF, ici description textuelle).
        *   10 - Piéton (non applicable)
    *   **`catu`** : Catégorie d'usager.
        *   1 - Conducteur
        *   2 - Passager
        *   3 - Piéton
    *   **`grav`** : Gravité de blessure.
        *   1 - Indemne
        *   2 - Tué
        *   3 - Blessé hospitalisé
        *   4 - Blessé léger
    *   **`sexe`** : Sexe de l'usager.
        *   1 - Masculin
        *   2 - Féminin
    *   **`an_nais`** : Année de naissance de l'usager.
    *   **`trajet`** : Motif du déplacement.
        *   -1 - Non renseigné
        *   0 - Non renseigné
        *   1 - Domicile - travail
        *   2 - Domicile - école
        *   3 - Courses - achats
        *   4 - Utilisation professionnelle
        *   5 - Promenade - loisirs
        *   9 - Autre
    *   **`secu1`, `secu2`, `secu3`** : Équipements de sécurité utilisés (jusqu'à 3 possibles).
        *   -1 - Non renseigné
        *   0 - Aucun équipement
        *   1 - Ceinture
        *   2 - Casque
        *   3 - Dispositif enfants
        *   4 - Gilet réfléchissant
        *   5 - Airbag (2RM/3RM)
        *   6 - Gants (2RM/3RM)
        *   7 - Gants + Airbag (2RM/3RM)
        *   8 - Non déterminable
        *   9 - Autre
    *   **`locp`** : Localisation du piéton.
        *   -1 - Non renseigné
        *   0 - Sans objet
        *   Sur chaussée : 1 - A + 50 m du passage piéton, 2 - A - 50 m du passage piéton
        *   Sur passage piéton : 3 - Sans signalisation lumineuse, 4 - Avec signalisation lumineuse
        *   Divers : 5 - Sur trottoir, 6 - Sur accotement, 7 - Sur refuge ou BAU, 8 - Sur contre allée, 9 - Inconnue
    *   **`actp`** : Action du piéton.
        *   -1 - Non renseigné
        *   0 - Non renseigné ou sans objet
        *   Se déplaçant : 1 - Sens véhicule heurtant, 2 - Sens inverse du véhicule
        *   Divers : 3 - Traversant, 4 - Masqué, 5 - Jouant - courant, 6 - Avec animal, 9 - Autre
        *   A - Monte/descend du véhicule, B - Inconnue
    *   **`etatp`** : État du piéton (seul, accompagné, en groupe).
        *   -1 - Non renseigné
        *   1 - Seul
        *   2 - Accompagné
        *   3 - En groupe
    """)

