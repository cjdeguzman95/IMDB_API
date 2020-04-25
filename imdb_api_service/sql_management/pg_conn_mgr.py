from psycopg2 import connect


class IMDBConnManager:

    def __init__(self, dbname='imdb', user='postgres', password='postgres', host='localhost', port=5432):
        self.connection = connect(dbname=dbname, user=user, password=password, host=host, port=port)
        self.cursor = self.connection.cursor()

    def query_execution(self, sql_query_string):
        return self.cursor.execute(sql_query_string)

    def all_data_from_query(self):
        return self.cursor.fetchall()
