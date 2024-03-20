from flask import Flask, redirect, render_template, jsonify,request, url_for
from modules.seggregator import seggregate_input, trim_title, trim_desc
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
    return render_template('newauto.html')
elements=[]
@app.route('/newproject', methods=['POST'])
def newproject():
    global elements
    data = request.json.get('selected_item')
    print(data)
    elements=seggregate_input(data)

    return redirect(url_for('project',title=elements[0], description=elements[1]))
    
@app.route("/project")
def project(title=None, description=None):
    current = request.url

    print(current)
    return render_template('saved-project1.html', title=elements[0], description=elements[1])

if __name__ == '__main__':
    app.run(debug=True)
