"""
-------------------------------------------------------------------------
Projeto: Dashboard Macroeconômico UFFinance
Arquivo: functions.py
Autor:   Matheus Wirz (UFFinance)
Data:    Dezembro, 2025

Descrição: 
    Agrupei aqui as funções para tornar o processo de criação de gráficos,
    requisições e etc mais rápido.
-------------------------------------------------------------------------
"""

import pandas as pd
import requests
from dash import html, dcc
import plotly.express as px
import datetime
import pandas_datareader.data as web

#--=--
# Funções de estilo

def style_graph(fig):
    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)', 
        font={'family': "Google Sans Flex", 'color': "#f0f0f0"},
        margin=dict(l=40, r=20, t=40, b=40),
        hovermode="x unified"
    )
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor='#333333', zeroline=False)
    return fig

def criar_grafico(tipo, df, x, y, titulo, **kwargs):
    if tipo == 'area':
        fig = px.area(df, x=x, y=y, title=titulo, **kwargs)
    elif tipo == 'bar':
        fig = px.bar(df, x=x, y=y, title=titulo, **kwargs)
    else:
        fig = px.line(df, x=x, y=y, title=titulo, **kwargs)
    
    return style_graph(fig)


def card_grafico(figura):
    return html.Div(className='card', children=[
        dcc.Graph(figure=figura, config={'displayModeBar': False})
    ])


#--=--
# Funções para puxar dados de APIs

def get_bcb_data(codigo_serie, data_inicial_anos=10):
    # Puxa dados da API do BACEN 
    # Apenas aceita dados em um limite de 10 anos 
    try:
        # Cada indice tem um código de série
        url=f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json'

        data_inicial = datetime.datetime.now() - datetime.timedelta(days=365*data_inicial_anos)

        data_inicial = data_inicial.strftime('%d/%m/%Y')

        url += f'&dataInicial={data_inicial}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        df = pd.DataFrame(response.json())
        df['data'] = pd.to_datetime(df['data'], dayfirst=True)
        df['valor'] = df['valor'].astype(float)

        return df
    
    except Exception as e:
        print(f'Erro BCB: {e}')
        return pd.DataFrame()
    
def get_pnad_data():
    # Puxa dados da API do IBGE (SIDRA)
    # PNAD - Taxa de Desocupação e Renda Média - tabela 6381
    try:
        url = "https://apisidra.ibge.gov.br/values/t/6381/n1/all/v/4099/p/last%2013"
        
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        df = pd.DataFrame(data)
        
        # Limpeza do cabeçalho do SIDRA
        df.columns = df.iloc[0]
        df = df[1:].copy()
        
        # Seleciona apenas data e valor
        # 'Trimestre Móvel (Código)' vem como '202401'
        df = df[['Trimestre Móvel (Código)', 'Valor']].copy()
        df.columns = ['data_ref', 'Desemprego (%)']
        
        # Converte para número
        df['Desemprego (%)'] = pd.to_numeric(df['Desemprego (%)'], errors='coerce')
        
        def formatar_data(x):
            try:
                return f"{x[-2:]}/{x[:4]}" # Pega os 2 últimos (mês) e os 4 primeiros (ano)
            except:
                return x
                
        df['Trimestre'] = df['data_ref'].apply(formatar_data)
        
        return df[['Trimestre', 'Desemprego (%)']]
    
    except Exception as e:
        print(f'Erro BCB: {e}')
        return pd.DataFrame()

def get_fred_data(code, data_inicial_anos=5, calculo=None):
    # puxa dados do FRED (Federal Reserve) pelo pandas datareader
    # Calculo pode ser pce_anual, diferenca_mensal, etc
    try:
        start = datetime.datetime.now() - datetime.timedelta(days=365*data_inicial_anos)
        end = datetime.datetime.now()

        df = web.DataReader(code, 'fred', start, end)
        df = df.reset_index()
        df.columns = ['data', 'valor']

        if calculo == 'variacao_anual': # i.e % YoY
            df['valor'] = df['valor'].pct_change(periods=12) * 100

        if calculo == 'diferenca_mensal': # i.e saldo
            df['valor'] = df['valor'].diff() * 1000
        
        df = df.dropna()

        return df
    
    except Exception as e:
        print(f'Erro FRED: {e}')
        return pd.DataFrame()