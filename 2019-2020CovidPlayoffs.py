import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/hhasan9979/hhasan9979.github.io/main/PlayoffStatsPre%26PostBubble.csv')
goats = ['Michael Jordan','Lebron James','Magic Johnson','Larry Bird','Tim Duncan','Shaquille']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.Div([
        html.H1('2019 Playoffs vs. 2020 Bubble Playoffs')
    ]),
    html.Div([
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            id='Year-slider',
            min=df['Num'].min(),
            max=df['Num'].max(),
            value=df['Num'].min(),
            marks={str(Year): str(Year) for Year in df['Num'].unique()},
            step=None
        )
    ])
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('Year-slider', 'value')])
def update_figure(selected_Year):
    filtered_df = df[df.Num == selected_Year]

    fig = px.scatter(filtered_df, x="FG%", y="AST",
                     size="PTS", color="YEAR", hover_name="PLAYER",
                     log_x=True, size_max=40)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
