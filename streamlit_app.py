import streamlit as st
import snowflake.connector
import pandas as pd

st.title("Zena's Amazing Athleisure Catalog")


# Connecting to Snowflake
my_cnx=snowflake.connector.connect(**st.secrets["snowflake"])
my_cur=my_cnx.cursor()

#my_cur.execute("SELECT CURRENT_USER(), CURRENT_REGION(), CURRENT_ACCOUNT()")
#my_data_row=my_cur.fetchone()
#st.text("Hello From Snowflake")
#st.text(my_data_row)

my_cur.execute("select color_or_style from catalog_for_website")
list_of_colors=my_cur.fetchall()

#converting the query result, which is like a json to a dataframe for easier accessebility 
df=pd.DataFrame(list_of_colors)
#st.write("My List of colors: ", df)

selection=st.selectbox('Pick a sweatsuit color or style:', df[0].tolist())

#st.text("You selected: ", selection)
