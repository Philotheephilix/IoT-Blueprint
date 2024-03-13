from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/aboutus")
def aboutus():
    return render_template('about-us-page.html')

@app.route("/saved")
def saved():
    return render_template('saved-project.html')

@app.route("/new")
def new():
    return render_template('new-project-1-select-4.html')

if __name__ == '__main__':
    app.run(debug=True)
