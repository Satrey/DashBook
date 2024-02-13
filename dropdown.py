import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    html.H1('Hello Dash Application',
            style={
                'color': 'green',
                'fontSize': '40px',
                'fontWeight': 'bold',
                'marginLeft': 'auto',
                'textAlign': 'center',
                'textShadow': '2px 2px 2px black',
            }
            ),
    dcc.Dropdown(
        id='color_dropdown',
        options=[{'label': color, 'value': color}
                    for color in ['blue', 'green', 'yellow', 'orange', 'red']
                ],
        style={
            'boxShadow': '1px 1px 1px gray',
            },
        ),
    html.Div(
        id='color_output'
    ),
])

@app.callback(Output('color_output', 'children'),
                    Input('color_dropdown', 'value'))
def display_selected_color(color):

    if color is None:
        color = 'nothing'
    return 'You selected ' + color


if __name__ == '__main__':
    app.run_server(debug=True)