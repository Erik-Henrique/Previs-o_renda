import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Banco X",
     page_icon="https://st3.depositphotos.com/1768926/17672/v/450/depositphotos_176724494-stock-illustration-x-letter-logo-template-vector.jpg",
     layout="wide",
)

st.image('https://st3.depositphotos.com/1768926/17672/v/450/depositphotos_176724494-stock-illustration-x-letter-logo-template-vector.jpg',width = 170)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://www.castecnologia.com.br/wp-content/uploads/2014/08/background.png");
background-size: cover;
}
[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}
[data-testid="stSidebar"] {
background-image: url("https://www.castecnologia.com.br/wp-content/uploads/2014/08/background.png");
background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown('''
            ## Análise dos resultados
            
            ### Obtivemos os seguintes resultados:

            ##### Na base de treino o R-quadrado foi de 79,91%
            ##### Na base de teste o R-quadrado foi de 88,46%

            ##### Entendemos que o resultado foi satisfatorio pois conseguimos um bom valor de R-quadrado na base de treinos e conseguimos com os ajustes no modelo, obter um R-quadrado de quase 90% na base de testes, mostrando que não há overfitting e com uma otima porcentagem de explicação do fenômeno.
            ''')










