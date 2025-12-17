# 📈 Dashboard Macroeconômico - UFFinance

Painel interativo para monitoramento em tempo real dos principais indicadores econômicos do Brasil e dos Estados Unidos.

Desenvolvido como parte das iniciativas de tecnologia da **UFFinance** (Liga de Mercado Financeiro da Universidade Federal Fluminense), com o objetivo de facilitar a visualização de dados macro para as áreas de análise e gestão.

🔗 **Acesse Online:** https://dashboard-uffinance.onrender.com

---

## 📊 Funcionalidades e Dados

O dashboard coleta dados automaticamente de APIs públicas oficiais, trata as séries temporais e gera visualizações interativas.

### 🇧🇷 Brasil
**Fontes:** Banco Central do Brasil (SGS) e IBGE (SIDRA).
* **Política Monetária:** Taxa Selic (Meta) e CDI Mensal.
* **Inflação:** IPCA, IPCA-15 e IGP-M.
* **Atividade Econômica:** PIB Trimestral e IBC-Br (Prévia do PIB).
* **Mercado de Trabalho:** Taxa de Desocupação (PNAD Contínua).

### 🇺🇸 Estados Unidos
**Fonte:** FRED (Federal Reserve Economic Data - St. Louis Fed).
* **Employment:** Non-Farm Payrolls (NFP) e Unemployment Rate.
* **Inflation:** CPI (Consumidor), PCE (Inflação do Fed) e PPI (Produtor).
* **Rates:** Fed Funds Rate (Juros) e Curva de Treasuries (Spread 10Y vs 2Y).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* **[Dash](https://dash.plotly.com/)** (Framework Web para Dados)
* **[Plotly](https://plotly.com/)** (Gráficos Interativos)
* **Pandas** (ETL e Manipulação de Dados)
* **Pandas-DataReader & YFinance** (Coleta de Dados de Mercado)
* **Render** (Hospedagem / Deploy)

---

## 🚀 Como Rodar Localmente

Siga estes passos para executar o dashboard na sua máquina:

1. **Clone o repositório**
   ```bash
   git clone [https://github.com/MatheusWirz/Dashboard-UFFinance.git](https://github.com/MatheusWirz/Dashboard-UFFinance.git)
   cd Dashboard-UFFinance

2. **Crie um ambiente virtual**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
    
   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt

4. **Execute o App**
   ```bash
   python app.py

5. **Acesse o localhost**
   O dashboard estará disponível em: http://127.0.0.1:8050/
