from imdb_api_service.sql_management.query_manager import IMDBQueryManager
from imdb_api_service.json_management.json_encoding import IMDBJsonEncoder


class IMDBFactory:

    def __init__(self):
        self.json_encoder = IMDBJsonEncoder()
        self.query_manager = IMDBQueryManager()

    def get_all_movie_data_json(self):
        return self.json_encoder.create_imdb_dict_array(self.query_manager.get_query_data('SELECT * FROM moviedata;'))

    def get_all_films_over_half_a_billion_json(self):
        return self.json_encoder.create_imdb_dict_array(self.query_manager.get_query_data('SELECT * FROM moviedata WHERE gross > 500000000;'))

    def get_all_films_with_imdb_score_over_nine(self):
        return self.json_encoder.create_imdb_dict_array(self.query_manager.get_query_data('SELECT * FROM moviedata WHERE imdb_score > 9.0 ORDER BY imdb_score DESC;'))

    def get_all_foreign_language_films(self):
        return self.json_encoder.create_imdb_dict_array(self.query_manager.get_query_data("SELECT * FROM moviedata WHERE language != 'English' and title_year >= 2000 ORDER BY title_year DESC"))

    def get_top_ten_uk_films(self):
        return self.json_encoder.create_imdb_dict_array(self.query_manager.get_query_data("SELECT * FROM moviedata WHERE country = 'UK' and gross IS NOT NULL ORDER BY gross DESC LIMIT 10;"))
