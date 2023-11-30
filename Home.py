import streamlit as st
from PIL import Image

def main():
    st.header("HOME PAGE")
    st.title("Projet 2 -Recommandation de Film pour le cinéma de la Creuse")
    st.subheader("Wild Code School 2023")
    image = Image.open("image d'affiche.png")
    st.image(image, caption='')

if __name__ == '__main__':
    main()



