import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

server = app.server

app.layout = html.Div([

    # DROPDOWN https://dash.plot.ly/dash-core-components/dropdown
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'Tiger Analytics', 'value': 'TA'},
            {'label': 'Microsoft', 'value': 'MS'},
            {'label': 'TATA', 'value': 'TCS'}
        ],
        value='TA'
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
                options=[
            {'label': 'Tiger Analytics', 'value': 'TA'},
            {'label': 'Microsoft', 'value': 'MS'},
            {'label': 'TATA', 'value': 'TCS'}
        ],
        value=['TA','MS'],
        multi=True
    ),

    # SLIDER https://dash.plot.ly/dash-core-components/slider
    html.Label('Slider'),
    html.P(
    dcc.Slider(
        min=-5,
        max=10,
        step=0.5,
        marks={i: i for i in range(-5,11)},
        value=-3
    )),

    # RADIO ITEMS https://dash.plot.ly/dash-core-components/radioitems
    html.Label('Radio Items'),
    dcc.RadioItems(
               options=[
            {'label': 'Tiger Analytics', 'value': 'TA'},
            {'label': 'Microsoft', 'value': 'MS'},
            {'label': 'TATA', 'value': 'TCS'}
        ],
        value='TA'
    )
], style={'width': '50%'})

if __name__ == '__main__':
    app.run_server()