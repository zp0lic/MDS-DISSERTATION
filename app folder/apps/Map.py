import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()



dfg = pd.read_csv(DATA_PATH.joinpath("variablesdataapp.csv"))
variable_map = ["Carbon, Organic, Dissolved as C :- {DOC}", "pH", "Nitrate as N", "Oxygen, Dissolved as O2"]
layout = html.Div([
    html.H1('Map of Measurements', style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.Pre(children="Year", style={"fontSize":"150%"}),
            dcc.Dropdown(
                id='year-dropdown', value='Year', clearable=False,
                persistence=True, persistence_type='session',
                options=[{'label': x, 'value': x} for x in sorted(dfg["Year"].unique())]
            )
        ], className='six columns'),

        html.Div([
            html.Pre(children="pH", style={"fontSize": "150%"}),
            dcc.Dropdown(
                id='pH-dropdown', value='Variable', clearable=False,
                persistence=True, persistence_type='local',
                options=[{'label': x, 'value': x} for x in variable_map]
            )
            ], className='six columns'),
    ], className='row'),

    dcc.Graph(id='my-map', figure={}),
])


@app.callback(
    Output(component_id='my-map', component_property='figure'),
    [Input(component_id='year-dropdown', component_property='value'),
     Input(component_id='pH-dropdown', component_property='value')]
)

def display_value(option_chosen, year_chosen):
    #dfg_fltrd = dfg[dfg.loc[df['Year'] == year_chosen]]
    #dfg_fltrd = dfg[(dfg['Year'] == year_chosen)]
    #dfg_fltrd = dfg_fltrd.nlargest(10000, option_chosen) 
    #dfg_fltrd = dfg_fltrd.groupby(["Customer State"])[['Sales']].sum()
    #dfg_fltrd.reset_index(inplace=True)
    figz = px.scatter_geo(dfg, lon ='Longitude', lat = 'Latitude', color="Location", hover_name="text", size="Oxygen, Dissolved as O2", animation_frame = 'Year')
    figz.update_geos(fitbounds="geojson")
    figz.update_layout(
    title = 'Variable measurement in water',
    geo_scope='europe',)
                     #animation_frame="Year",
                     #animation_group = 'Location'
    return figz
