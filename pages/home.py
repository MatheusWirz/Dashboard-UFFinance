"""
-------------------------------------------------------------------------
Projeto: Dashboard Macroeconômico UFFinance
Arquivo: home.py
Autor:   Matheus Wirz (UFFinance)
Data:    Dezembro, 2025

Descrição: 
    Página inicial onde o usuário poderá escolher o país / categoria que
    deseja monitorar.
-------------------------------------------------------------------------
"""

import dash
from dash import html, dcc

dash.register_page(__name__, path='/', name='Início')

layout = html.Div(className='main-banner', children=[
    html.Div(children=[
        html.H1('Bem vindo ao Dashboard Macro da UFFinance.'),
        html.P('Selecione qualquer categoria para monitorar.'),
        html.Ol('')
    ]),
])