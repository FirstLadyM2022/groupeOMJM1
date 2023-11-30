import pandas as pd
import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import plotly.express as px
from PIL import Image

st.set_page_config(layout="wide")

title1, title2 = st.columns([0.7, 0.3])

with title1 :
  st.title('Projet 2 : Système de recommandation de films')
with title2 :
  "Olmira, Mireille, Maxime, Julie" 
  st.image('/app/groupeomjm1/pages/logo_WCS.png')

#st.header("Données")
st.subheader("Acteurs les Plus Présents dans notre dataset ")
#diagrammes à barres interactifs

df4 = pd.read_csv("/app/groupeomjm1/pages/Nombre de count_y par primaryName.csv")



fig = px.bar( data_frame = df4, 
             x= "primaryName",
             y= 'Nombre de count_y',
             color='primaryName',
             labels={'Nombre de count_y': "Nombres de Films", "primaryName" : "Acteurs"},
             width=1000, height=600
)
st.plotly_chart(fig) 


with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:

            image1 = Image.open("/app/groupeomjm1/pages/Bruce Willis.png")
            st.image(image1 , caption='1er : Bruce Willis')

        with col2 :
            image2 = Image.open("/app/groupeomjm1/pages/Nicolas cage.png")
            new_image2 = image2.resize((200, 200))
            st.image(new_image2, caption='2ième : Nicolas cage')
        
        with col3 :
           image3 = Image.open("/app/groupeomjm1/pages/Samuel L. Jackson.png")
           new_image3 = image3.resize((200, 200))
           st.image(new_image3, caption='3ième : Samuel L. Jackson')
        with col4 :
             image4 = Image.open("/app/groupeomjm1/pages/Gérard Depardieu.png")
             new_image4 = image4.resize((200, 200))
             st.image(new_image4, caption='4ième : Gérard Depardieu')
        with col5 :
            image5 = Image.open("/app/groupeomjm1/pages/Dolph Lundgren.png")
            st.image(image5, caption='5ième : Dolph Lundgren')



imagerandom = pd.DataFrame([image1, image2 ,image3 ,image4 ,image5], ["1er", "2ième" ,"3ième" ,"4ième" , "5ième"])

im1, im2, im3, im4, im5 = st.columns(5)


#filteredImages: [image1, image2 ,image3 ,image4 ,image5] # your images here
#caption = ["1er","2ième","3ième","4ième", "5ième"] # your caption here



#primaryName,Nombre de count_y
###############################################
#"1er"
#image = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\pages\Bruce Willisj.peg.jpeg")
#st.image(image, caption='')

###############################################
#"2ième"
#image = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\pages\nicolas_cage.png")
#st.image(image, caption='')
###############################################
#"3ième"
#image = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\pages\Samuel L. Jackson.jpg")
#st.image(image, caption='')
###############################################
#"4ième"
#image = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\pages\Gérard Depardieu.jpeg")
#st.image(image, caption='')
###############################################
#"5ième"
#image = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\pages\Dolph Lundgren.jpeg")
#st.image(image, caption='')

"Dataset"
st.write(df4)
