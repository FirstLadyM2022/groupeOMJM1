import pandas as pd
import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import plotly.express as px

st.set_page_config(layout="wide")

title1, title2 = st.columns([0.7, 0.3])

with title1 :
  st.title('Projet 2 : Système de recommandation de films')
with title2 :
  "Olmira, Mireille, Maxime, Julie" 
  st.image('/app/groupeomjm1/pages/logo_WCS.png')

#####

#diagrammes à barres interactif

df1 = pd.read_csv("/app/groupeomjm1/pages/Nombre de tconst par genres.csv")
st.write(df1)

fig = px.bar( data_frame = df1, 
             x= "genres", 
             y= "Nombre de tconst",
             title = "30 premiers genres de notre dataset",
             color='genres',
             width=1000, height=600
)
st.plotly_chart(fig)
