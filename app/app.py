import os
import streamlit as st
import pickle

model_dir = os.path.join(os.path.dirname(__file__), "..", "model")
movies = pickle.load(open(os.path.join(model_dir, "movies.pkl"), "rb"))
similarity = pickle.load(open(os.path.join(model_dir, "similarity.pkl"), "rb"))

def recommend(movie):
    
    movie_index = movies[movies["title"]==movie].index[0]

    distances = similarity[movie_index]

    recommended_movies=[]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x:x[1]
    )[1:6]

    for i in movie_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies


st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Choose a movie",
    movies["title"].values
)

if st.button("Recommend"):
    
    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)