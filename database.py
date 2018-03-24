# Database to store and fetch the messages
import json
from point import Point
import os
import sqlite3

class Database:
  
  def __init__(self):
    """Connects to the specific database."""    
    # A "database" until we have an actual database; connect to the SQL database
    print("Init")

  def create(self, db, lat, lon, message):
#    point = Point(lat, lon, message)
#    print("[Database] Created new: " + str(point))
    #self.fakeDatabase.append(point) # Inserts
    db.execute('insert into points (message, lon, lat) values (?, ?, ?)',
                 [message,lon,lat])
    db.commit()


  def query(self, db, lat, lon, limit=10):
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    # This just converts all the Points to a JSON form before sending it back
    #sqlinput= 'SELECT lat, lon, message FROM points WHERE lat BETWEEN {}-1 AND {} AND lon BETWEEN {}-1 and {} ORDER BY id DESC'.format(lat,lat,lon,lon)
    lonbound = 1
    latbound = 1
    cur = db.execute('SELECT lat, lon, message FROM points WHERE lat BETWEEN (?) AND (?) AND lon BETWEEN (?) and (?)',[lat - latbound, lat + latbound, lon - lonbound, lon + lonbound])
    points = cur.fetchall()
    entries_list = []
    x = 0
    def loop_1(point):
        entries_list = []
        x = 0
        while x < len(point):
            entries_list.append(Point(point[x][0],point[x][1],point[x][2]).toJSON())
            x = x + 1
        return entries_list
    return loop_1(points)
    #return str(points[0][0]) + ", " + str(points[0][1]) + ", " + points[0][2]
    print("Show entries")

    # return json.dumps(map(lambda p: p.toJSON(), self.fakeDatabase)) #Selects
  
  def close_db(self):
    """Closes the database again at the end of the request."""
    #if hasattr(g, 'sqlite_db'):
    #    g.sqlite_db.close()
    print("Close db")

  #def show_entries(self, db):
  #  cur = db.execute('select title, text from entries order by id desc')
  #  entries = cur.fetchall()
  #  return entries
  #  print("Show entries")

  # def add_entry(self, db):
  #   if not session.get('logged_in'):
  #       abort(401)
  #   db.execute('insert into entries (title, text) values (?, ?)',
  #                [request.form['title'], request.form['text']])
  #   db.commit()
