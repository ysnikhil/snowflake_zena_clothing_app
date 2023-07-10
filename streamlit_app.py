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

my_cur.execute("select * from catalog_for_website")
list_of_colors=my_cur.fetchall()

#converting the query result, which is like a json to a dataframe for easier accessebility 
df=pd.DataFrame(list_of_colors,columns=['color_or_style','price','direct_url','size_list','upsell_product_desc'])
#st.write("My List of colors: ", df)

selection=st.selectbox('Pick a sweatsuit color or style:', df['color_or_style'].tolist())
st.write("You selected: ", selection)

product_caption='Our Warm, Comfortable, '+ selection+ ' SweatSuit!'
st.write(df.loc[df['color_or_style']==selection,['direct_url']])
#st.write(df['direct_url'])
st.image(df[df['color_or_style']==selection],['direct_url'][0], width=400, caption=product_caption)



