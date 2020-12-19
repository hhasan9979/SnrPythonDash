import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
import plotly.express as px
import plotly.io as pio
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
from IPython.display import display, Markdown
from math import pi
import seaborn as sns

########
dff = pd.read_csv("NBAPlayerWinProbability1.csv")
dff = dff.groupby(['Team', 'Player'],as_index=False)[['WPA','SH','TO','FT']].sum()
print (dff[:5])


barchart = px.bar(
    data_frame=dff,
    x="Team",
    y="WPA",
    color="Player",
    opacity=0.9,
    orientation="v",
    barmode='relative',
                  

    labels={"WPA":"Win Probability Added",
    "Player":"Player"},
    title='Win Probability Added for Each Team',
    width=1400,
    height=720,
    template='presentation',            

#pio.show(barchart)
)
########

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
    ]),
    html.Div([
            dcc.Dropdown(id='linedropdown',
                options=[
                         {'label': 'Deaths', 'value': 'deaths'},
                         {'label': 'Cases', 'value': 'cases'}
                ],
                value='deaths',
                multi=False,
                clearable=False
            ),
        ],className='six columns'),

    html.Div([
            dcc.Graph(figure=barchart)
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
