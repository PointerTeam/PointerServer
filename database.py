# Database to store and fetch the messages
import json
from point import Point

class Database:

  def __init__(self):
    # A "database" until we have an actual database
    self.fakeDatabase = [
      Point(43.472113, -80.543936, 'Hello world!'),
      Point(43.471772, -80.545337, 'thank mr goose')
    ]

  def create(self, lat, long, message):
    point = Point(lat, long, message)

    print("[Database] Created new: " + str(point))
    self.fakeDatabase.append(point)

  def query(self, lat, long, limit=10):
    # This just converts all the Points to a JSON form before sending it back
    return json.dumps(map(lambda p: p.toJSON(), self.fakeDatabase))
