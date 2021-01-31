from flask import Flask, render_template, redirect, url_for, request
import json
app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def home():




    # Opening JSON file with homesless shelters info
    f = open('shelters.json')

    #returns JSON object as a dictionary
    shelters_data = json.load(f)


    for i in shelters_data['shelters']:
        print(i['name'])

    # Closing file
    f.close()
    matching = []
    ordered_matching = []
    matching_shelters = {}
    matching_shelters['shelters'] = matching
    if request.method == 'POST':
        print("$$$$$")
        if 'age' or 'gender' in request.form:
            print("*******")
            gender = request.form['gender']
            age = request.form['age']
            ordered_locations = request.json
            print(gender)
            print(age)

            for shelter in shelters_data['shelters']:
                if (shelter['gender'] == gender) and (shelter['age'] == age):
                    matching.append(shelter)
            print(matching)
            # for s in ordered_shelters:
            #     for sun in matching:
            #         if sun['name'] == s['name']:
            #             ordered_matching.append(sun)
            # matching_shelters['shelters'] = ordered_matching
            shelters_data = matching_shelters

    #return render_template('index.html', shelters_data=matching_shelters)
    return render_template('index.html', shelters_data=shelters_data)
if __name__ == '__main__':
    app.run()
#app.run('0.0.0.0', 8000, debug = True)