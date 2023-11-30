import pandas as pd
import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import plotly.express as px
from PIL import Image


#st.header("Données")
st.subheader("Acteurs les Plus Présents dans notre dataset ")
#diagrammes à barres interactifs

df4 = pd.read_csv(r"C:\Users\mirei\Desktop\WildSchool\Projet 2\dossier fait ensemble\Nombre de count_y par primaryName.csv")



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

            image1 = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\pages\Bruce Willis.png")
            st.image(image1 , caption='1er : Bruce Willis')

        with col2 :
            image2 = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\Nicolas cage.png")
            new_image2 = image2.resize((200, 200))
            st.image(new_image2, caption='2ième : Nicolas cage')
        
        with col3 :
           image3 = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\pages\Samuel L. Jackson.png")
           new_image3 = image3.resize((200, 200))
           st.image(new_image3, caption='3ième : Samuel L. Jackson')
        with col4 :
             image4 = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\pages\Gérard Depardieu.png")
             new_image4 = image4.resize((200, 200))
             st.image(new_image4, caption='4ième : Gérard Depardieu')
        with col5 :
            image5 = Image.open(r"C:\Users\mirei\Desktop\dossier streamlit\pages\Dolph Lundgren.png")
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
