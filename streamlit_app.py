import streamlit

streamlit.title('my parents new healthy dinner')
streamlit.header('Breakfast favourites')

streamlit.text('🥣Omega 3 & blueberry oatmeal')
streamlit.text('🥗kale, spinach & rocket smoothie')
streamlit.text('🐔Hard-boiled free ranged egg')
streamlit.text('🥑🍞Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)


