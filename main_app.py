import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import pymysql
import plotly.graph_objects as go
import plotly.express as px

# #########
# Data
# #########

engine = create_engine("mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022")

df_bikes = pd.read_sql(sql='SELECT * FROM edinburgh_bikes limit 200000', con=engine)

# ###########
# Vizualizace
# ###########
st.title('Moje prvni appka')

page = st.sidebar.radio('Select page', ['Mapa', 'Thomson'])

if page  == 'Mapa':
    fig = px.scatter_mapbox(df_temp,lat='start_station_latitude', lon='start_station_longitude', zoom=15, height=600)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

if page == 'Thomson':
    st.write('Thomson sampling')
