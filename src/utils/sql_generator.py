class SqlGenerator(object):
    QUERIES = {
        "ALL": """SELECT * FROM properties""",
        "SUBSET": """SELECT * FROM properties WHERE retrieved_at = '2018-10-13' and search_name like 'N%'"""
        }

    def get_sql(self, category):
        return self.QUERIES[category.upper()] or "Not a valid query category"
