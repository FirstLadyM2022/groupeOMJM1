import streamlit as st
import pandas as pd
import seaborn as sns
#from sklearn.neighbors import NearestNeighbors
#import matplotlib.pyplot as plt

# Page Présentation
st.title("Présentation du projet")
st.markdown("*Projet réalisé par: Julie, Mireille, Olmira, Maxime.* Étudiants à la Wild Code School")
st.header("Sujet du Projet")
st.write("Vous êtes un Data Analyst freelance. Un cinéma en perte de vitesse situé dans la Creuse vous contacte. "
            "Il a décidé de passer le cap du digital en créant un site Internet taillé pour les locaux. "
            "Pour aller encore plus loin, il vous demande de créer un moteur de recommandations de films qui à terme, "
            "enverra des notifications aux clients via Internet.")

st.write("Pour l’instant, aucun client n’a renseigné ses préférences, vous êtes dans une situation de cold start. "
            "Mais heureusement, le client vous donne une base de données de films basée sur la plateforme IMDb.")

st.write("Vous allez commencer par proposer une analyse complète de la base de données (Quels sont les acteurs les plus présents ? "
            "À quelle période ? La durée moyenne des films s’allonge ou se raccourcit avec les années ? Les acteurs de série sont-ils "
            "les mêmes qu’au cinéma ? Les acteurs ont en moyenne quel âge ? Quels sont les films les mieux notés ? Partagent-ils des caractéristiques "
            "communes ? etc…)")

st.write("Suite à une première analyse, vous pouvez décider de spécialiser votre cinéma, par exemple sur la « période années 90 », ou alors sur « les films d’action et d’aventure », "
            "afin d'affiner votre exploration.")

st.write("Après cette étape analytique, sur la fin du projet, vous utiliserez des algorithmes de machine learning pour recommander des films en fonction de films "
            "qui ont été appréciés par le spectateur.")

st.write("Le client vous fournit également une base de données complémentaires venant de TMDB, contenant des données sur les pays des boîtes de production, "
            "le budget, les recettes et également un chemin vers les posters des films. Il vous est demandé de récupérer les images des films pour les afficher "
            "dans votre interface de recommandation.")

st.write("Attention ! L’objectif n’est pas de diffuser dans le cinéma les films recommandés. L’objectif final est d’avoir une application avec d’une part des KPI et d’autre "
            "part le système de recommandation avec une zone de saisie de nom de film pour l’utilisateur. Cette application sera mise à disposition des clients du cinéma afin "
            "de leur proposer un service supplémentaire, en ligne, en plus du cinéma classique.")