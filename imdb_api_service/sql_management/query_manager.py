from imdb_api_service.sql_management.pg_conn_mgr import IMDBConnManager


class IMDBQueryManager(IMDBConnManager):

    def __init__(self):
        super().__init__()

    def get_query_data(self, sql_query_string):
        self.query_execution(sql_query_string)
        return self.all_data_from_query()
