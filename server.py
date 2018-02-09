from flask import Flask, request
import json
from point import Point
from database import Database

app = Flask(__name__)

db = Database()

# Get messages near the (lat, long)
# Ex. curl localhost:5000/messages?lat=123,long=456
@app.route('/messages', methods=['GET'])
def getPoints():
  # We should sanity check here and return error if invalid
  lat = request.args.get('lat', 0)
  long = request.args.get('long', 0)

  print('[Server] Getting messages for (' + str(lat) + ', ' + str(long) + ')')
  return db.query(lat, long)

# Create a new message at the location
@app.route('/messages', methods=['POST'])
def createPoint():
  # We should sanity check the JSON here before adding to the database
  print(request.json)
  db.create(request.json['lat'], request.json['long'], request.json['message'])
  return 'Successfully created message'

# Test to see if the server is up
@app.route('/ping', methods=['GET'])
def ping():
  return 'Pong! :)'
