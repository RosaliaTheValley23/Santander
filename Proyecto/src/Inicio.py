import streamlit as st
import pandas as pd
import os

current_dir = os.path.dirname(os.path.realpath(__file__)) 
# path_imagen = os.path.join(current_dir, 'media_stock/Banco_Santander_Logotipo.png')

st.set_page_config(page_title="Santander People Analytics")
st.image(path_imagen)
st.header('TheGoodWay')
st.markdown('---')


