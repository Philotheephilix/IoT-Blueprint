from flask import Flask, redirect, render_template, jsonify, request, url_for

from modules.components import items
from modules.seggregator import seggregate_input

app = Flask(__name__)

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# About us page route
@app.route("/aboutus")
def aboutus():
    return render_template('about-us-page.html')

# Saved Project page route
@app.route("/saved")
def saved():
    return render_template('saved-project.html')

# New project page routes
@app.route("/new")
def new():
    return render_template('newauto.html', items=items)

@app.route('/newproject', methods=['POST'])
def newproject():
    global elements
    data = request.json.get('selected_items')
    print(data)
    elements = seggregate_input(data)
    print(elements)
    return redirect(url_for('project', title=elements[0], description=elements[1]))

@app.route("/project")
def project():
    current = request.url
    print(current)
    return render_template('saved-project1.html', title=elements[0], description=elements[1])

if __name__ == '__main__':
    app.run(debug=True)
