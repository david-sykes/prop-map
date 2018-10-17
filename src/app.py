# -*- coding: utf-8 -*-

import dash, datetime, math, os, sys, argparse
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
from flask import Flask
from utils import db_utils
from utils import sql_generator
from utils import data_parser_helpers as dp
from utils import graph_plot_helpers as gp
import numpy as np
import pandas as pd
import pdb

app = dash.Dash(__name__)
dl = db_utils.DataLoader()
sg = sql_generator.SqlGenerator()
parser = argparse.ArgumentParser()

parser.add_argument('--dataset', help='Define the dataset you want to use')
args = parser.parse_args()
dataset = args.dataset

if dataset:
    sql = sg.get_sql(dataset)
else:
    sql = sg.get_sql('subset')

df = dl.load_data(sql)
df = dp.parse_dates(df)
df = dp.transform_branch_names(df, 10)

mapbox_access_token = os.environ.get('MAPBOX_ACCESS_TOKEN')

app.layout = html.Div(children=[
    html.H1(children='Property Dash'),

    html.Div(children='''
        Map of properties in area
    '''),
    dcc.Dropdown(
                id='feature-dropdown',
                options=[
                    {'label': 'Price', 'value': 'price'},
                    {'label': 'Age', 'value': 'age'},
                    {'label': 'Estate Agent', 'value': 'branch_name'},
                    {'label': 'No. of bedrooms', 'value': 'bedrooms'},
                    {'label': 'Property type', 'value': 'property_subtype'}
                ],
                value="price",
                placeholder="Price",
                className="feature-picker"
            ),
    dcc.Graph(
        id='map-graph',
    )
])

@app.callback(Output("map-graph", "figure"),
              [Input("feature-dropdown", "value")])
def update_map(value):
    datatype = dp.get_data_type(value)
    if datatype == "continuous":
        config = gp.get_continuous_scatter_config(df, value, mapbox_access_token)
        data = [
        go.Scattermapbox(
            lat=df['lat'],
            lon=df['lon'],
            mode='markers',
            marker=config["marker"],
        )
        ]
    else:
        config = gp.get_discrete_scatter_config(df, value, mapbox_access_token)
        data = gp.get_discrete_datasets(df, value)


    return go.Figure(data=data, layout=config["layout"])



if __name__ == '__main__':
    app.run_server()
