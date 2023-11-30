import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Recommandation")
st.header("Objectif de la Recommandation")
st.write("Bienvenue dans la section de recommandation de films ! Cette fonctionnalité permet aux utilisateurs de découvrir "
            "des films en fonction de leurs préférences. Entrez simplement le genre de film qui vous intéresse, et notre système "
            "vous fournira des recommandations basées sur une analyse approfondie de la base de données de films IMDb. Profitez de "
            "la diversité des recommandations et trouvez des films qui correspondent à vos goûts cinématographiques !")

# Charger les données des films
df_result = pd.read_csv("/app/groupeomjm1/pages/df_rec_maxime.csv", sep=',')
#df_result

# Saisie de l'utilisateur pour le genre
genre_entre_par_utilisateur = st.text_input("Entrez le genre de films que vous recherchez:")

# Bouton pour lancer la recommandation
if genre_entre_par_utilisateur:
    # Faire des prédictions pour le genre donné
    st.write(f"Recommandations de films par genre('{genre_entre_par_utilisateur}'):")
    for i in [0,1,2,3,4]:
        st.write(df_result[df_result['Genre'] ==genre_entre_par_utilisateur][str(i)+" title"].values[0],", noté à ", df_result[df_result['Genre'] ==genre_entre_par_utilisateur][str(i)+" rating"].values[0] )
        #st.write(f"{row['primaryTitle']} : Note: {round(row['weightedScore'], 2)}")
else:
    st.write(f"Veuillez rentrer le genre de film en anglais.")


st.header("Points positifs")
st.write("- Le modèle utilise une approche k-NN pour les recommandations, ce qui peut fournir des résultats pertinents.")
st.write("- Le score pondéré prend en compte à la fois la note moyenne des films et le nombre de votes, offrant ainsi une recommandation plus équilibrée.")
st.write("- La sélection des films se base sur des critères spécifiques, tels que les années 1990 et un nombre minimum de votes, pour des recommandations plus actuelles et populaires.")

# Points négatifs
st.header("Points négatifs")
st.write("- Le modèle k-NN peut ne pas être optimal pour des jeux de données très larges et peut être sensible à la présence de valeurs aberrantes.")
st.write("- Les paramètres tels que la période des années 1990 et le seuil de votes sont définis de manière statique, ce qui peut ne pas convenir à tous les utilisateurs.")

# Idées futures
st.header("Idées futures")
st.write("- Permettre à l'utilisateur de personnaliser davantage ses préférences et affiner les recommandations.")
st.write("- Explorer d'autres algorithmes de recommandation, tels que les méthodes de factorisation de matrices, pour comparer les performances.")
st.write("- Intégrer des informations supplémentaires, telles que les genres spécifiques, pour améliorer la pertinence des recommandations.")
# Page Analyse
