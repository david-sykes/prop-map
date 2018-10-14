import pandas as pd
import os
import psycopg2


class PropertiesDB(object):
    def __init__(self):
        self.DB_NAME = os.environ.get('DB_NAME')
        self.DB_USER = os.environ.get('DB_USER')
        self.DB_HOST = os.environ.get('DB_HOST')
        self.DB_PASSWORD = os.environ.get('DB_PASSWORD')
        self.conn = psycopg2.connect(dbname=self.DB_NAME,
                                host=self.DB_HOST,
                                user=self.DB_USER,
                                password=self.DB_PASSWORD)


class DataLoader(object):
    def __init__(self):
        self.db = PropertiesDB()


    def load_data(self, sql):
        return pd.read_sql(sql, self.db.conn)
