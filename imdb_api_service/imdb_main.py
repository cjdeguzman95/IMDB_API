from flask import Flask, render_template
from imdb_api_service.imdb_factory.imdb_factory_manager import IMDBFactory as IMDBFactory

imdb_api = Flask(__name__)


@imdb_api.route('/')
def home_page():
    return render_template("homepage.html")


@imdb_api.route('/all-movie-data')
def all_movie_data():
    return IMDBFactory().get_all_movie_data_json()


@imdb_api.route('/all-films-over-half-a-billion')
def films_over_half_billion():
    return IMDBFactory().get_all_films_over_half_a_billion_json()


@imdb_api.route('/all-films-with-imdb-score-over-nine')
def films_with_high_imdb_score():
    return IMDBFactory().get_all_films_with_imdb_score_over_nine()


@imdb_api.route('/top-10-uk-films')
def top_ten_uk_films():
    return IMDBFactory().get_top_ten_uk_films()


@imdb_api.route('/foreign-language-films-2000')
def foreign_language_films():
    return IMDBFactory().get_all_foreign_language_films()


if __name__ == '__main__':
    imdb_api.run()
