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

        if request.form.get("age") and request.form.get("gender"):
            gender = request.form['gender']
            age = request.form['age']
            ordered_locations = request.json
            print(gender)
            print(age)

            for shelter in shelters_data['shelters']:
                if (shelter['gender'] == gender) and (shelter['age'] == age):
                    matching.append(shelter)
            print(matching)
            shelters_data = matching_shelters
            return render_template('index.html', shelters_data=shelters_data)
        if request.json:
            print("hello")
            ordered_shelters = request.json
            ordered_matching=[]
            for s in ordered_shelters:
                for sun in shelters_data["shelters"]:
                    if sun['name'] == s['name']:
                        sun["distance"] = s["duration"]
                        ordered_matching.append(sun)
            
            shelters_data = ordered_matching
            print(shelters_data)

    #return render_template('index.html', shelters_data=matching_shelters)
    return render_template('index.html', shelters_data=shelters_data ,message="hey")

@app.route('/Shelter', methods=["POST"])
def shelter():
    if request.method == 'POST':
        print(request.form['username'])
        homeless_shelter_name = request.form['username']

    return render_template("shelterAdmin.html",homeless_shelter_name=homeless_shelter_name )

@app.route('/login', methods=["GET","POST"])


def login():
    return render_template("login.html")


@app.route('/distance', methods=["GET"])
def distance():
    print("here")
    f = open('shelters.json')

    #returns JSON object as a dictionary
    shelters_data = json.load(f)


    for i in shelters_data['shelters']:
        print(i['name'])

    # Closing file
    f.close()


    hard_coded_data = {"shelters":
    [{'id': '2', 'name': 'ACCUEIL BONNEAU - HALTE RÃ‰PIT DU GRAND QUAI DU VIEUX PORT', 'address': '200 de la Commune Street West, Ville-Marie, MontrÃ©al, QC, H2Y 4B2', 'phone': '438-220-2129', 'demographic': 'people experiencing homelessness', 'lat': '45.50278210975688', 'lng': '-73.55078210122505', 'age': '18+', 'gender': 'either', 'capacity': '20', 'gMaps': 'https://www.google.com/maps/place/200+de+la+Commune+St+W,+Montreal,+QC+H2Y+4B2/@45.5026164,-73.5595368,15z/data=!3m1!4b1!4m5!3m4!1s0x4cc91a586b624b7f:0x2dba63a25fb9be72!8m2!3d45.5026167!4d-73.5507821', 'distance': '1 hour 44 mins'}, 
    {'id': '7', 'name': "ASSOCIATION D'ENTRAIDE LE CHAÃŽNON", 'address': "4373 de l'Esplanade Avenue, Le Plateau-Mont-Royal, MontrÃ©al, QC, H2W 1T2", 'phone': '514-845-0151', 'demographic': 'women in difficult situations, 18 years old and over', 'lat': '45.51786071817851', 'lng': '-73.58611811656979', 'age': '18+', 'gender': 'female', 'capacity': '20', 'gMaps': 'https://www.google.com/maps/place/4373+Esplanade+Ave,+Montreal,+QC+H2W+1T2/@45.4784231,-74.1110307,10z/data=!4m5!3m4!1s0x4cc91a2d3025ff8f:0x481a17b3d0ca1ac6!8m2!3d45.5176728!4d-73.5860752', 'distance': '1 hour 6 mins'}, 
    {'id': '6', 'name': "AMOUR EN ACTION (L')", 'address': '10201 des Laurentides Avenue, MontrÃ©al-Nord, MontrÃ©al, QC, H1H 4V4', 'phone': '514-327-0200', 'demographic': 'people on a low income, warming centre: men, women and children', 'lat': '45.58222905820677', 'lng': '-73.6384263435507', 'age': '18+', 'gender': 'either', 'capacity': '20', 'gMaps': 'https://www.google.com/maps/search/536+Chicoine+Street0201+des+Laurentides+Avenue,+Montr%C3%A9al-Nord,+Montr%C3%A9al,+QC,+H1H+4V4,+Vaudreuil-Dorion,+Mont%C3%A9r%C3%A9gie,+QC,+J7V+7E4/@45.4784231,-74.1110307,10z/data=!3m1!4b1', 'distance': '2 hours 26 mins'}, 
    {'id': '1', 'name': 'ABRI DE LA RIVE-SUD', 'address': '459 Sainte-Foy Boulevard, Longueuil, MontÃ©rÃ©gie, QC, J4J 1X9', 'phone': '450-646-7809', 'demographic': 'homeless men and women 18 years old and over', 'lat': '45.527113', 'lng': '-73.491401', 'age': '18+', 'gender': 'either', 'capacity': '20', 'gMaps': 'https://www.google.com/maps/place/Abri+de+la+Rive-Sud/@45.5268947,-73.4936006,17z/data=!3m1!4b1!4m5!3m4!1s0x4cc91b3be4da3581:0x70817d9cd99e18c1!8m2!3d45.5268947!4d-73.4914119', 'distance': '4 hours 5 mins'}, 
    {'id': '4', 'name': "ACTION JEUNESSE DE L'OUEST-DE-L'ÃŽLE - WARMING CENTRE", 'address': '5100 du ChÃ¢teau-Pierrefonds Avenue, Pierrefonds-Roxboro, MontrÃ©al, QC, H9K 1P3', 'phone': ' ', 'demographic': 'homeless people, pets accepted', 'lat': '45.46504971765899', 'lng': '-73.89738864355341', 'age': '18+', 'gender': 'either', 'capacity': '20', 'gMaps': 'https://www.google.com/maps/place/5100+Ave+du+Ch%C3%A2teau-Pierrefonds,+Pierrefonds,+QC+H9K+1P3/@45.4648237,-73.9061648,15z/data=!3m1!4b1!4m5!3m4!1s0x4cc93a3504bc9041:0xd49e7dd4040c4a1a!8m2!3d45.464824!4d-73.8974101', 'distance': '5 hours 15 mins'}, 
    {'id': '3', 'name': 'ACCUEIL COMMUNAUTAIRE JEUNESSE DES BASSES-LAURENTIDES - LE RÃ‰PIT DE LA RUE', 'address': '303 and 305 FÃ©rÃ© Street, Saint-Eustache, Laurentides, QC, J7R 2V1', 'phone': '450-472-3135', 'demographic': 'people 18 years and over, homeless or at risk of homelessness', 'lat': '45.56022216472333', 'lng': '-73.90146460122374', 'age': '18+', 'gender': 'either', 'capacity': '20', 'gMaps': 'https://www.google.com/maps/place/305+Rue+F%C3%A9r%C3%A9,+Saint-Eustache,+QC+J7R+2V1/@45.5600416,-73.9102193,15z/data=!3m1!4b1!4m5!3m4!1s0x4cc92f8392d47ee1:0x75b43d17f11b9edf!8m2!3d45.5600419!4d-73.9014646', 'distance': '5 hours 25 mins'},
     {'id': '5', 'name': "AIGUILLAGE (L')", 'address': '536 Chicoine Street, Vaudreuil-Dorion, MontÃ©rÃ©gie, QC, J7V 7E4', 'phone': '450-218-6418', 'demographic': 'homeless men and women 18 years old and over', 'lat': '45.376053545234946', 'lng': '-74.02330378773671', 'age': '18+', 'gender': 'either', 'capacity': '20', 'gMaps': 'https://www.google.com/maps/place/536+Rue+Chicoine,+Vaudreuil-Dorion,+QC+J7V+7E4/@45.375895,-74.0320263,15z/data=!3m1!4b1!4m5!3m4!1s0x4cc94816441a2641:0x9577cc278499dc99!8m2!3d45.3758953!4d-74.0232716', 'distance': '7 hours 49 mins'}]
    }

    for shel in hard_coded_data["shelters"]:
        for she in shelters_data["shelters"]:
            if shel['id'] == she['id']:
                shel['capacity'] = she['capacity']

    return render_template("distance.html",shelters_data=hard_coded_data)

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
                print("updating capacity")
                shelter['capacity'] = updated_capacity

        a_file = open("shelters.json", "w")
        json.dump(json_object, a_file)
        a_file.close()




    return render_template("updated.html")

if __name__ == '__main__':
    app.run()
#app.run('0.0.0.0', 8000, debug = True)