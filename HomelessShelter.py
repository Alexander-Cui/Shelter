from flask import Flask, render_template
import json
app = Flask(__name__)


@app.route('/')
def home():

    # Opening JSON file with homesless shelters info
    f = open('shelters.json')

    #returns JSON object as a dictionary
    shelters_data = json.load(f)


    for i in shelters_data['shelters']:
        print(i['name'])

    # Closing file
    f.close()

    return render_template('index.html', shelters_data=shelters_data)
if __name__ == '__main__':
    app.run()
#app.run('0.0.0.0', 8000, debug = True)