import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import graphviz

from sklearn import datasets
from sklearn import tree
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

import patsy
import statsmodels.api as sm
import statsmodels.formula.api as smf
import streamlit as st

# Estilo e cabeçalho da página

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

st.markdown('## Modelagem e ánalise pré e pós poda')

#Desenvolvimento do código

renda = pd.read_csv(r"C:\Users\erikd\Projeto\previsao_de_renda.csv")


# Seleção dos dados

renda = renda.drop('Unnamed: 0', axis=1)
renda = renda.drop('id_cliente', axis=1)
renda = renda.drop('data_ref', axis=1)


# Limpeza dos dados

renda.dropna(inplace = True)
renda.reset_index(drop=True,inplace=True)


# Construção

# Transformando a variável tipo_renda em dummies
dummie_tipo_renda = pd.get_dummies(renda['tipo_renda'])

# Transformando a variável educacao em dummies
dummie_educacao = pd.get_dummies(renda['educacao'])

# Transformando a variável estado_civil em dummies
dummie_estado_civil = pd.get_dummies(renda['estado_civil'])

# Transformando a variável tipo_residencia em dummies
dummie_tipo_residencia = pd.get_dummies(renda['tipo_residencia'])

# Retirando as colunas transformadas em Dummie do DF original
renda = renda.drop(['tipo_renda','educacao','estado_civil','tipo_residencia'], axis=1)

# Juntando todos os DF's 
renda_tratado = pd.concat([renda,dummie_tipo_renda,dummie_educacao,dummie_estado_civil,dummie_tipo_residencia], axis=1)


# Formatação

# Transformando a variável sexo para booleanos numéricos
renda_tratado['sexo'] = renda_tratado['sexo'].map({'M':1, 'F':0})

# Transformando a variável posse_de_veiculo para booleanos numéricos
renda_tratado['posse_de_veiculo'] = renda_tratado['posse_de_veiculo'].map({True:1, False:0})

# Transformando a variável posse_de_imovel para booleanos numéricos
renda_tratado['posse_de_imovel'] = renda_tratado['posse_de_imovel'].map({True:1, False:0})

# Renomeando as colunas do DF
renda_tratado.columns = ['sexo', 'posse_de_veiculo', 'posse_de_imovel', 'qtd_filhos', 'idade',
       'tempo_emprego', 'qt_pessoas_residencia', 'renda', 'Assalariado',
       'Bolsista', 'Empresário', 'Pensionista', 'Servidor_público', 'Primário',
       'Pós_graduação', 'Secundário', 'Superior_completo',
       'Superior_incompleto', 'Casado', 'Separado', 'Solteiro', 'União',
       'Viúvo', 'Aluguel', 'Casa', 'Com_os_pais', 'Comunitário', 'Estúdio',
       'Governamental']



# Separando o Data Frame em variáveis explicativas e em variável resposta
y = pd.DataFrame(renda_tratado['renda'])
X = renda_tratado.drop('renda', axis = 1)

# Separando o Data Frame em teste e treino
X_treino, X_teste, y_treino, y_teste = train_test_split(X,y, test_size= 0.3, random_state=0)


analise = st.radio(
    "Selecione a ánalise",
    ["Pré-poda", "Pós-poda"])

if analise == 'Pré-poda':
    # Buscando os melhores parâmetros de poda da árvore
     mses = []
     ind_i = []
     ind_j = []

     for i in range(5, 15):
          for j in range(5, 13):
           regr_1 = DecisionTreeRegressor(max_depth=i, min_samples_leaf=j)
           regr_1.fit(X_treino, y_treino)
           mse1 = regr_1.score(X_teste, y_teste)
           mses.append(mse1)
           ind_i.append(i)
           ind_j.append(j)
     col1, col2 = st.columns([0.6, 1])
     df_mse = pd.DataFrame({'mses':mses, 'profundidade':ind_i, 'n_minimo':ind_j})
     plt.figure(figsize=(10, 10))
     sns.heatmap(df_mse.pivot(index='profundidade', columns='n_minimo', values='mses'))
     st.set_option('deprecation.showPyplotGlobalUse', False)
     col1.pyplot()
     col2.markdown('''# Análise para Pré-poda
                    No HeatMap ao lado, podemos observar o resultado do R-quadrado de acordo com a profundidade 
    definida para a árvore e também com o número minimo de dados para a criação de uma nova
    "Categoria interna" na árvore. Iremos dar sequência a construção da árvore baseado 
    nos melhores resultados apresentados, que são de: Máxima profundidade 14 e 
    número minimo de observações de 9.''')

     col2.markdown('''# Resultado 
                    Seguindo os dados obtidos acima, treinamos a árvore e obtivemos os seguintes resultados:
    R-quadrado na base de treino: 29,11%
    R-quadrado na base de testes: 57,86%''')

elif analise == 'Pós-poda':  

     # Treinando a árvore 
     regr_1 = DecisionTreeRegressor(max_depth = 14, random_state= 0, min_samples_leaf = 9)

     treino_1 = regr_1.fit(X_treino, y_treino)
     teste_1 = regr_1.fit(X_teste, y_teste)

     path = regr_1.cost_complexity_pruning_path(X_treino, y_treino)
     ccp_alphas = path.ccp_alphas


     col1, col2 = st.columns([0.6, 1])
     
     # Impureza da árvore em função do Alpha
     ccp_alphas, impurities = path.ccp_alphas, path.impurities

     plt.figure(figsize=(5,5))     
     plt.plot(ccp_alphas, impurities)
     plt.xlabel('Alpha efetivo')
     plt.ylabel('Impureza')
     st.set_option('deprecation.showPyplotGlobalUse', False)
     col1.pyplot()

     col2.markdown('''# Análise da impureza dos dados pelo Alpha
                    Notamos que quanto maior o Alpha, maior a impureza dos dados.''')
     

     col1, col2 = st.columns([0.6, 1])

     clfs = []

     for ccp_alpha in ccp_alphas:
      clf = DecisionTreeRegressor(random_state = 0, ccp_alpha = ccp_alpha)
      clf.fit(X_treino, y_treino)
      clfs.append(clf)
     # Calculando efetividade do Alpha pela profundidade
     profunfidade_da_árvore = [clf.tree_.max_depth for clf in clfs]
     plt.figure(figsize=(5,5))
     plt.plot(ccp_alphas[:-1], profunfidade_da_árvore[:-1])
     plt.xlabel('Alpha efetivo')
     plt.ylabel('Profundidade da árvore')
     st.set_option('deprecation.showPyplotGlobalUse', False)
     col1.pyplot()

     col2.markdown('''# Análise do Alpha pelaprofundidade da Árvore
                    Notamos que quanto maior o Alpha, maior a impureza dos dados.''')     


     col1, col2 = st.columns([0.6, 1])

     train_scores = [mean_squared_error(y_treino , clf.predict(X_treino)) for clf in clfs]
     test_scores  = [mean_squared_error(y_teste  , clf.predict(X_teste )) for clf in clfs]

     fig, ax = plt.subplots()
     ax.set_xlabel("alpha")
     ax.set_ylabel("MSE")
     ax.set_title("MSE x alpha do conjunto de dados de treino e teste")
     ax.plot(ccp_alphas[:-1], train_scores[:-1], marker='o', label="treino",
        drawstyle="steps-post")
     ax.plot(ccp_alphas[:-1], test_scores[:-1], marker='o', label="teste",
        drawstyle="steps-post")
     ax.legend()
     st.set_option('deprecation.showPyplotGlobalUse', False)
     col1.pyplot()

     col2.markdown('''# Comparação do Alpha e MSE em todas as árvores treinadas 
                    Usaremos um CCP-Alpha de 2.''') 
     












