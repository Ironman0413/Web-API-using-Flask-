from flask import *
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("SecretKey")
}

@auth.verify_password
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

app = Flask(__name__)

dogBreeds = [{
        "breed": "Labrador Retriever",
        "breedType": "Purebred",
        "origin": "Canada,USA",
        "popularity": 1,
        "temperament": ["Cheerful", "Gentle", "Friendly", "Intelligent"],
        "hypoallergenic": "No",
        "intelligence": 7,
    }, {
        "breed": "German Shepard",
        "breedType": "Purebred",
        "origin": "Germany",
        "popularity": 2,
        "temperament": ["Corageous", "Intelligent", "Loyal", "Watchful"],
        "hypoallergenic": "No",
        "intelligence": 3,
        
    }, {
        "breed": "Golden Retriever",
        "breedType": "Purebred",
        "origin": "United Kingdom",
        "popularity": 3,
        "temperament": ["Intelligent", "Kind", "Friendly", "Confident"],
        "hypoallergenic": "No",
        "intelligence": 4,
        
    }, {
        "breed": "French Bulldog",
        "breedType": "Purebred",
        "origin": "France, UK",
        "popularity": 4,
        "temperament": ["Playful", "Sociable", "Friendly", "Lively", "Patient"],
        "hypoallergenic": "No",
        "intelligence": 58,
        

    }, {
        "breed": "Bulldog",
        "breedType": "Purebred",
        "origin": "United Kingdom",
        "popularity": 5,
        "temperament": ["Friendly", "Docile", "Willful", "Gregarious"],
        "hypoallergenic": "No",
        "intelligence": 77,
        
    }, {
        "breed": "Beagle",
        "breedType": "Purebred",
        "origin": "United Kingdom",
        "popularity": 6,
        "temperament": ["Gentle", "Intelligent", "Even Tempered", "Determined"],
        "hypoallergenic": "No",
        "intelligence": 72,
        
    }, {
        "breed": "Poodle",
        "breedType": "Purebred",
        "origin": "Germany, France",
        "popularity": 7,
        "temperament": ["Intelligent", "Faithful", "Trainable", "Instinctual"],
        "hypoallergenic": "Yes",
        "intelligence": 2,
        

    }, {
        "breed": "Rottweiler",
        "breedType": "Purebred",
        "origin": "Germany",
        "popularity": 8,
        "temperament": ["Intelligent", "Corageous", "Fearless", "Confident"],
        "hypoallergenic": "No",
        "intelligence": 9,
        

    }, {
        "breed": "German Shorthaired Pointer",
        "breedType": "Purebred",
        "origin": "Germany",
        "popularity": 9,
        "temperament": ["Intelligent", "Trainable", "Boisterous", "Cooperative"],
        "hypoallergenic": "No",
        "intelligence": 9,
        
    }, {
        "breed": "Yorkshire Terrier",
        "breedType": "Purebred",
        "origin": "United Kingdom",
        "popularity": 10,
        "temperament": ["Independent", "Intelligent", "Corageous", "Confident"],
        "hypoallergenic": "Yes",
        "intelligence": 27,
        

    } ]

#GET method for accessing the data
@app.route("/dogbreeds",methods=['GET'])
@auth.login_required
def get():
    return jsonify({'dogbreeds': dogBreeds})

#Access dog breeds based on popularity
@app.route("/dogbreeds/<int:popularity>",methods = ['GET'])
@auth.login_required
def get_breeds_of_popularity(popularity):
    return jsonify({'breeds_based_on_popularity':dogBreeds[popularity-1]})

#POST method for adding the data in existing data
@app.route("/dogbreeds/post",methods = ['POST'])
@auth.login_required
def create():
    breed = {
        "breed": "Boxer",
        "breedType": "Purebred",
        "origin": "Germany",
        "popularity": 11,
        "temperament": ["Playful", "Friendly", "Devoted", "Loyal"],
        "hypoallergenic": "No",
        "intelligence": 48,
        }
    dogBreeds.append(breed)
    return jsonify({'Data Added': breed})


#PUT method for modifying values in existing data
@app.route("/dogbreeds/<int:popularity>",methods = ['PUT'])
@auth.login_required
def update(popularity):
    # dogBreeds[popularity-1]['breed'] = "ABCD"
    return jsonify({'DogBreeds': dogBreeds[popularity-1]})

#For deletion of existing data
@app.route("/dogbreeds/<int:popularity>",methods = ['DELETE'])
def delete(popularity):
    dogBreeds.remove(dogBreeds[popularity-1])
    return jsonify({'result':True})

    
if __name__ == "__main__":
    app.run(debug=True)