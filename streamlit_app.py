import streamlit as st
import snowflake.connector

st.title("Zena's Amazing Athleisure Catalog")

selection=st.selectbox('Pick a sweatsuit color or style:', ('Orange', 'Burgandy'))

st.write('You have selected: ',selection)
