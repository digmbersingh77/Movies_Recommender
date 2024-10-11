import streamlit as st
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv
import os


def fetch_poster(movie_name):
    os.getenv(api_key)
    url = f'https://omdbapi.com/?t={movie_name}&apikey={api_key}'
    responce = requests.get(url)
    data = responce.json()
    return data['Poster']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key= lambda x:x[1])[1:11]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommended_movies_poster.append(fetch_poster(title))
        recommended_movies.append(title)
    return recommended_movies, recommended_movies_poster

load_dotenv()
similarity  = pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('How would you like', movies['title'].values)
if st.button('Recommend'):
   names, poster = recommend(selected_movie_name)
   col1, col2, col3 = st.columns(3)
   with col1:
       st.header(names[0])
       st.image(poster[0])
   with col2:
       st.header(names[1])
       st.image(poster[1])
   with col3:
       st.header(names[2])
       st.image(poster[2])
   col4, col5, col6 = st.columns(3)
   with col4:
       st.header(names[3])
       st.image(poster[3])
   with col5:
       st.header(names[4])
       st.image(poster[4])
   with col6:
       st.header(names[5])
       st.image(poster[5])
   col7, col8, col9 = st.columns(3)
   with col7:
       st.header(names[6])
       st.image(poster[6])
   with col8:
       st.header(names[7])
       st.image(poster[7])
   with col9:
       st.header(names[8])
       st.image(poster[8])
