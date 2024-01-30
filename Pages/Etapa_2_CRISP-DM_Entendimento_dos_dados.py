import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt




# Cabeçalho

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Banco X",
     page_icon="https://st3.depositphotos.com/1768926/17672/v/450/depositphotos_176724494-stock-illustration-x-letter-logo-template-vector.jpg",
     layout="wide",
)




# Logo

col1, col2 = st.columns([0.6, 1])
col1.image('https://st3.depositphotos.com/1768926/17672/v/450/depositphotos_176724494-stock-illustration-x-letter-logo-template-vector.jpg',width = 170)
col2.markdown('# Entendimento dos dados')




# Estilo da página

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




# Desenvolvimento da análise

renda = pd.read_csv(r"C:\Users\erikd\Projeto\previsao_de_renda.csv")




# Univariada

st.markdown('### Univariada')

seletor_univariada = st.selectbox(
          '**Selecione a Análise Univariada desejada:**',
          ('Educação', 'Estado civil', 'Gênero', 'Idade', 'Posse de imóvel','Posse de veículo', 'Quantidade de filhos', 'Quantidade de pessoas na residência', 'Tempo de emprego', 'Tipo de renda', 'Tipo de residência'), 
           index = None, placeholder= 'Clique aqui para selecionar a análise desejada')

if seletor_univariada == 'Posse de imóvel':

     col1, col2 = st.columns([0.05, 0.05])

     sns.displot(data= renda, x= 'posse_de_imovel', element = 'step');
     plt.title('Gráfico de distribuição')
     plt.xlabel('Posse de imóvel')
     plt.ylabel('Quantidade')
     col1.pyplot(plt)
     sns.displot(data= renda, x= 'posse_de_imovel', kind= 'ecdf');
     plt.title('Gráfico de proporção')
     plt.xlabel('Posse de imóvel')
     plt.ylabel('Proporção')
     col2.pyplot(plt)

elif seletor_univariada == 'Posse de veículo':     
     col1, col2 = st.columns([0.05, 0.05])

     sns.displot(data= renda, x= 'posse_de_veiculo', element = 'step');
     plt.title('Gráfico de distribuição')
     plt.xlabel('Posse de veículo')
     plt.ylabel('Quantidade')
     col1.pyplot(plt)
     sns.displot(data= renda, x= 'posse_de_veiculo', kind= 'ecdf');
     plt.title('Gráfico de proporção')
     plt.xlabel('Posse de veículo')
     plt.ylabel('Proporção')
     col2.pyplot(plt)

elif seletor_univariada == 'Gênero':     
     col1, col2 = st.columns([0.05, 0.05])

     sns.displot(data= renda, x= 'sexo', element = 'step');
     plt.title('Gráfico de distribuição')
     plt.xlabel('Gênero')
     plt.ylabel('Quantidade')
     col1.pyplot(plt)
     sns.displot(data= renda, x= 'sexo', kind= 'ecdf');
     plt.title('Gráfico de proporção')
     plt.xlabel('Gênero')
     plt.ylabel('Proporção')
     col2.pyplot(plt)

elif seletor_univariada == 'Idade':     
     col1, col2, col3 = st.columns([0.05, 0.05, 0.05])

     sns.displot(data= renda, x= 'idade', element = 'step');
     plt.title('Gráfico de distribuição')
     plt.xlabel('Idade')
     plt.ylabel('Quantidade')
     col1.pyplot(plt)
     sns.displot(data= renda, x= 'idade', kind= 'kde');
     plt.title('Gráfico de densidade')
     plt.xlabel('Idade')
     plt.ylabel('Densidade')
     col2.pyplot(plt)
     sns.displot(data= renda, x= 'idade', kind= 'ecdf');
     plt.title('Gráfico de proporção')
     plt.xlabel('Idade')
     plt.ylabel('Proporção')
     col3.pyplot(plt)

elif seletor_univariada == 'Tempo de emprego':     
     col1, col2, col3 = st.columns([0.05, 0.05, 0.05])

     sns.displot(data= renda, x= 'tempo_emprego', element = 'step');
     plt.title('Gráfico de distribuição')
     plt.xlabel('Tempo de emprego')
     plt.ylabel('Quantidade')
     col1.pyplot(plt)
     sns.displot(data= renda, x= 'tempo_emprego', kind= 'kde');
     plt.title('Gráfico de densidade')
     plt.xlabel('Tempo de emprego')
     plt.ylabel('Densidade')
     col2.pyplot(plt)
     sns.displot(data= renda, x= 'tempo_emprego', kind= 'ecdf');
     plt.title('Gráfico de proporção')
     plt.xlabel('Tempo de emprego')
     plt.ylabel('Proporção')
     col3.pyplot(plt)

elif seletor_univariada == 'Quantidade de filhos':     
     col1, col2, col3 = st.columns([0.05, 0.05, 0.05])

     sns.displot(data= renda, x= 'qtd_filhos', element = 'step');     
     plt.title('Gráfico de distribuição')
     plt.xlabel('Quantidade de filhos')
     plt.ylabel('Quantidade')
     col1.pyplot(plt)
     sns.displot(data= renda, x= 'qtd_filhos', kind= 'kde');
     plt.title('Gráfico de densidade')
     plt.xlabel('Quantidade de filhos')
     plt.ylabel('Densidade')
     col2.pyplot(plt)
     sns.displot(data= renda, x= 'qtd_filhos', kind= 'ecdf');
     plt.title('Gráfico de proporção')
     plt.xlabel('Quantidade de filhos')
     plt.ylabel('Proporção')
     col3.pyplot(plt)

elif seletor_univariada == 'Tipo de renda':     
     col1, col2 = st.columns([0.05, 0.05])

     sns.displot(data= renda, x= 'tipo_renda', element = 'step')
     plt.xticks(rotation=45);
     plt.title('Gráfico de distribuição')
     plt.xlabel('Tipo de renda')
     plt.ylabel('Quantidade')
     col1.pyplot(plt)
     sns.displot(data= renda, x= 'tipo_renda', kind= 'ecdf')
     plt.xticks(rotation=45);
     plt.title('Gráfico de proporção')
     plt.xlabel('Tipo de renda')
     plt.ylabel('Proporção')
     col2.pyplot(plt)

elif seletor_univariada == 'Educação':     
     col1, col2 = st.columns([0.05, 0.05])

     sns.displot(data= renda, x= 'educacao', element = 'step')
     plt.xticks(rotation=50);
     plt.title('Gráfico de distribuição')
     plt.xlabel('Educação')
     plt.ylabel('Quantidade')
     col1.pyplot(plt)
     sns.displot(data= renda, x= 'educacao', kind= 'ecdf')
     plt.xticks(rotation=50);
     plt.title('Gráfico de proporção')
     plt.xlabel('Educação')
     plt.ylabel('Proporção')
     col2.pyplot(plt)

elif seletor_univariada == 'Estado civil':     
     col1, col2 = st.columns([0.05, 0.05])

     sns.displot(data= renda, x= 'estado_civil', element = 'step')
     plt.xticks(rotation=45);
     plt.title('Gráfico de distribuição')
     plt.xlabel('Estado civil')
     plt.ylabel('Quantidade')
     col1.pyplot(plt)
     sns.displot(data= renda, x= 'estado_civil', kind= 'ecdf')
     plt.xticks(rotation=45);
     plt.title('Gráfico de proporção')
     plt.xlabel('Estado civil')
     plt.ylabel('Proporção')
     col2.pyplot(plt)

elif seletor_univariada == 'Tipo de residência':     
     col1, col2 = st.columns([0.05, 0.05])

     sns.displot(data= renda, x= 'tipo_residencia', element = 'step');
     plt.xticks(rotation=45);
     plt.title('Gráfico de distribuição')
     plt.xlabel('Tipo de residência')
     plt.ylabel('Quantidade')
     col1.pyplot(plt)
     sns.displot(data= renda, x= 'tipo_residencia', kind= 'ecdf');
     plt.xticks(rotation=45);
     plt.title('Gráfico de proporção')
     plt.xlabel('Tipo de residência')
     plt.ylabel('Proporção')
     col2.pyplot(plt)

elif seletor_univariada == 'Quantidade de pessoas na residência':     
     col1, col2, col3 = st.columns([0.05, 0.05, 0.05])

     sns.displot(data= renda, x= 'qt_pessoas_residencia', element = 'step');
     plt.title('Gráfico de distribuição')
     plt.xlabel('Quantidade de pessoas na residência')
     plt.ylabel('Quantidade')
     col1.pyplot(plt)
     sns.displot(data= renda, x= 'qt_pessoas_residencia', kind= 'kde');
     plt.title('Gráfico de densidade')
     plt.xlabel('Quantidade de pessoas na residência')
     plt.ylabel('Densidade')
     col2.pyplot(plt)
     sns.displot(data= renda, x= 'qt_pessoas_residencia', kind= 'ecdf')
     plt.title('Gráfico de proporção')
     plt.xlabel('Quantidade de pessoas na residência')
     plt.ylabel('Proporção')
     col3.pyplot(plt)

st.write(' ')
st.write(' ')




# Bivariada

st.markdown('### Bivariadas')

seletor_bivariadas = st.selectbox(
          '**Selecione a Análise Bivariadas desejada:**',
          ('Renda e Educação', 'Renda e Estado civil', 'Renda e Genêro', 'Renda e Idade', 'Renda e Posse de imóvel','Renda e Posse de veículo', 'Renda e Quantidade de filhos', 'Renda e Quantidade de pessoas na residência', 'Renda e Tempo de emprego', 'Renda e Tipo de renda', 'Renda e Tipo de residência'), 
           index = None, placeholder= 'Clique aqui para selecionar a análise desejada')

if seletor_bivariadas == 'Renda e Educação':
     col1, col2 = st.columns([0.07, 0.05])
     sns.barplot(renda, x='educacao', y='renda');
     plt.xticks(rotation=45);
     plt.title('Relação Renda e Educação')
     plt.xlabel('Educação')
     plt.ylabel('Renda')
     col1.pyplot(plt)

elif seletor_bivariadas == 'Renda e Estado civil':
     col1, col2 = st.columns([0.07, 0.05])
     sns.barplot(renda, x='estado_civil', y='renda');
     plt.xticks(rotation=45);
     plt.title('Relação Renda e Estado civil')
     plt.xlabel('Estado civil')
     plt.ylabel('Renda')
     col1.pyplot(plt)
     
elif seletor_bivariadas == 'Renda e Genêro':
     col1, col2 = st.columns([0.07, 0.05])
     sns.barplot(renda, x='sexo', y='renda');
     plt.title('Relação Renda e Genêro')
     plt.xlabel('Genêro')
     plt.ylabel('Renda')
     col1.pyplot(plt)

elif seletor_bivariadas == 'Renda e Idade':
     col1, col2 = st.columns([0.07, 0.05])
     sns.scatterplot(renda, x='idade', y='renda');
     plt.title('Relação Renda e Idade')
     plt.xlabel('Idade')
     plt.ylabel('Renda')
     col1.pyplot(plt)

elif seletor_bivariadas == 'Renda e Posse de imóvel':
     col1, col2 = st.columns([0.07, 0.05])
     sns.barplot(renda, x='posse_de_imovel', y='renda');
     plt.title('Relação Renda e Posse de imóvel')
     plt.xlabel('Posse de imóvel')
     plt.ylabel('Renda')
     col1.pyplot(plt)

elif seletor_bivariadas == 'Renda e Posse de veículo':
     col1, col2 = st.columns([0.07, 0.05])
     sns.barplot(renda, x='posse_de_veiculo', y='renda');
     plt.title('Relação Renda e Posse de veículo')
     plt.xlabel('Posse de veículo')
     plt.ylabel('Renda')
     col1.pyplot(plt)

elif seletor_bivariadas == 'Renda e Quantidade de filhos':
     col1, col2 = st.columns([0.07, 0.05])
     sns.barplot(renda, x='qtd_filhos', y='renda');
     plt.title('Relação Renda e Quantidade de filhos')
     plt.xlabel('Quantidade de filhos')
     plt.ylabel('Renda')
     col1.pyplot(plt)

elif seletor_bivariadas == 'Renda e Quantidade de pessoas na residência':
     col1, col2 = st.columns([0.07, 0.05])
     sns.barplot(renda, x='qt_pessoas_residencia', y='renda');
     plt.title('Relação Renda e Quantidade de pessoas na residência')
     plt.xlabel('Quantidade de pessoas na residência')
     plt.ylabel('Renda')
     col1.pyplot(plt)

elif seletor_bivariadas == 'Renda e Tempo de emprego':
     col1, col2 = st.columns([0.07, 0.05])
     sns.scatterplot(renda, x='tempo_emprego', y='renda');
     plt.title('Relação Renda e Tempo de emprego')
     plt.xlabel('Tempo de emprego')
     plt.ylabel('Renda')
     col1.pyplot(plt)

elif seletor_bivariadas == 'Renda e Tipo de renda':
     col1, col2 = st.columns([0.07, 0.05])
     sns.barplot(renda, x='tipo_renda', y='renda');
     plt.title('Relação Renda e Tipo de renda')
     plt.xlabel('Tipo de renda')
     plt.ylabel('Renda')
     col1.pyplot(plt)

elif seletor_bivariadas == 'Renda e Tipo de residência':
     col1, col2 = st.columns([0.07, 0.05])
     sns.barplot(renda, x='tipo_residencia', y='renda');
     plt.title('Relação Renda e Tipo de residência')
     plt.xlabel('Tipo de residência')
     plt.ylabel('Renda')
     col1.pyplot(plt)
