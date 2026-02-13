from flask import Flask, render_template, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

#Lookup-only pages

@app.route("/")
def greet():
    return_template("index.html")

@app.route("/competitions")
def view_comp():
    return_template("comp.html")

@app.route("/teams")
def view_team():
    return_template("team.html")

#Complex pages

@app.route("/search",methods = ['GET,POST'])
def search():
    return 0 #placeholder

@app.route("/signup",methods = ['GET,POST'])
def search():
    return 0 #placeholder

@app.route("/login",methods = ['GET,POST'])
def search():
    return 0 #placeholder

if __name__ == '__main__':
    app.run(debug=True)