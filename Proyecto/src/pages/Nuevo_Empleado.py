import streamlit as st
import pandas as pd
from datetime import date
import altair as alt
import matplotlib.pyplot as plt
import os
import openpyxl

# current_dir = os.path.dirname(os.path.realpath(__file__)) 
# path_nuevo_empleado = os.path.join(current_dir, 'data//Data_streamlit.xlsx')

data = pd.read_excel('/app/santander/Proyecto/data/Data_streamlit.xlsx', engine='openpyxl')

st.set_page_config(page_title="Santander People Analytics", page_icon="📊")
st.image("/app/santander/Proyecto/media_stock/Banco_Santander_Logotipo.png")
st.header('TheGoodWay')
st.markdown('---')





gender = st.selectbox('Género', ('Male', 'Female', 'No answer'), key='gender')
age = st.selectbox('Edad', list(range(18, 75, 1)), key='age')
country = st.selectbox('País', ('Spain', 'Other'), key='country')
educ = st.selectbox('Nivel educativo', ('Ninguno', 'Licenciatura', 'Grado','Máster', 'Doctorado') , key='country')

features_button = st.button(label='OK', key='features_button')

if features_button:

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

    
    certificaciones = pd.read_excel('/app/santander/Proyecto/data/Certificaciones.xlsx', sheet_name="certificaciones", engine='openpyxl')
    master = pd.read_excel('/app/santander/Proyecto/data/Certificaciones.xlsx', sheet_name="master", engine='openpyxl')
    idiomas = pd.read_excel('/app/santander/Proyecto/data/Certificaciones.xlsx', sheet_name="idiomas", engine='openpyxl')
    habilidades = pd.read_excel('/app/santander/Proyecto/data/Certificaciones.xlsx', sheet_name="habilidades", engine='openpyxl')


    fig, ax = plt.subplots(2, 2, 
                figsize=(14, 14))
    ax[0][0].bar(certificaciones['Certificaciones'], certificaciones['Importacia'], color='#EA1D25' )
    ax[0][1].bar(master['Master'], master['Importancia'], color='#EA1D25')
    ax[1][0].bar(idiomas['idiomas'], idiomas['Importancia'], color='#EA1D25')
    ax[1][1].bar(habilidades['Habilidades'], habilidades['Importancia'], color='#EA1D25')

    st.pyplot(fig)
