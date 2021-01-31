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

        if 'age' or 'gender' in request.form:
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

@app.route('/Shelter', methods=["POST"])
def shelter():
    if request.method == 'POST':
        print(request.form['username'])
        homeless_shelter_name = request.form['username']

    return render_template("shelterAdmin.html",homeless_shelter_name=homeless_shelter_name )

@app.route('/login', methods=["GET","POST"])


def login():
    return render_template("login.html")



@app.route('/updated', methods=["POST"])
def update():

    if request.method == 'POST' and 'spots' in request.form and 'username' in request.form:

        updated_capacity= request.form['spots']
        username = request.form['username']
        a_file =open('shelters.json','r')
        json_object = json.load(a_file)
        a_file.close()
        for shelter in json_object["shelters"]:
            if shelter['name'] == username:
                shelter['capacity'] = updated_capacity

        a_file = open("shelters.json", "w")
        json.dump(json_object, a_file)
        a_file.close()




    return render_template("updated.html")

if __name__ == '__main__':
    app.run()
#app.run('0.0.0.0', 8000, debug = True)