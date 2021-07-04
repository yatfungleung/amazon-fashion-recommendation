import streamlit as st
import pandas as pd
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
This software will recommend customers with similar fashion products with respect to Calvin Klein's products they are browsing.\n
So companies can advertise their own brands by providing products based on customers' recent preferences.
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

# create function
# main function
def main(apparel):
    st.write('-------------------------')

    # load data
    df = pd.read_csv(f'data/{apparel}_recommender.csv')

    for i in range(len(df)):

        # ck columns
        col0, col1 = st.beta_columns((1,2))

        with col0:
            # ck product image
            img = Image.open(df['img_file'][i])
            st.image(img)

        with col1:
            # ck logo
            img = Image.open('image/streamlit/calvin_klein_logo.jpg')
            st.image(img, width=100)

            ck_name = df['name'][i]
            ck_price = df['price'][i]

            # ck product name and price
            st.write(ck_name)
            st.write(ck_price, ' \+ Shipping Fee')

            # link to amazon product page
            html = df['url'][i]
            link = f"[More Details]({html})"
            st.markdown(link, unsafe_allow_html=True)

        # amazon columns
        col0, col1, col2, col3 = st.beta_columns((1,2,1,2))

        ck_price = float(ck_price.replace(',','')[4:])

        with col0:
            # amazon product 1 image
            img = Image.open(df['recommend_img_file1'][i])
            st.image(img)

        with col1:
            # amazon logo
            img = Image.open('image/streamlit/amazon_logo.jpg')
            st.image(img, width=70)

            amazon_price = df['recommend_price1'][i]
            
            # amazon prodcut 1 price
            st.write(amazon_price, ' \+ Shipping Fee')

            # show the price difference
            amazon_price = float(amazon_price.replace(',','')[4:])

            price_save = round(ck_price - amazon_price)
            percent = round(price_save / ck_price * 100)

            # show when it is cheaper
            if price_save > 0:
                st.write('You Save: HKD', str(price_save), '(', str(percent), '%)')

            # link to amazon product page
            html = df['recommend_url1'][i]
            link = f"[Buy Now]({html})"
            st.markdown(link, unsafe_allow_html=True)

        
        with col2:
            # amazon product 2 image
            img = Image.open(df['recommend_img_file2'][i])
            st.image(img)

        with col3:
            # amazon logo
            img = Image.open('image/streamlit/amazon_logo.jpg')
            st.image(img, width=70)
            
            amazon_price = df['recommend_price2'][i]
            
            # amazon prodcut 2 price
            st.write(amazon_price, ' \+ Shipping Fee')

            # show the price difference
            amazon_price = float(amazon_price.replace(',','')[4:])

            price_save = round(ck_price - amazon_price)
            percent = round(price_save / ck_price * 100)

            # show when it is cheaper
            if price_save > 0:
                st.write('You Save: HKD', str(price_save), '(', str(percent), '%)')

            # link to amazon product page
            html = df['recommend_url2'][i]
            link = f"[Buy Now]({html})"
            st.markdown(link, unsafe_allow_html=True)
        
        st.write('-------------------------')

st.write('Please Select Apparel:')

# default showing 'sweatshirts-hoodies'
apparel = 'sweatshirts-hoodies'

# buttons for selecting apparel
col0, col1, col2 = st.beta_columns(3)

with col0:
    if st.button('Activewear'):
        apparel = 'activewear'
with col1:
    if st.button('Jackets'):
        apparel = 'jackets'
with col2:
    if st.button('Sweatshirts'):
        apparel = 'sweatshirts-hoodies'

# main function
main(apparel)

