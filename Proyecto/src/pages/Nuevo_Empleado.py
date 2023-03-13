import streamlit as st
import pandas as pd
from datetime import date
import altair as alt
import matplotlib.pyplot as plt


data = pd.read_excel("../data/Data_streamlit.xlsx")
st.set_page_config(page_title="Santander People Analytics", page_icon="📊")
st.image("../media_stock/Banco_Santander_Logotipo.png")
st.header('TheGoodWay')
st.markdown('---')





gender = st.selectbox('Gender?', ('Male', 'Female', 'No answer'), key='gender')
age = st.selectbox('How old are you?', list(range(18, 75, 1)), key='age')
country = st.selectbox('Where are you from?', ('Spain', 'Other'), key='country')

features_button = st.button(label='OK', key='features_button')

if features_button:
    st.write(f"gender: {gender}")
    st.write(f"age: {age}")
    st.write(f"country: {country}")

    # Horizontal stacked bar chart
    source = st.session_state.data[['ID_empleado', 'status']]
    
    threshold = pd.DataFrame([{"total": 100}])

    rule = alt.Chart(threshold).mark_rule().encode(
        x='total:Q'
    )


    bars = alt.Chart(source).mark_bar(color='#FF0000').encode(
        x='status:Q',
        y="ID_empleado:O"
    )
    text = bars.mark_text(
        align='left',
        baseline='middle',
        # dx=3  # Nudges text to right so it doesn't appear on top of the bar
    ).encode(
        text='status:Q'
    )
    
    rule = alt.Chart(threshold).mark_rule().encode(
        x='total:Q'
    )

    st.write("Porcentaje Accuracy Upskilling")
    st.altair_chart(bars + text + rule)

    certificaciones = pd.read_excel("../data/Certificaciones.xlsx", sheet_name="certificaciones")
    master = pd.read_excel("../data/Certificaciones.xlsx", sheet_name="master")
    idiomas = pd.read_excel("../data/Certificaciones.xlsx", sheet_name="idiomas")
    habilidades = pd.read_excel("../data/Certificaciones.xlsx", sheet_name="habilidades")



    
    certificaciones = pd.read_excel("C:/Users/u1132046/OneDrive - IQVIA/Desktop/THE VALLEY/Proyecto/data/Certificaciones.xlsx", sheet_name="certificaciones")
    master = pd.read_excel("C:/Users/u1132046/OneDrive - IQVIA/Desktop/THE VALLEY/Proyecto/data/Certificaciones.xlsx", sheet_name="master")
    idiomas = pd.read_excel("C:/Users/u1132046/OneDrive - IQVIA/Desktop/THE VALLEY/Proyecto/data/Certificaciones.xlsx", sheet_name="idiomas")
    habilidades = pd.read_excel("C:/Users/u1132046/OneDrive - IQVIA/Desktop/THE VALLEY/Proyecto/data/Certificaciones.xlsx", sheet_name="habilidades")


    fig, ax = plt.subplots(2, 2, 
                figsize=(14, 14))
    ax[0][0].bar(certificaciones['Certificaciones'], certificaciones['Importacia'], color='#EA1D25' )
    ax[0][1].bar(master['Master'], master['Importancia'], color='#EA1D25')
    ax[1][0].bar(idiomas['idiomas'], idiomas['Importancia'], color='#EA1D25')
    ax[1][1].bar(habilidades['Habilidades'], habilidades['Importancia'], color='#EA1D25')

    st.pyplot(fig)
