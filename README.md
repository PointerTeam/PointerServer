# Pointer Server

Backend for an app that lets you put messages on a map and get messages near you

![](https://github.com/PointerTeam/PointerApp/raw/master/Screenshot.png)

Video demo: [https://www.youtube.com/watch?v=lAqzTX5RzQg](https://www.youtube.com/watch?v=lAqzTX5RzQg)


## Team members

- 🐰 Luana @l398chen
- 🐵 JP @junpark97


## Running

For setup instructions, go to [SETUP](https://github.com/PointerTeam/PointerServer/blob/master/SETUP.md)

In a new Terminal/Command Prompt,

**Step 1**: Get to the project folder

*On Mac*

```
cd ~/Documents/GitHub/PointerServer
```

*On Windows*

```
cd Documents\GitHub\PointerServer
```

**Step 2**: Start the server

*On Mac*

```
. venv/bin/activate
export FLASK_APP="server.py"
export FLASK_DEBUG=1
flask run
```

*On Windows*

```
venv\Scripts\activate
set FLASK_APP=server.py
set FLASK_DEBUG=1
flask run
```

**Step 3**: Check that the server is running

In another terminal, enter

```
curl localhost:5000/ping
```

You should see a `Pong!`


## Testing the APIs

*On Mac/Linux*

To get messages from the server, send a GET request to `/messages` with the `lat` and `lon` as query parameters:

```
curl localhost:5000/messages?lat=123&lon=456
```

To create a new message, send a POST request to `/messages` with a JSON body with `lat`, `lon`, and `message` specified:

```
curl localhost:5000/messages -X POST -H "Content-Type: application/json" -d '{"lat": 123, "lon": 456, "message": "My message"}'
```

*On Windows or Mac/Linux/Anything with Chrome*

You can also use [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) instead to get a pretty UI :)


## Project files

```
PointerServer/   (project folder)
|
├── server.py    (Flask server)
├── database.py  (Database where we get the messages)
└── point.py     (Representation of a message)
```

## Setting up SQLite and creating the the database

Install SQLite3: [SQLite3](https://www.sqlite.org/download.html)

To create the databse or to refresh it:

**Step 1**: open your command prompt and go to the PointerServer directory

```
cd Documents\GitHub\PointerServer
```

**Step 2**: call SQLite3 and create the database by inputting the following code:

*On Windows*
```
sqlite3 database.db < schema.sql
```
