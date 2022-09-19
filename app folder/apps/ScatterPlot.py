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

dfv = pd.read_csv(DATA_PATH.joinpath("variabledata.csv"))  
variable_list = ["Carbon, Organic, Dissolved as C :- {DOC}", "pH", "Nitrate as N", "Oxygen, Dissolved as O2"]


layout = html.Div([
    html.H1('Water Quality Analysis', style={"textAlign": "center"}),

    html.Div([
        html.Div(dcc.Dropdown(
            id='location-dropdown', value='Location', clearable=False,
            options=[{'label': x, 'value': x} for x in sorted(dfv.Location.unique())]
        ), className='six columns'),

        html.Div(dcc.Dropdown(
            id='variable-dropdown', value='pH', clearable=False,
            persistence=True, persistence_type='memory',
            options=[{'label': x, 'value': x} for x in variable_list]
        ), className='four columns'),
    ], className='row'),

    dcc.Graph(id='my-bar', figure={}),
])


@app.callback(
    Output(component_id='my-bar', component_property='figure'),
    [Input(component_id='location-dropdown', component_property='value'),
     Input(component_id='variable-dropdown', component_property='value')]
)
def display_value(location_chosen, variable_chosen):
    dfv_fltrd = dfv[dfv['Location'] == location_chosen]
    dfv_fltrd = dfv_fltrd.nlargest(10000, variable_chosen)
    fig = px.scatter(dfv_fltrd, x='Year', y=variable_chosen,trendline="ols", color='Water Type')
    fig = fig.update_yaxes(tickprefix="", ticksuffix="")
    return fig

