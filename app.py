import streamlit as st
import pickle
import pandas as pd


df = pickle.load(open('df.pkl', 'rb'))
df = pd.DataFrame(df)

similarity = pickle.load(open('similarity.pkl', 'rb'))
similarity = pd.DataFrame(similarity)


def get_index(name):
  return df[df['title'] == name].index[0]


def recc(movie):
    mlist = []
    index = get_index(movie)
    l = similarity[index]
    movie_list = sorted(list(enumerate(l)), reverse = True, key = lambda x:x[1])[1:6]
    for i in movie_list:
        mlist.append(df.iloc[i[0]].title)
    return mlist




st.title("Movie Reccomender System")

option = st.selectbox(
    'How would you like to be contacted?',
    df['title'].values)


st.button("Reset", type="primary")
if st.button('Enter'):
    st.write([x for x in recc(option)])


st.write('You selected:', option)