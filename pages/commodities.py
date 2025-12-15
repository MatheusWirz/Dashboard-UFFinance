"""
-------------------------------------------------------------------------
Projeto: Dashboard Macroeconômico UFFinance
Arquivo: commodities.py
Autor:   Matheus Wirz (UFFinance)
Data:    Dezembro, 2025

Descrição: 
    Página que plota dados sobre as commodities.
-------------------------------------------------------------------------
"""

import dash
from dash import html
import functions

dash.register_page(__name__, path='/commodities', name='Commodities')

#--=--
# HTML

layout = html.Div(children=[
    html.H1(className='centered-category', children='Em Construção...')
])