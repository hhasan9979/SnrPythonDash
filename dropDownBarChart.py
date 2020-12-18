import pandas as pd     #(version 1.0.0)
import plotly           #(version 4.5.4) #pip install plotly==4.5.4
import plotly.express as px
import plotly.io as pio
import dash
import dash_core_components as dcc
import dash_html_components as html

# excel sheet from https://www.kaggle.com/rajanand/prison-in-india/data
# National Crime Records Bureau (NCRB), Govt of India has shared this dataset
dff = pd.read_csv("Caste.csv")
dff = dff[dff['state_name']=='Maharashtra']
dff = dff.groupby(['year','gender',],as_index=False)[['detenues','under_trial','convicts','others']].sum()
print (dff[:5])


barchart = px.bar(
    data_frame=dff,
    x="year",
    y="convicts",
    color="gender",               # differentiate color of marks
    opacity=0.9,                  # set opacity of markers (from 0 to 1)
    orientation="v",              # 'v','h': orientation of the marks
    barmode='relative',           # in 'overlay' mode, bars are top of one another.
                                  # in 'group' mode, bars are placed beside each other.
                                  # in 'relative' mode, bars are stacked above (+) or below (-) zero.
    #----------------------------------------------------------------------------------------------


    labels={"convicts":"Convicts in Maharashtra",
    "gender":"Gender"},           # map the labels of the figure
    title='Indian Prison Statistics', # figure title
    width=1400,                   # figure width in pixels
    height=720,                   # figure height in pixels
    template='gridon',            # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',


#pio.show(barchart)
)

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Div([
        html.H1('Title')
    ]),
    html.Div([
        dcc.Graph(figure=barchart)
    ])
])
