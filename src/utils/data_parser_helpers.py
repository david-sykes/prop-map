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

def transform_branch_names(dataframe, max_branches):
    if 'branch_name' in dataframe:
        branch_counts = dataframe.branch_name.value_counts()
        top_branches = branch_counts.iloc[0:max_branches]
        dataframe['branch_name'] = dataframe['branch_name'].apply((lambda branch: fill_branch_name(top_branches, branch)))
        return dataframe

def fill_branch_name(top_branches, name):
    if name in top_branches:
        return name
    else:
        return 'Other'
