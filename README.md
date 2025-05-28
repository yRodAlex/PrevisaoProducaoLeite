# 📊 Sistema de Análise e Previsão de Séries Temporais

Este é um aplicativo web interativo desenvolvido com **Streamlit** para análise e previsão de séries temporais, utilizando o modelo **SARIMAX**. Ele permite que o usuário carregue um arquivo `.csv` contendo dados mensais (sem cabeçalho) e visualize a decomposição da série e previsões futuras com apenas alguns cliques.

---

## 🔗 Acesse o App Online

Você pode testar o aplicativo diretamente pelo link abaixo:

👉 [Acesse o Sistema de Previsão](https://yrodalex-previsaoproducaoleite-main-bts1hx.streamlit.app/)

---

## 🧰 Tecnologias Utilizadas

- **Python**
- **Streamlit** – Interface web interativa
- **Pandas** – Manipulação de dados
- **Statsmodels** – Modelagem estatística (SARIMAX, decomposição)
- **Matplotlib** – Visualização de gráficos

---

## 🚀 Funcionalidades

- Upload de arquivo `.csv` contendo a série temporal (apenas uma coluna de valores).
- Escolha da data inicial da série.
- Definição do número de meses para previsão (até 48 meses).
- Decomposição da série em tendência, sazonalidade e ruído.
- Modelagem com **SARIMAX**.
- Visualização gráfica da decomposição e previsão.
- Tabela com os valores previstos.

---

## 📁 Formato do Arquivo Esperado

O aplicativo espera arquivos `.csv` **sem cabeçalho**, contendo **apenas uma coluna** com os valores mensais da série.

**Exemplo:**
105.2
108.4
112.1
115.3
...

## 🛠️ Como Rodar Localmente

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

###✅ Requisitos
Crie um arquivo requirements.txt com as seguintes dependências:
streamlit
pandas
statsmodels
matplotlib
