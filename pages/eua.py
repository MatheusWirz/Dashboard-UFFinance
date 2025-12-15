"""
-------------------------------------------------------------------------
Projeto: Dashboard Macroeconômico UFFinance
Arquivo: eua.py
Autor:   Matheus Wirz (UFFinance)
Data:    Dezembro, 2025

Descrição: 
    Página que plotas os principais indicadores macroeconômicos dos Estados
    Unidos.
-------------------------------------------------------------------------
"""

import dash
from dash import html
import plotly.graph_objects as go
import functions

dash.register_page(__name__, path='/eua', name='EUA')

#--=--
# Puxando os dados do FRED através da funções em ./functions.py

df_nfp = functions.get_fred_data('PAYEMS', calculo='diferenca_mensal')

df_unrate = functions.get_fred_data('UNRATE')

df_cpi = functions.get_fred_data('CPIAUCSL', calculo='variacao_anual')

df_pce = functions.get_fred_data('PCEPI', calculo='variacao_anual')

df_ppi = functions.get_fred_data('PPIACO', calculo='variacao_anual')

df_fed_funds = functions.get_fred_data('FEDFUNDS')

df_treasury_10y = functions.get_fred_data('DGS10')

df_treasury_2y = functions.get_fred_data('DGS2')

#--=--
# Criando os Gráficos

fig_nfp = functions.criar_grafico('bar', df_nfp, 'data', 'valor', 'Non-Farm Payrolls (Vagas Criadas)')

fig_unrate = functions.criar_grafico('line', df_unrate, 'data', 'valor', 'Taxa de Desemprego (%)')

fig_cpi = functions.criar_grafico('line', df_cpi, 'data', 'valor', 'CPI - Inflação Consumidor (YoY %)')

fig_pce = functions.criar_grafico('line', df_pce, 'data', 'valor', 'PCE - Inflação do FED (YoY %)')

fig_ppi = functions.criar_grafico('line', df_ppi, 'data', 'valor', 'PPI - Inflação do Produtor (YoY %)')

fig_fed = functions.criar_grafico('line', df_fed_funds, 'data', 'valor', 'Fed Funds Rate (Juros)', line_shape='hv')

fig_treasuries = go.Figure()
if not df_treasury_10y.empty:
    fig_treasuries.add_trace(go.Scatter(x=df_treasury_10y['data'], y=df_treasury_10y['valor'], name='10 Anos', line=dict(color='#4e8cff')))
if not df_treasury_2y.empty:
    fig_treasuries.add_trace(go.Scatter(x=df_treasury_2y['data'], y=df_treasury_2y['valor'], name='2 Anos', line=dict(color='#ffaa00')))

fig_treasuries.update_layout(title='Treasuries (Curva de Juros EUA)')
fig_treasuries = functions.style_graph(fig_treasuries)

#--=--
# HTML

layout = html.Div(children=[
    
    html.H1(className='centered-category', children='Estados Unidos'),

    html.Div(className='grid-2-colunas', children=[

        functions.card_grafico(fig_fed),
        functions.card_grafico(fig_treasuries),
        functions.card_grafico(fig_nfp),
        functions.card_grafico(fig_unrate),
        functions.card_grafico(fig_cpi),
        functions.card_grafico(fig_pce),
        functions.card_grafico(fig_ppi),

    ])

])