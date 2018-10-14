# -*- coding: utf-8 -*-

import dash, datetime, math, os
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
from flask import Flask
from utils import db_utils as db
from utils import sql_generator as sql_gen
import numpy as np
import pandas as pd

app = dash.Dash(__name__)

dl = db.DataLoader()
sg = sql_gen.SqlGenerator()
df = dl.load_data(sg.getSQL('subset'))
df['first_visible_date'] = pd.to_datetime(df['first_visible_date'])
df["age"] = (datetime.datetime.now()  - df['first_visible_date']).dt.days
maxAge = df["age"].max()
minAge = df["age"].min()

def getAgeColorIndex(age):
    percentile = (age - minAge)/(maxAge - minAge)
    index = percentile/(1/24)
    return index

def mapAgeToColorIndex(array):
    return list(map(getAgeColorIndex, array))

mapbox_access_token = os.environ.get('MAPBOX_ACCESS_TOKEN')

data = [
    go.Scattermapbox(
        lat=df['lat'],
        lon=df['lon'],
        mode='markers',
        marker=dict(
            size=9,
            color=mapAgeToColorIndex(df["age"].values),
            colorscale=[[0, 'rgb(244,236,21)'], [0.04167, 'rgb(218,240,23)'],
                                [0.0833, 'rgb(187,236,25)'], [0.125, 'rgb(157,232,27)'],
                                [0.1667, 'rgb(128,228,29)'], [0.2083, 'rgb(102,224,31)'],
                                [0.25, 'rgb(76,220,32)'], [0.292, 'rgb(52,216,34)'],
                                [0.333, 'rgb(36,210,73)'], [0.375, 'rgb(37,208,66)'],
                                [0.4167, 'rgb(38,204,88)'], [0.4583, 'rgb(40,200,109)'],
                                [0.50, 'rgb(41,196,129)'], [0.54167, 'rgb(42,192,147)'],
                                [0.5833, 'rgb(43,188,164)'],[1.0, 'rgb(97,48,153)']]
        ),
    )
]

layout = go.Layout(
    autosize=True,
    hovermode='closest',
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
        Age of property
    '''),

    dcc.Graph(
        id='age_of_prop',
        figure={
            'data': data,
            'layout': layout
        }
    )
])

if __name__ == '__main__':
    app.run_server()
