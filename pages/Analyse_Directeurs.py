import pandas as pd
import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import plotly.express as px
from PIL import Image

#st.header("Données")
st.subheader("Directeurs les Plus Présents dans notre dataset ")
#diagrammes à barres interactif

df6 = pd.read_csv(r"C:\Users\mirei\Desktop\WildSchool\Projet 2\dossier fait ensemble\Nombre de tconst par primaryName.csv")



fig = px.bar( data_frame = df6, 
             x= "primaryName",
             y= 'Nombre de tconst',
             color='primaryName',
             labels={'Nombre de tconst': "Nombres de Films", "primaryName" : "Directeurs"},
             width=1000, height=600
)
st.plotly_chart(fig) 

#primaryName,Nombre de tconst


with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:

            image1 = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\Takashi.le1er.png")
            st.image(image1 , caption='1er : Takashi Mikke')

        with col2 :
            image2 = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\sed.2ieme.png")
            new_image2 = image2.resize((200, 200))
            st.image(new_image2, caption='2ième : Soderbergh Steven')
        
        with col3 :
           image3 = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\FrancoisOzon.png")
           new_image3 = image3.resize((200, 200))
           st.image(new_image3, caption='3ième : Ozon François')
        with col4 :
             image4 = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\tsui.png")
             new_image4 = image4.resize((200, 200))
             st.image(new_image4, caption='4ième : Hark Tsui')
        with col5 :
            image5 = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\hong sang soo.png")
            st.image(image5, caption='5ième : Hong Sang-soo')



imagerandom = pd.DataFrame([image1, image2 ,image3 ,image4 ,image5], ["1er", "2ième" ,"3ième" ,"4ième" , "5ième"])

im1, im2, im3, im4, im5 = st.columns(5)



df6
