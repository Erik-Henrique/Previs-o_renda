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


st.write('# Seja bem vindo ao seu útlimo Banco')

st.write('')


st.markdown('''
            #### Nós do Banco X estamos sempre buscando melhorar a qualidade dos nossos serviços, pensando nisso, construimos este modelo de Machine Learning para resolver um dos nossos maiores problemas.
            ''')

st.write('')

st.markdown('#### **👈 Para saber mais sobre, clique sobre a barra lateral e analise o passo a passo do projeto, junto com algumas informações sobre o nosso negócio.**')








