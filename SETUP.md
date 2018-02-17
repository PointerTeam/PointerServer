# Setup

**Step 1**: Install the [GitHub desktop app](https://desktop.github.com)

**Step 2**: Press the green "Clone or download" button at the top of this page and then "Open in Desktop" to open the repository inside the app. Then you can clone (download) the repository to your computer.

**Step 3**: After you clone the repository, open up the Terminal (Mac) or Command Prompt (Windows) and go to where you copied the project

*On Mac*

```
cd ~/Documents/GitHub/PointerServer
```

*On Windows*

```
cd Documents\GitHub\PointerServer
```

`cd` is `change directory`

*If you want a very basic overview of the Terminal, you can check [this](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line)*

**Step 4**: Install `virtualenv`

*On Mac*

```
sudo pip install virtualenv
```

*On Windows*

```
pip install virtualenv
```

If you get an error about not having `pip`, you can install it following the instructions [here](https://pip.pypa.io/en/stable/installing/)

If you get an error about not having `python` while installing `pip`, you can install it following the instructions [here](https://www.python.org/downloads/).

If you still get an error about not having `python` or `pip`, you might have to add `C:\Python27` and `C:\Python27\Scripts` to your environment variables following the instructions [here](https://dev.to/el_joft/installing-pip-on-windows).


**Step 5**: Create the virtual environment

```
virtualenv venv
```

The [virtual environment](https://virtualenv.pypa.io/en/stable/) is used so that different Python projects can use different libaries without problems.

**Step 6**: Install [Flask](http://flask.pocoo.org/docs/0.12/installation/#installation)

*On Mac*

```
. venv/bin/activate
pip install -r requirements.txt
```

*On Windows*

```
venv\Scripts\activate
pip install -r requirements.txt
```

**Step 7**: Celebrate 🎉

Try running the project by following the [README](https://github.com/PointerTeam/PointerServer/blob/master/README.md)!
