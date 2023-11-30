import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

title1, title2 = st.columns([0.7, 0.3])

with title1 :
  st.title('Projet 2 : Système de recommandation de films')
with title2 :
  "Olmira, Mireille, Maxime, Julie" 
  st.image('/app/groupeomjm1/pages/logo_WCS.png')

#####

def main():
    st.header("HOME PAGE")
    st.title("Projet 2 -Recommandation de Film pour le cinéma de la Creuse")

  A,B,C = st.columns(3)
  with B :
    st.subheader("Wild Code School 2023")
    image = Image.open("notre affiche.png")
    st.image(image, caption='')

if __name__ == '__main__':
    main()



