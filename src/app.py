# -*- coding: utf-8 -*-

import dash, datetime, math, os, sys, argparse
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
from flask import Flask
from utils import db_utils
from utils import sql_generator
from utils import data_parser_helpers as dp
import numpy as np
import pandas as pd

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

mapbox_access_token = os.environ.get('MAPBOX_ACCESS_TOKEN')

data = [
    go.Scattermapbox(
        lat=df['lat'],
        lon=df['lon'],
        mode='markers',
        marker=dict(
            size=9,
            color=dp.map_percentiles(df["age"].values),
            colorscale=[[0, 'rgb(244,236,21)'], [0.021, 'rgb(218,240,23)'],
                                [0.042, 'rgb(187,236,25)'], [0.063, 'rgb(157,232,27)'],
                                [0.084, 'rgb(128,228,29)'], [0.115, 'rgb(102,224,31)'],
                                [0.146, 'rgb(76,220,32)'], [0.170, 'rgb(52,216,34)'],
                                [0.225, 'rgb(36,210,73)'], [0.275, 'rgb(37,208,66)'],
                                [0.325, 'rgb(38,204,88)'], [0.375, 'rgb(40,200,109)'],
                                [0.4, 'rgb(41,196,129)'], [0.5, 'rgb(42,192,147)'],
                                [0.6, 'rgb(43,188,164)'],[1.0, 'rgb(97,48,153)']]
        ),
    )
]

layout = go.Layout(
    autosize=True,
    hovermode='closest',
    height=700,
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=df.iloc[0].lat,
            lon=df.iloc[0].lon
        ),
        pitch=0,
        zoom=10,
        style="dark"
    ),
)

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
                value="Price",
                placeholder="Price",
                className="feature-picker"
            ),
    dcc.Graph(
        id='prop_details',
        figure={
            'data': data,
            'layout': layout
        }
    )
])

if __name__ == '__main__':
    app.run_server()
