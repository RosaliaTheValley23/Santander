import streamlit as st
import pandas as pd



data = pd.read_excel("../data/Data_streamlit.xlsx")
st.set_page_config(page_title="Santander People Analytics")
st.image("../media_stock/Banco_Santander_Logotipo.png")
st.header('TheGoodWay')
st.markdown('---')


