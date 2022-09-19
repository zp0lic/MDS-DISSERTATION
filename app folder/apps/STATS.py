import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app
import seaborn as sns

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()



dfstats = pd.read_csv(DATA_PATH.joinpath('variablesdataapp.csv'))

variable_stats = ["Carbon, Organic, Dissolved as C :- {DOC}", "pH", "Nitrate as N", "Oxygen, Dissolved as O2"]

layout = html.Div([
    html.H1('Map of Measurements', style={"textAlign": "center"}),

    html.Div([
        
        html.Div([
            html.Pre(children="Year", style={"fontSize":"150%"}),
            dcc.Dropdown(
                id='year-selection', value='Year', clearable=False,
                persistence=True, persistence_type='session',
                options=[{'label': x, 'value': x} for x in sorted(dfstats["Year"].unique())]
            )
        ], className='six columns'),

        html.Div([
            html.Pre(children="pH", style={"fontSize": "150%"}),
            dcc.Dropdown(
                id='variable-selection', value='pH', clearable=False,
                persistence=True, persistence_type='local',
                options=[{'label': x, 'value': x} for x in variable_stats]
            )
            ], className='six columns'),
    ], className='row'),

    dcc.Graph(id='my-stats', figure={})

])

@app.callback(
    Output(component_id='my-stats', component_property='figure'),
    [Input(component_id='year-selection', component_property='value'),
     Input(component_id='variable-selection', component_property='value')
     ]
)

    


def display_value(variable_selection):
    #dfs_fltrd = dfs[dfs.loc[dfs['Year'] == year_chosen]]
    #dfg_fltrd = dfg[(dfg['Year'] == year_chosen)]
    #dfg_fltrd = dfg_fltrd.nlargest(10000, option_chosen) 
    #dfg_fltrd.reset_index(inplace=True)
    #figz = px.scatter_geo(dfg, lon ='Longitude', lat = 'Latitude', color="Location", hover_name="text", size=option_chosen, animation_frame = 'Year')
    #figz.update_geos(fitbounds="geojson")
    #figz.update_layout(
    #title = 'Dissolved Oxygen content in water',
    #geo_scope='europe',)
                     #animation_frame="Year",
                     #animation_group = 'Location'
    #return figz
    return pd.describe(dfstats[variable_selection])
    