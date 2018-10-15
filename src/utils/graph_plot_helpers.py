from . import data_parser_helpers as dp
import plotly.graph_objs as go

def get_continuous_scatter_config(data, category, access_token):
    marker=dict(
        size=4,
        opacity=0.5,
        color=dp.map_percentiles(data[category].values),
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
            "outlinecolor": 'rgba(68,68,68,0)',
            "ticks": 'inside',
            "ticklen": 3,
            "ticksuffix": 'k',
            "tickprefix": '£',
            "dtick": 0.1}
    )

    layout = go.Layout(
        autosize=True,
        hovermode='closest',
        height=700,
        showlegend=False,
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
    marker=dict(
        size=4,
        color=data[category].values,
    )

    layout = go.Layout(
    autosize=True,
    hovermode='closest',
    height=700,
    showlegend=True,
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
