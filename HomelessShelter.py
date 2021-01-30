from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Homeless Shelters'

@app.route('/Shelter')
def shelter():
    return render_template("shelterAdmin.html")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        print(request.form)
    return render_template("login.html")

app.run('0.0.0.0', 8000, debug = True)