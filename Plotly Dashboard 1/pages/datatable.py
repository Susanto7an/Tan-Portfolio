import pandas as pd
from pandas.api.types import CategoricalDtype
import plotly.express as px
import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table

df = pd.read_csv(r'C:\Users\Sven\PycharmProjects\normal_dash FINAL\datasets\datatable.csv')



dash.register_page(__name__,path='/datatable', name='Datatable', order=4)

layout = html.Div([ html.Br(),
    dash_table.DataTable(
        id='datatable-interactivity',
        columns = [
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
        ],
        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': 'rgb(50, 50, 50)',
            'color': 'white'
        },
        data=df.to_dict('records'),  # the contents of the table
        editable=True,  # allow editing of data inside all cells
        filter_action="native",  # allow filtering of data by user ('native') or not ('none')
        sort_action="native",  # enables data to be sorted per-column by user or not ('none')
        sort_mode="single",  # sort across 'multi' or 'single' columns
        cell_selectable=False,
        column_selectable="multi",  # allow users to select 'multi' or 'single' columns
        row_selectable="multi",  # allow users to select 'multi' or 'single' rows
        row_deletable=True,  # choose if user can delete a row (True) or not (False)
        selected_columns=[],  # ids of columns that user selects
        selected_rows=[],  # indices of rows that user selects
        page_action="native",  # all data is passed to the table up-front or not ('none')
        page_current=0,  # page number that user is on
        page_size=7,  # number of rows visible per page
        style_cell={  # ensure adequate header width when text is shorter than cell's text
            'minWidth': 95, 'maxWidth': 95, 'width': 95
        },
    ),
    html.Br(),
    html.Br(),
    html.Div(id='bar-container'),
])


@callback(
    Output('bar-container', "children"),
    Input('datatable-interactivity', "derived_virtual_data"),
    Input('datatable-interactivity', "derived_virtual_selected_rows"))
def update_graph(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = df if rows is None else pd.DataFrame(rows)

    # used to highlight selected day of week on bar chart
    colors = ['#ffff00' if i in derived_virtual_selected_rows else '#00cc00'
              for i in range(len(dff))]

    if "Year" in dff and "Sales" in dff:
        return [
            dcc.Graph(id='bar-chart',
                      figure=px.bar(
                          data_frame=dff,
                          x="Year",
                          y='Sales',
                          hover_data=['Day of Week', 'Sales']
                      ).update_xaxes(linecolor='#FFFFFF').update_yaxes(showgrid=False,linecolor='#FFFFFF')\
                      .update_layout(title='Average Yearly Sales (Day of Week)',
                                      template='plotly_dark',
                                      hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"),
                                      showlegend=False,
                                      xaxis={'categoryorder': 'total ascending'})
                      .update_traces(marker_color=colors)
                      )
        ]





