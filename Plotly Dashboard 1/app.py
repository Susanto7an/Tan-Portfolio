import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


LOGO = "https://images.prismic.io/plotly-marketing-website-2/69e12d6a-fb65-4b6e-8423-9465a29c6028_plotly-logo-lg.png?auto=compress,format"

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags = [{'name': 'viewport',
                    'content': 'width=device-width, initial-scale=1.0'}]
)

sidebar2 = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=False,
            pills=True,
            className="bg-dark",
)


sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-dark",
)

app.layout = dbc.Container([
    html.A(
        dbc.Row([
            dbc.Col(html.Img(src=LOGO, height="25px"))
    ], justify='center'),href="https://plotly.com",
                style={"textDecoration": "none"}),
        dbc.Row([
            dbc.Col(html.Div("Corporacion Favorita Dashboard", className='font-weight-bold text-white',
                             style={'fontSize':50})),
        dbc.Row([
            sidebar2, dash.page_container,
        ])
    ], justify='center'),

], fluid=True)


if __name__ == "__main__":
    app.run(debug=False, port=9000)