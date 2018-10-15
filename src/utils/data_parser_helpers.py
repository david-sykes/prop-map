import pandas as pd
import datetime, functools

def parse_dates(df):
    df['first_visible_date'] = pd.to_datetime(df['first_visible_date'])
    df["age"] = (datetime.datetime.now()  - df['first_visible_date']).dt.days
    return df

def calculate_percentile(max, min, value):
    percentile = (value - min)/(max - min)
    return percentile

def map_percentiles(data_array):
    max = data_array.max()
    min = data_array.min()
    return list(map(functools.partial(calculate_percentile, max, min), data_array))

def get_data_type(category):
    DATA_TYPES = {"age":"continuous",
                  "price": "continuous",
                  "bedrooms": "continuous",
                  "branch_name": "discrete",
                  "property_subtype": "discrete"}
    return DATA_TYPES.get(category, None)
