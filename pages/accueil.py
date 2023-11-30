import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(layout="wide")

title1, title2 = st.columns(0.7,0.3)

with title1 :
  st.title('Projet 2 : Système de recommandation de films')
with title2 :
  "Olmira, Mireille, Maxime, Julie" 
image = Image.open("/app/groupeomjm1/pages/logo_WCS.png")
st.image(image, caption='')

st.title('Première partie : Analyse de données')

st.write("Il nous a été demandé premièrement de nettoyer et analyser une base de données contenant les caractérisqtiques de nombreux films, et d'en extraire une selection à proposer à un cinéma Français en perte de vitesse.")

st.title('Seconde partie : Machine Learning')

st.write("La deuxième tâche qui nous a été confiée consiste en la création d'un modèle de Machine Learning permettant de recommander des films en fonction d'une choix de film par l'utilisateur.")
