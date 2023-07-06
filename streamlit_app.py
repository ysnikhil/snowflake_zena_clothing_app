import streamlit as st
import snowflake.connector

st.title("Zena's Amazing Athleisure Catalog")

selection=st.selectbox('Pick a sweatsuit color or style:', ('Orange', 'Burgandy'))

st.write('You have selected: ',selection)


my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()

my_cur.execute("SELECT CURRENT_USER(), CURRENT_REGION(), CURRENT_ACCOUNT()")

my_data_row=my_cur.fetchone()

st.text("Hello From Snowflake")
st.text(my_data_row)
