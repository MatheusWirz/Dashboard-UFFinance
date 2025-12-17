"""
-------------------------------------------------------------------------
Projeto: Dashboard Macroeconômico UFFinance
Arquivo: app.py
Autor:   Matheus Wirz (UFFinance)
Data:    Dezembro, 2025

Descrição: 
    Arquivo pilar do dashboard, contém os layouts de barra, containers, etc.
-------------------------------------------------------------------------
"""

import dash
from dash import Dash, html, dcc

# Inicializa o app
app = Dash(__name__, use_pages=True)
server = app.server

# o HTML do Dashboard
app.layout = html.Div(className='container', children=[

    html.Div(className='warn-top-bar', children=[
        html.P('É recomendado acessar o dashboard pelo computador')
    ]),

    html.Div(className='top-bar', children=[
        html.Img(src='./assets/logotipo-uffinance.png')
    ]),

    html.Div(className='nav-bar', children=[
        dcc.Link(f"{page['name']}", href=page['relative_path'], className='nav-link')
        for page in dash.page_registry.values()
    ]),

    html.Div(className='conteudo-pagina', children=[
           dash.page_container, # puxando as pages
           
           html.Div(className='grid-menu-home', children=[
                dcc.Link(href=page['relative_path'], className='card-menu', children=[
                    html.H3(page['name'])
                ])
                for page in dash.page_registry.values()
                if page['relative_path'] != '/'
            ]),
    ]),

    html.Div(className='footer', children=[
        html.P('UFFinance - A Liga de Mercado Financeiro da UFF'),
        html.P('Instagram @uffinance'),
        html.P('Linkedin @uffinance'),
        html.P('Universidade Federal Fluminense - 4º Andar - Bloco F')
    ])

])

if __name__ == '__main__':
    app.run(debug=True)