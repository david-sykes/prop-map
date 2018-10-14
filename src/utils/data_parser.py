class DataParser(object):
    def parseDates(dataframe):
        df['first_visible_date'] = pd.to_datetime(df['first_visible_date'])
        df["age"] = (datetime.datetime.now()  - df['first_visible_date']).dt.days
