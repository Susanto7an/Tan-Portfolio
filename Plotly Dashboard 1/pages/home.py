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



state_sales_data = pd.read_csv(r'C:\Users\Sven\PycharmProjects\web deployment Dash\datasets\state_sales_data.csv')
store_sales_data = pd.read_csv(r'C:\Users\Sven\PycharmProjects\web deployment Dash\datasets\store_sales_data.csv')
state_sales_quarterly = pd.read_csv(r'C:\Users\Sven\PycharmProjects\web deployment Dash\datasets\state_sales_quarterly')
store_sales_quarterly = pd.read_csv(r'C:\Users\Sven\PycharmProjects\web deployment Dash\datasets\store_sales_quarterly')




bs = 'https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/darkly/bootstrap.min.css'
dash.register_page(__name__,path='/home', name='Home', order=1)
layout = dbc.Container([html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='dropdown', multi=False, value=2013,
                         options=[{'label':x, 'value':x}for x in sorted(state_sales_data['year'].unique())],
                         ),
            dcc.Graph(id='state_bar', figure = {})
        ], width={'size':6, 'offset':0, 'order':1 },
        xs=12, sm=12, md=12, lg=5, xl=5),
        dbc.Col([
            dcc.Dropdown(id='dropdown2', multi=False, value=2013,
                         options=[{'label':x, 'value':x}for x in sorted(store_sales_data['year'].unique())],
                         ),
            dcc.Graph(id='store_pie', figure = {})
        ], width={'size':6, 'offset':0, 'order':2 },
        xs=12, sm=12, md=12, lg=5, xl=5)
    ], justify='around', align='center'),html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='dropdown3', multi=False,
                         value=state_sales_quarterly['state'][0],
                         options=[{'label': x, 'value': x} for x in sorted(state_sales_quarterly['state'].unique())],
                         ),
            dcc.Graph(id='state_line_bar', figure={})
        ], width={'size': 6, 'offset': 0, 'order': 3},
            xs=12, sm=12, md=12, lg=5, xl=5),
        dbc.Col([
            dcc.Dropdown(id='dropdown4', multi=False,
                         value=store_sales_quarterly['store_type'][0],
                         options=[{'label': x, 'value': x} for x in sorted(store_sales_quarterly['store_type'].unique())],
                         ),
            dcc.Graph(id='store_line_bar', figure={})
        ], width={'size': 6, 'offset': 0, 'order': 4},
            xs=12, sm=12, md=12, lg=5, xl=5)
    ], justify='around', align='center'),
], fluid=True)


@callback(
    Output('state_bar', 'figure'),
    Input('dropdown', 'value'))
def state_bar_chart(year):
    dff = state_sales_data.copy()
    dff = dff.sort_values(['year', 'sales'], ascending=[True,True])
    dff = dff[dff['year']==year]
    annotations = [dict(yref='paper', y=0.2, showarrow=False, text = '      ')]
    fig1bar = go.Figure()
    fig1bar.add_trace(trace=go.Bar(y=dff['state'], x=dff['sales'],marker=dict(color='#32cd32'),orientation='h'))
    fig1bar.update_xaxes(showgrid=False)
    fig1bar.update_yaxes(showgrid=False)
    fig1bar.update_layout(title='Average State Sales',
                          height=500, annotations=annotations,
                          hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"),
                          template='plotly_dark',
                          font_family='Arial', font_size=14, font_color='white')
    return fig1bar

@callback(
    Output('store_pie', 'figure'),
    Input('dropdown2', 'value'))
def store_pie_chart(year):
    dff = store_sales_data.copy()
    dff = dff.sort_values(['year', 'sales'], ascending=[True, True])
    dff = dff[dff['year'] == year]
    fig1pie = go.Figure()
    fig1pie.add_trace(go.Pie(values=dff['sales'], labels=dff['store_type'],
                             marker=dict(colors=['#008000','#009900','#00b300','#6aff6a','#ccffcc']),
                             hoverinfo='label+percent+value',textinfo='label+percent', hole=0.7))
    fig1pie.update_layout(title='Store Sales Pie Chart (Average Sales)',
                          height=500,
                          hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"),
                          template='plotly_dark',
                          font_family='Arial', font_size=14, font_color='white',
                          showlegend=False)
    return fig1pie

@callback(
    Output('state_line_bar', 'figure'),
    Input('dropdown3', 'value'))
def state_line_bar(state):
    dff = state_sales_quarterly.copy()
    dff = dff[dff['state'] == state]
    fig1line_bar = go.Figure()
    fig1line_bar.add_trace(go.Scatter(x=dff['month_text'], y=dff['sales'], mode='lines+markers',line={'color':'#ffff00'}))
    fig1line_bar.add_trace(go.Bar(x=dff['month_text'], y=dff['sales'], marker_color='#42d142'))
    fig1line_bar.update_layout(title='Average Monthly Sales (State)',
                               height=500,
                               hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"),
                               template='plotly_dark',
                               font_family='Arial', font_size=14, font_color='white',
                               showlegend=False)
    return fig1line_bar

@callback(
    Output('store_line_bar', 'figure'),
    Input('dropdown4', 'value'))
def store_line_bar(store):
    dff = store_sales_quarterly.copy()
    dff = dff[dff['store_type'] == store]
    fig2line_bar = go.Figure()
    fig2line_bar.add_trace(go.Scatter(x=dff['month_text'], y=dff['sales'], mode='lines+markers',line={'color':'#ffff00'}))
    fig2line_bar.add_trace(go.Bar(x=dff['month_text'], y=dff['sales'], marker_color='#42d142'))
    fig2line_bar.update_layout(title='Average Monthly Sales (Store)',
                               height=500,
                               hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"),
                               template='plotly_dark',
                               font_family='Arial', font_size=14, font_color='white',
                               showlegend=False)
    return fig2line_bar



