from . import data_parser_helpers as dp
import plotly.graph_objs as go

def get_continuous_scatter_config(data, category, access_token):
    marker=dict(
        size=4,
        opacity=0.5,
        color=data[category].values,
        colorscale=[[0, 'rgb(244,236,21)'], [0.021, 'rgb(218,240,23)'],
                            [0.042, 'rgb(187,236,25)'], [0.063, 'rgb(157,232,27)'],
                            [0.084, 'rgb(128,228,29)'], [0.115, 'rgb(102,224,31)'],
                            [0.146, 'rgb(76,220,32)'], [0.170, 'rgb(52,216,34)'],
                            [0.225, 'rgb(36,210,73)'], [0.275, 'rgb(37,208,66)'],
                            [0.325, 'rgb(38,204,88)'], [0.375, 'rgb(40,200,109)'],
                            [0.4, 'rgb(41,196,129)'], [0.5, 'rgb(42,192,147)'],
                            [0.6, 'rgb(43,188,164)'],[1.0, 'rgb(97,48,153)']],
        colorbar={
            "thickness": 10,
            "titleside": 'right',
            "outlinecolor": '#444444',
            "ticks": 'inside',
            "x": 0.95,
            "xpad": 0,
            "ticklen": 3,
            "tickmode": "array",
            "tickvals": [0, 1],
            "ticktext": [data[category].min(), data[category].max()],
            "ticksuffix": 'k',
            "tickprefix": '£'}
    )

    layout = go.Layout(
        autosize=True,
        hovermode='closest',
        height=500,
        showlegend=False,
        margin = dict(l = 0, r = 0, t = 0, b = 0),
        mapbox=dict(
            accesstoken=access_token,
            bearing=0,
            center=dict(
                lat=data.iloc[0].lat,
                lon=data.iloc[0].lon
            ),
            pitch=0,
            zoom=10,
            style="dark"
        ),
    )
    return {"marker": marker, "layout": layout}


def get_discrete_scatter_config(data, category, access_token):
    layout = go.Layout(
    autosize=True,
    hovermode='closest',
    height=500,
    showlegend=True,
    margin=dict(l = 0, r = 0, t = 0, b = 0),
    mapbox=dict(
        accesstoken=access_token,
        bearing=0,
        center=dict(
            lat=data.iloc[0].lat,
            lon=data.iloc[0].lon
        ),
        pitch=0,
        zoom=10,
        style="dark"
    ),
    )

    marker = {}

    return {"marker": marker, "layout": layout}

def get_continuous_histogram_config(data, category):
    (min, max, interval) = dp.get_histogram_xaxis_config(data[category].values)
    return {
        'data': [
            {
                'x': data[category],
                'name': category.capitalize(),
                'type': 'histogram',
                'autobinx': False,
                'xbins': {
                    'start': min,
                    'end': max,
                    'size': interval
                }
            }
        ],
        'layout': {
            'margin': {'l': 70, 'r': 40, 't': 40, 'b': 60},
            'autosize': True,
            'plot_bgcolor': '#333333',
            'paper_bgcolor': '#333333',
            'font': {
                'color': '#FFF'
            },
            
            'xaxis': {
                'autorange': True,
                'title': category.capitalize(),
                'showticklabels': True,
                'type': 'linear',
                'visible': True,
                'tickmode': 'auto',
                'ticklen': 10,
                'tickcolor': '#B2B2B2',
                'tickfont': {
                    'family': 'Raleway, sans-serif',
                    'color': '#B2B2B2'
                },
                'titlefont': {
                    'family': 'Raleway, sans-serif',
                    'color': '#B2B2B2'
                }
                },
            'yaxis': {
                'title': 'Count',
                'autorange': True,
                'showticklabels': True,
                'type': 'linear',
                'visible': True,
                'tickmode': 'auto',
                'ticklen': 5,
                'tickcolor': '#B2B2B2',
                'tickfont': {
                    'family': 'Raleway, sans-serif',
                    'color': '#B2B2B2'
                },
                'titlefont': {
                    'family': 'Raleway, sans-serif',
                    'color': '#B2B2B2'
                }
                },
        }
    }


def get_discrete_datasets(data, category):
    values = set(data[category].values)
    dataset = []
    for value in values:
        filtered_data = data[data[category] == value]
        dataset.append(
        go.Scattermapbox(
            lat=filtered_data['lat'],
            lon=filtered_data['lon'],
            mode="markers",
            marker=dict(
            size=4,
            opacity=0.5
            ),
            name=value
        ))
    return dataset
