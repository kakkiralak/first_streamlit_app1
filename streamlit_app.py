import streamlit
import pandas
import snowflake.connector
import requests
from urlib.error import urlerror

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free Range Egg')
streamlit.text('🥑Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list =my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
#streamlit.dataframe(my_fruit_list)
#lets put a pick list so they can pick the fruit they want to pick
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#new section to display fruitvice api response
streamlit.header('Fruitvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Apple')
streamlit.write('The user entered ', fruit_choice)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) # just writes data to screen

# Take the json response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) 
# Output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
#streamlit.stop()

#import snowflake.connector

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute ("SELECT CURRENT_USER(),CURRENT_ACCOUNT(),CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake :")
#streamlit.text(my_data_row)
#Query Some Data
my_cnx = snowflake.connector.connect(**streamlit . secrets["snowflake"])
my_cur = my_cnx. cursor()
my_cur . execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text ("The fruit load list contains:")
#streamlit.text (my_data_row)

streamlit.dataframe (my_data_rows)

fruit_choices = streamlit.text_input('What fruit would you like to add?','jackfruit')

streamlit.text ("Thanks for adding jackfruit")

my_cur.execute("Insert into fruit_load_list values ('from streamlit')")
