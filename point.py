# A representation of a point on the map

class Point:

  def __init__(self, lat, lon, message):
    self.lat = lat
    self.lon = lon
    self.message = message

  def __str__(self):
    return "Point(" + str(self.lat) + ", " + str(self.lon) + "; " + self.message + ")"

  def toJSON(self):
    return {
      'location': {
        'lat': self.lat,
        'lon': self.lon
      },
      'message': self.message
    }
