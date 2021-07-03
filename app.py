import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image

img = Image.open('image/streamlit/calvin_klein_poster.jpg')
st.image(img, use_column_width='always')

st.title('Amazon Fashion Recommender')

st.write('created by Abraham Leung')  
st.write('-------------------------')

img = Image.open('image/streamlit/abraham_leung_logo.jpg')
st.sidebar.image(img, width=300)

st.sidebar.title('Business Value:')
st.sidebar.write('''
This software will recommend customers with similar fashion products with respect to Calvin Klein's products\n
So companies can advertise their own brands by providing products based on customers' recent preferences
''')

with st.sidebar.beta_expander('Definition'):
    st.write('''
    "Amazon Fashion Recommender" is a machine learning recommendation application.\n
    The product details that used to train the algorithm were collected from the official website of Calvin Klein.\n
    The recommender selects similar Amazon products based on the product names and images.
    ''')
    
st.sidebar.write('-------------------------')
st.sidebar.title('Contact:')

linkedin1, linkedin2 = st.sidebar.beta_columns([1,4])

with linkedin1:
    img = Image.open('image/streamlit/linkedin_logo.png')
    st.image(img, width=30)

with linkedin2:
    link1 = "[Abraham's LinkedIn](https://www.linkedin.com/in/abraham-leung-data-science)"
    st.markdown(link1, unsafe_allow_html=True)

github1, github2 = st.sidebar.beta_columns([1,4])

with github1:
    img = Image.open('image/streamlit/github_logo.png')
    st.image(img, width=30)

with github2:
    link2 = "[Abraham's GitHub](https://github.com/yatfungleung)"
    st.markdown(link2, unsafe_allow_html=True)

# testing for activewear

# load data
df_activewear = pd.read_csv('data/activewear_recommender.csv')

for i in range(len(df_activewear)):

    col0, col1 = st.beta_columns((1,2))

    with col0:
        img = Image.open(df_activewear['img_file'][i])
        st.image(img)

    with col1:
        st.write(df_activewear['name'][i])

    col0, col1, col2, col3 = st.beta_columns((1,2,1,2))

    with col0:
        img = Image.open(df_activewear['recommend_img_file1'][i])
        st.image(img)

    with col1:
        st.write(df_activewear['recommend_name1'][i])
    
    with col2:
        img = Image.open(df_activewear['recommend_img_file2'][i])
        st.image(img)

    with col3:
        st.write(df_activewear['recommend_name2'][i])