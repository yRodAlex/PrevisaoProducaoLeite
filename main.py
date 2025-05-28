# Importação das bibliotecas necessárias
import streamlit as st  # Usada para criar a interface web
import pandas as pd     # Manipulação de dados
from statsmodels.tsa.statespace.sarimax import SARIMAX  # Modelo de previsão SARIMAX
from statsmodels.tsa.seasonal import seasonal_decompose  # Decomposição da série temporal
import matplotlib.pyplot as plt  # Visualização de dados
from datetime import date  # Manipulação de datas
from io import StringIO  # Conversão de arquivos enviados para string

# Configuração da página no Streamlit
st.set_page_config(
    page_title="Sistema de Analise e Previsão de Seríes Temporais",
    layout="wide"
)

# Título principal da aplicação
st.title("Sistema de Analise e Previsão de Seríes Temporais")

# Sidebar para o upload do arquivo e entrada de parâmetros
with st.sidebar:
    uploaded_file = st.file_uploader("Escolhe o Arquivo: ", type=['csv'])  # Upload de arquivos .csv

    if uploaded_file is not None:
        # Lê o arquivo carregado e transforma em dataframe
        stringIO = StringIO(uploaded_file.getvalue().decode("utf-8"))
        data = pd.read_csv(stringIO, header=None)  # Sem cabeçalho (1 coluna de dados apenas)

        # Define a data inicial padrão
        data_inicio = date(2000, 1, 1)

        # Entrada da data de início da série pelo usuário
        periodo = st.date_input("Periodo Inicial da Seríe", data_inicio)

        # Entrada do número de meses a prever (1 a 48)
        periodo_previsao = st.number_input(
            "Informe quantos meses quer prever",
            min_value=1, max_value=48, value=12
        )

        # Botão para iniciar o processamento
        processar = st.button("Processar")

# Processamento dos dados e geração dos resultados
if uploaded_file is not None and processar:
    try:
        # Cria uma série temporal com os dados carregados
        ts_data = pd.Series(
            data.iloc[:, 0].values,  # Valores da primeira (e única) coluna
            index=pd.date_range(start=periodo, periods=len(data), freq="ME")  # Frequência mensal (último dia do mês)
        )

        # Decomposição da série temporal (tendência, sazonalidade, ruído)
        decomposicao = seasonal_decompose(ts_data, model='additive')
        fig_decomposicao = decomposicao.plot()
        fig_decomposicao.set_size_inches(10, 8)

        # Criação e ajuste do modelo SARIMAX
        modelo = SARIMAX(ts_data, order=(2, 0, 0), seasonal_order=(0, 1, 1, 12))
        modelo_fit = modelo.fit()

        # Previsão futura da série para o número de meses informado
        previsao = modelo_fit.forecast(steps=periodo_previsao)

        # Geração do gráfico da série com a previsão
        fig_previsao, ax = plt.subplots(figsize=(10, 5))
        ax = ts_data.plot(ax=ax)  # Série original
        previsao.plot(ax=ax, style='r--')  # Previsão (linha tracejada vermelha)

        # Layout da visualização: 3 colunas
        col1, col2, col3 = st.columns([3, 3, 2])

        with col1:
            st.write("Decomposição")
            st.pyplot(fig_decomposicao)  # Exibe gráfico da decomposição

        with col2:
            st.write("Previsão")
            st.pyplot(fig_previsao)  # Exibe gráfico da previsão

        with col3:
            st.write("Dados da Previsão")
            st.dataframe(previsao)  # Tabela com os dados previstos

    except Exception as e:
        # Caso ocorra algum erro, exibe mensagem ao usuário
        st.error(f"Erro ao processar os dados: {e}")

##TESTE