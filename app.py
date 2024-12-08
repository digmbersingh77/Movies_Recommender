import pickle
import pandas as pd
import streamlit as st
import requests

import os

def fetch_poster(movie_name):
    url = "https://www.omdbapi.com/?t={}&apikey=694ac4b".format(movie_name)
    data = requests.get(url)
    data = data.json()
    return data['Poster']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_name = []
    recommended_movie_poster = []
    for i in distances:
        # fetch the movie poster
        movie_title = movies.iloc[i[0]].title
        recommended_movie_poster.append(fetch_poster(movie_title))
        recommended_movie_name.append(movie_title)

    return recommended_movie_name,recommended_movie_poster


st.header('Movie Recommender System')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown",movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
