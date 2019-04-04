from flask import Flask, render_template
import datetime

# Name of the this file can be different than "app.py", provided
# we use the below environment variable:
# export FLASK_APP=<different_filename.py>

# Create flask app
app = Flask(__name__)

# The home page of your website will be governed
# by the API - index().
# Whatever this function returns, it will be displayed 
# on screen.
@app.route("/")
def home_page():
    # This will search for sample.html in <current_dir>/templates/sample.html
    headline = "this is the headline"
    return render_template("sample.html", headline=headline)

# Defining ronan's page    
@app.route("/ronan")
def ronan():
    return "Welcome to page ronan"    
    
# Defining david's page    
@app.route("/david")
def david():
    return "This is David's page"     

'''    
# Defining a generic page to welcome any user
# http://127.0.0.1:5000/<any_user_name> 
# The name is passed as a parameter to the function.
@app.route("/<string:name>")
def genericWelcome(name):
    return f"Hello <b>{name}!</b>. This is a welcome page for you"     
'''

@app.route("/newyear")
def isItNewYear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    if new_year:
        return "<h1>Woohoooo! It's New Year!</h1>"
    else:
        return f"<h1>Not a New Year!</h1> <br><h2>Date: {now}</h2>"
    