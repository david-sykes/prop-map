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

external_stylesheets=[ "https://fonts.googleapis.com/css?family=Raleway:400,600" ]
external_scripts = [    {
        'src': "https://code.jquery.com/jquery-3.3.1.min.js",
        'integrity': "sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=",
        'crossorigin': "anonymous"
    }]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=external_scripts)
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
    html.Div([
    html.Img(id="logo", src='/assets/logo.png'),
    html.H1(id="title", children='LONDON PROPERTY MAP')
    ]),

    html.Div(id="summary", children='''
        A tool that lets you explore London's property market and visualise patterns in the associated data
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
    dcc.Graph(id='map-graph'),
    dcc.Graph(id='histogram')
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

@app.callback(Output("histogram", "figure"),
            [Input("feature-dropdown", "value")])
def update_histogram(value):
    datatype = dp.get_data_type(value)
    if datatype == "continuous":
        result = gp.get_continuous_histogram_config(df, value)
        return go.Figure(data=result['data'], layout=result['layout'])
    else:
        return go.Figure()

if __name__ == '__main__':
    app.run_server()
