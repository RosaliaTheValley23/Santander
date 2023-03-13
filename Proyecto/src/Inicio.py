import streamlit as st
import pandas as pd
from datetime import date
import plotly
import altair as alt
import matplotlib.pyplot as plt


data = pd.read_excel("../data/Data_streamlit.xlsx")
st.set_page_config(page_title="Santander People Analytics")
st.image("../media_stock/Banco_Santander_Logotipo.png")
st.header('TheGoodWay')
st.markdown('---')


# cd C:\Users\u1132046\OneDrive - IQVIA\Desktop\THE VALLEY\Proyecto\src
# streamlit run Inicio.py

