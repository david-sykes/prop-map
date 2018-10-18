class SqlGenerator(object):
    QUERIES = {
        "ALL": """SELECT * FROM properties""",
        "SUBSET": """SELECT * FROM properties WHERE retrieved_at = '2018-10-13' and search_name like 'N%'""",
        "LARGE": """SELECT * FROM properties WHERE retrieved_at >= '2018-10-14' and retrieved_at < '2018-10-16'"""
        }

    DEFAULT = "Not a valid query category"

    def get_sql(self, category):
        return self.QUERIES.get(category.upper(), self.DEFAULT)
