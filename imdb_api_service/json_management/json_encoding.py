from flask import jsonify


class IMDBJsonEncoder:

    def __init__(self):
        self.field_names = ['movie_id', 'movie_title', 'duration', 'color', 'director_name', 'actor_1_name',
                            'actor_2_name', 'actor_3_name', 'gross', 'genres', 'plot_keywords', 'language', 'country',
                            'content_rating', 'budget', 'title_year', 'imdb_score']

    def create_imdb_dict_array(self, list_of_tuple_results):
        list_of_results = []
        if len(list_of_tuple_results) >= 1:
            for tuple in list_of_tuple_results:
                list_of_results.append(dict(zip(self.field_names, tuple)))
            return jsonify(list_of_results)
        else:
            return "No movie data available"
