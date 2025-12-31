import streamlit as st
import pickle
import pandas as pd
similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
  recommended = []
  for i in movies_list:
    recommended.append(movies.iloc[i[0]].title)
  return recommended


movies_list = pickle.load(open('m.pkl','rb'))
movies = pd.DataFrame(movies_list)
st.title("Movie Recommend System ")

option = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)

if st.button("Recommend"):
    recommendation = recommend(option)
    for i in recommendation:
       st.write(i)