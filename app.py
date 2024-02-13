import dash
#import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div(
    [
        html.H1('Hello Dash Application',
                style={
                    'color': 'white',
                    'fontSize': '60px',
                    'fontWeight': 'bold',
                    'marginLeft': 'auto',
                    'textAlign': 'center',
                }
                ),
        html.H2('The World Bank',
                style={
                    'color': 'white',
                    'fontSize': '30px',
                    'fontWeight': 'bold',
                    'marginLeft': 'auto',
                    'textAlign': 'center',
                }
                ),
        dbc.Tabs([
            dbc.Tab([
                html.Ul([
                    html.Li('The World Bank'),
                    html.Li('The World Bank'),
                    html.Li('The World Bank'),
                    html.Li('The World Bank'),
                    html.Li([
                        'Source :', html.A(
                            'https://datacatalog.worldbank.org/search/dataset/0038020',
                            href='https://datacatalog.worldbank.org/search/dataset/0038020',
                        ),
                    ]),
                ]),
            ], label='Key Facts'),
            dbc.Tab([
                html.P('Учитывая ключевые сценарии поведения, постоянное информационно-пропагандистское обеспечение'
                       ' нашей деятельности предоставляет широкие возможности для своевременного выполнения сверхзадачи.'
                       ' Высокий уровень вовлечения представителей целевой аудитории является четким доказательством'
                       ' простого факта: повышение уровня гражданского сознания не оставляет шанса для своевременного'
                       ' выполнения сверхзадачи! Есть над чем задуматься: диаграммы связей формируют глобальную'
                       ' экономическую сеть и при этом — объективно рассмотрены соответствующими инстанциями.')
            ], label='Key News')

        ]),

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
