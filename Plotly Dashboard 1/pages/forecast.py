import dash
import pandas as pd
import numpy as np
import calendar
import os

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

data = pd.read_csv(r'C:\Users\Sven\PycharmProjects\normal_dash FINAL\datasets\combined_forecast.csv', low_memory=False)
state_list = data.state.unique()



dash.register_page(__name__,path='/forecast', name='Sales Forecast', order=3)
layout = dbc.Container([html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='dropdown5', multi=False, value='Azuay',
                         options=[{'label':x, 'value':x}for x in sorted(data['state'].unique())],
                         ),
            dcc.Graph(id='forecast_line', figure = {})
        ], width={'size':12, 'offset':0, 'order':1 },
        xs=12, sm=12, md=12, lg=12, xl=12),
    ], justify='around', align='center'),html.Br(),
], fluid=True)

@callback(
    Output('forecast_line', 'figure'),
    Input('dropdown5', 'value'))

def sales_forecast_line(state_list):
    dff = data.copy()
    dff = dff[dff['state']== state_list]
    fig1forecast = go.Figure()
    fig1forecast.add_trace(go.Scatter(x=dff['ds'], y=dff['yhat'], mode='lines', line=dict(color='#32cd32')))
    fig1forecast.update_xaxes(showgrid=False, linecolor='#FFFFFF')
    fig1forecast.update_yaxes(showgrid=False, linecolor='#FFFFFF')
    fig1forecast.update_layout(title='State Sales Forecast (1 year)',
                               height=500,
                               hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"),
                               template='plotly_dark',
                               font_family='Arial', font_size=14, font_color='white',
                               showlegend=False)
    return fig1forecast
