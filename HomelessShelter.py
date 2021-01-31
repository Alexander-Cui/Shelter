from flask import Flask, render_template
from flask import request
import json
app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        print(request.json)
    # Opening JSON file with homesless shelters info
    f = open('shelters.json')

    #returns JSON object as a dictionary
    shelters_data = json.load(f)


    for i in shelters_data['shelters']:
        print(i['name'])

    # Closing file
    f.close()

    return render_template('index.html', shelters_data=shelters_data)

@app.route('/Shelter')
def shelter():
    return render_template("shelterAdmin.html")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        print(request.form)
    return render_template("login.html")

if __name__ == '__main__':
    app.run()
#app.run('0.0.0.0', 8000, debug = True)