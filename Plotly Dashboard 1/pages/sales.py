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

y_m_st_sa = pd.read_csv(r'C:\Users\Sven\PycharmProjects\web deployment Dash\datasets\y_m_st_sa.csv')

top5_sa_by_state = pd.read_csv(r'C:\Users\Sven\PycharmProjects\web deployment Dash\datasets\top5_sa_by_state.csv')

#########################################################################################################
fig1sunburst = px.sunburst(top5_sa_by_state, path=['state', 'store_type', 'family'], values='sales',
                           title='Sales Volume% by State(Top 5) and Store Type', color='sales',

                           color_continuous_scale=['#004300', '#00cc00', '#91ff91'])

fig1sunburst.update_layout(title_x=0.5,height=850,
                           title_font=dict(size=29, color='#f2f2f2', family="Lato, sans-serif"),
                           template='plotly_dark')
fig1sunburst.data[0].textinfo = 'label+percent entry'
#########################################################################################################


fig1scatter = px.scatter(y_m_st_sa, x='month', y='store_type',
                 color='sales',color_continuous_scale=px.colors.sequential.Greens, size='sales',
                 facet_row='year',
                 title='Average Sales: Store Type vs Year(Month)')

fig1scatter.update_yaxes(ticksuffix='  ', title='Store Type', showgrid=False)
fig1scatter.update_xaxes(tickmode = 'array', tickvals=[i for i in range(1,13)],
                 ticktext=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
                 showgrid=False)
fig1scatter.update_layout(title_x=0.5,height=850, xaxis_title='', yaxis_title='Store Type',
                  margin=dict(t=70, b=0),
                  template='plotly_dark',
                  title_font=dict(size=29, color='#f2f2f2', family="Lato, sans-serif"),
                  font=dict(color='#555'),
                  font_family='Arial', font_size=14, font_color='white',
                  hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"))

dash.register_page(__name__,name='Sales Analysis 2',path='/sales', order=2)

layout = dbc.Container([html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='scatter_plot', figure=fig1scatter)
        ], width={'size': 10, 'offset': 1, 'order': 1},
            xs=10, sm=10, md=10, lg=10, xl=10)],justify='center'),html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='sunburst1', figure=fig1sunburst)
        ], width={'size': 10, 'offset': 0, 'order': 2},
            xs=10, sm=10, md=10, lg=10, xl=10)], justify='center')
],fluid=True)

