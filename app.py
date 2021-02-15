from flask import Flask, escape, request, render_template, url_for, redirect
import json
import os
from key import API_KEY
import requests
from pprint import PrettyPrinter
pp = PrettyPrinter()
apiKey = API_KEY






app = Flask(__name__)





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorites')
def favorites():
    #Read out favorited movies.
    filename = os.path.join('data.json')
    with open(filename) as data_file:
        data = json.load(data_file)
  
    return redirect(url_for('savefavorites', data=data))

@app.route('/savefavorites/<data>')
def savefavorites(data):
    """if query params are passed, write movie to json file."""
    return render_template('favorites.html', data=data)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['title']
    data_URL ='http://www.omdbapi.com/?apikey='+API_KEY
    year = ''
    movieTitle = query
    params = {
    's':movieTitle,
    'type':'movie',
    'y':year    
    }
    response = requests.get(data_URL,params=params).json()
    pp.pprint(response)
    return (f'Your Movie Result: {response}')

@app.route('/movie/<movie_oid>')
def movie_detail():
    """if fetch data from movie database by oid and display info."""
    qs_name = request.args.get('name', '')
    qs_oid = request.args.get('oid', '')
    return f'Hello, {escape(name)}'
