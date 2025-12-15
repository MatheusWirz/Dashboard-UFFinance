"""
-------------------------------------------------------------------------
Projeto: Dashboard Macroeconômico UFFinance
Arquivo: brasil.py
Autor:   Matheus Wirz (UFFinance)
Data:    Dezembro, 2025

Descrição: 
    Página que plota os principais indicadores macroeconômicos do Brasil.
-------------------------------------------------------------------------
"""

import dash
from dash import html
import functions

dash.register_page(__name__, path='/brasil', name='Brasil')

#--=--
# Puxando os dados do BACEN e do IBGE através da funções em ./functions.py

df_selic = functions.get_bcb_data(1178)

df_di = functions.get_bcb_data(4391)

df_ipca = functions.get_bcb_data(433)

df_ipca_15 = functions.get_bcb_data(7478)

df_pib_tri = functions.get_bcb_data(22099)

df_pnad = functions.get_pnad_data()

df_igp_m = functions.get_bcb_data(189)

df_ibc_br = functions.get_bcb_data(24363)

#--=--
# Criando as variáveis dos gráficos

fig_selic = functions.criar_grafico('line', df_selic, 'data', 'valor', 'Taxa Selic (Meta Copom)', line_shape='hv')

fig_di = functions.criar_grafico('line', df_di, 'data', 'valor', 'CDI Mensal (Rentabilidade %)')

fig_ipca = functions.criar_grafico('bar', df_ipca, 'data', 'valor', 'IPCA (Inflação Oficial Mensal)')

fig_ipca_15 = functions.criar_grafico('bar', df_ipca_15, 'data', 'valor', 'IPCA-15 (Prévia da Inflação)')

fig_pib_tri = functions.criar_grafico('line', df_pib_tri, 'data', 'valor', 'PIB Trimestral')

fig_ibc_br = functions.criar_grafico('line', df_ibc_br, 'data', 'valor', 'IBC-Br (Prévia do PIB Mensal)')

fig_igp_m = functions.criar_grafico('line', df_igp_m, 'data', 'valor', 'IGP-M (Inflação do Aluguel)')

fig_desemprego = functions.criar_grafico('bar', df_pnad, 'Trimestre', 'Desemprego (%)', 'Taxa de Desocupação')

#--=--
# HTML

layout = html.Div(children=[

    html.H1(className='centered-category', children='Brasil'),

    html.Div(className='grid-2-colunas', children=[

        functions.card_grafico(fig_selic),
        functions.card_grafico(fig_di),
        functions.card_grafico(fig_ipca),
        functions.card_grafico(fig_ipca_15),
        functions.card_grafico(fig_pib_tri),
        functions.card_grafico(fig_ibc_br),
        functions.card_grafico(fig_igp_m),
        functions.card_grafico(fig_desemprego),

    ])
])
