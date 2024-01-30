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

st.write('# Este projeto é a solução para o seguinte problema enfrentado por nós:')

st.markdown('''
            #### O Banco X possui em sua base de dados, informações diversas sobre a vida financeira de seus clientes fornecidas pelos gerentes das contas. A área de risco do banco no entanto detectou que cada vez menos os clientes se sentem confortaveis em revelar a sua renda atual, prejudicando a liberação de crédito saúdavel, já que o banco não sabe a situação financeira do cliente e corre o risco de liberar um valor que o mesmo não consegue arcar, acabando assim sofrendo Defaut. O objetivo deste projeto é a criação e implementação de um modelo que entenda os padrões nos dados já coletados dos cliente do Banco X e seja capaz de prever o valor da renda dos novos clientes captados pelo banco que não informam a sua renda.
            
           
            ''')









