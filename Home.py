import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

def main():
    st.title("HOME PAGE")   
if __name__ == '__main__':
  main()

title1, title2 = st.columns([0.7, 0.3])

with title1 :
  st.header('Projet 2 : Système de recommandation de films')
with title2 :
  "Julie, Mireille, Olmira, Maxime" 
  st.image('/app/groupeomjm1/pages/logo_WCS.png')

#####



A,B,C = st.columns([0.1,0.8,0.1])
with B :
  st.subheader("Wild Code School 2023")
  image = Image.open("notre affiche.png")
  st.image(image, caption='')





