import pandas as pd
import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import plotly.express as px

#diagrammes à barres interactif

df1 = pd.read_csv("Nombre de tconst par genres.csv")
st.write(df1)

fig = px.bar( data_frame = df1, 
             x= "genres", 
             y= "Nombre de tconst",
             title = "30 premiers genres de notre dataset",
             color='genres',
             width=1000, height=600
)
st.plotly_chart(fig)
