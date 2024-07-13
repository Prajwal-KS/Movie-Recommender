
import pickle
import streamlit as st
import requests
import base64

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:21]:
        
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


with open("data/test.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()  

page_bg_img = f'''
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{encoded_image}");
    background-size: cover;
}}

[data-testid="stHeader"]{{
    background-color: rgba(0, 0, 0, 0);
}}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


st.header('Movie Recommender System Using Machine Learning', divider='rainbow')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    col11, col12, col13, col14, col15 = st.columns(5)
    col16, col17, col18, col19, col20 = st.columns(5)
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
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col9:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col10:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
    with col11:
        st.text(recommended_movie_names[10])
        st.image(recommended_movie_posters[10])
    with col12:
        st.text(recommended_movie_names[11])
        st.image(recommended_movie_posters[11])
    with col13:
        st.text(recommended_movie_names[12])
        st.image(recommended_movie_posters[12])
    with col14:
        st.text(recommended_movie_names[13])
        st.image(recommended_movie_posters[13])
    with col15:
        st.text(recommended_movie_names[14])
        st.image(recommended_movie_posters[14])
    with col16:
        st.text(recommended_movie_names[15])
        st.image(recommended_movie_posters[15])
    with col17:
        st.text(recommended_movie_names[16])
        st.image(recommended_movie_posters[16])
    with col18:
        st.text(recommended_movie_names[17])
        st.image(recommended_movie_posters[17])
    with col19:
        st.text(recommended_movie_names[18])
        st.image(recommended_movie_posters[18])
    with col20:
        st.text(recommended_movie_names[19])
        st.image(recommended_movie_posters[19])

