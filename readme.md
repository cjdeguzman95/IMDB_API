# IMDB Web API

As written in the setup file, this project is a basic API written in flask which returns results from a dockerised IMDB database. A basic HTML template was also created for the home page to communicate the different routes within the API.

## SQL Management
Psycopg2 is used to connect the IMDBConnManager to the PostgreSQL IMDB databased. This class also defines the variables required to establish the connection between the programme and the database.
Through abstraction and inheritance, the query manager brings together the two methods from the IMDBConnManager into one method which executes the SQL query then fetches and returns all the results.

## JSON Management
Jsonify from flask is used to convert the tuple of results from the query manager into JSON format. First, it takes the results and creates a list of key-value pairs which is then converted into JSON.

## IMDB Factory
This brings together the methods from the JSON encoder and the query manager so that specific results from the given SQL query are retrieved. These are then displayed in the web API via designated routes.

## IMDB_main.py
This file uses flask to create a simple web API which displays all the results from the IMDB factory.
