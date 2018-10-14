class SqlGenerator(object):
    QUERIES = {
        "ALL": """SELECT * FROM properties""",
        "SUBSET": """SELECT * FROM properties WHERE retrieved_at = '2018-10-13' and search_name like 'N%'"""
        }

    def getSQL(self, category):
        return QUERIES[category] or "Not a valid query category"
