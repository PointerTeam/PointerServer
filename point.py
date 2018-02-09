# A representation of a point on the map

class Point:

  def __init__(self, lat, long, message):
    self.lat = lat
    self.long = long
    self.message = message

  def __str__(self):
    return "Point(" + str(self.lat) + ", " + str(self.long) + "; " + self.message + ")"

  def toJSON(self):
    return {
      'location': {
        'lat': self.lat,
        'long': self.long
      },
      'message': self.message
    }
