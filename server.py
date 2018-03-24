#imports
import os
import sqlite3

from flask import Flask, request, g
import json
from point import Point
from database import Database
import json

app = Flask(__name__)
app.config.from_object(__name__) # load config from this file  ****

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'database.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def get_sqlite():
  rv = sqlite3.connect(app.config['DATABASE'])
  rv.row_factory = sqlite3.Row
  return rv

db = Database()

# Get messages near the (lat, lon)
# Ex. curl localhost:5000/messages?lat=123,lon=456
@app.route('/messages', methods=['GET'])
def getPoints():
  # We should sanity check here and return error if invalid
  lat = float(request.args.get('lat', 0))
  lon = float(request.args.get('lon', 0))

  print('[Server] Getting messages for (' + str(lat) + ', ' + str(lon) + ')')
  return json.dumps(db.query(get_sqlite(), lat, lon))

# Create a new message at the location
@app.route('/messages', methods=['POST'])
def createPoint():
  # We should sanity check the JSON here before adding to the database
  print(request.json)
  db.create(get_sqlite(), request.json['lat'], request.json['lon'], request.json['message'])
  return 'Successfully created message'

# Test to see if the server is up
@app.route('/ping', methods=['GET'])
def ping():
  return 'Pong! :)'

@app.teardown_appcontext
def close_db(error):
  db.close_db()
  
@app.cli.command('initdb')
def initdb_command():
  with app.open_resource('schema.sql', mode='r') as f:
    db = get_sqlite()
    db.cursor().executescript(f.read())
    db.commit()
    print('Initialized the database.')
  
# @app.route('/')
# def show_entries():
#   return str(db.show_entries(get_sqlite()))

# @app.route('/add', methods=['POST'])
# def add_entry():
#   db.add_entry()
