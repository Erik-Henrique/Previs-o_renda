import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st



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
col2.markdown('# Dados tratados')



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



# Esclarecimento sobre a página
st.write('# Aqui você tem acesso ao Data frame final que será usado no nosso modelo. Ele já está tratado e no formato correto.')
st.write(' ')
st.write('##### Você pode filtrar o Data Frame, basta indicar o indice inicial e o indice final:') 
st.write(' ')


# Filtro do Data frame
number1 = st.number_input('Indice inicial')
number2 = st.number_input('Indice final')

if number1 == 0 and number2 == 0 :
     st.data_editor(
     renda_tratado,
     column_config={
         "renda": st.column_config.ProgressColumn(
            "renda",
            help="The sales volume in USD",
            format="R$%f",
            min_value=0,
            max_value=245141.67,
        ),
    },
    hide_index=True,
)    
if number1 != 0 or number2 != 0 :
     st.data_editor(
     renda_tratado[int(number1):int(number2)+1],
     column_config={
         "renda": st.column_config.ProgressColumn(
            "renda",
            help="The sales volume in USD",
            format="R$%f",
            min_value=0,
            max_value=245141.67,
        ),
    },
    hide_index=True,
) 



























