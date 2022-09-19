import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app
import dash
import dash_bootstrap_components as dbc


#File Imports
from app import app

layout =html.Div([
        dbc.Row([
        html.Div([
            html.Header([
                html.H4("North Pennines AONB Dashboard App Project"),
                html.H5(["This dashboard is part of an ongoing project to collate and visualise water quality data from the North Pennines. The North Pennines is an area of outstanding natural beauty and ecological importance. The dashboard presented here can be seen as an initial developed concept for the project. This design demonstrates what the app is capable of, and helps envisage the path for future works.",
                html.Br(), html.Br(), "All the data used for this project is publicly available from the Water Quality Archive via the ", html.A(" Environment Agency website.", href ="https://environment.data.gov.uk/water-quality/view/download/new", id="linkInText")]),

            ])
        ], style={ "margin-top": "3rem", "margin-right": "0.5rem",  "margin-left": "1.5rem"})
    ]),
        dbc.Row([
            dbc.Col([
                html.Div([html.Hr()], id = "horizontalLine"),
                