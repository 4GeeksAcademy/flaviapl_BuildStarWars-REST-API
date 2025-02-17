"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planet, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



# @app.route('/user', methods=['GET'])
# def handle_hello():

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200



@app.route('/people', methods=['GET'])
def get_all_people():

    all_people = People.query.all()
    print(all_people)

    results = list(map(lambda people: people.serialize(), all_people))
    print(results)


    # response_body = {
    #     "msg": "Hello, this is your GET /people response ",
    #     "results": results
    # }

    return jsonify(results), 200               #se vuoi che appaia response_body lo metti tra parentesi, altrimenti metti direttamente "results" che è la variabile che racchiude la lista



@app.route('/people/<int:people_id>', methods=['GET'])
def get_single_people(people_id):

    single_people = People.query.get(people_id)
    print(single_people.serialize())

    return jsonify(single_people.serialize()), 200   
      





@app.route('/planets', methods=['GET'])
def get_all_planets():

    all_planets = Planet.query.all()
    print(all_planets)

    results2 = list(map(lambda planet: planet.serialize(), all_planets))
    print(results2)


    # response_body = {
    #     "msg": "Hello, this is your GET /people response ",
    #     "results": results
    # }

    return jsonify(results2), 200       



@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_single_planet(planet_id):

    single_planet = Planet.query.get(planet_id)
    print(single_planet.serialize())

    return jsonify(single_planet.serialize()), 200   





@app.route('/users', methods=['GET'])
def get_all_users():

    all_planets = User.query.all()
    print(all_planets)

    results_planets = list(map(lambda planet: planet.serialize(), all_planets))

    return jsonify(results_planets), 200


@app.route('/users/favorites', methods=['GET'])
def get_all_favorites():

    all_favorites = Favorites.query.all()
    print(all_favorites)

    results_favorites = list(map(lambda fav: fav.serialize(), all_favorites))
 
    return jsonify(results_favorites), 200



@app.route('/users/<int:user_id>/favorites/planet/<int:planet_id>', methods=['POST'])
def add_planet_to_favorites(user_id, planet_id):
    print(request)                      #request è un oggetto di Flask che contiene tutte le informazioni relative alla richiesta dal client
    print(request.json)

    user = User.query.get(user_id)    # Recupera l'utente dal database

    planet = Planet.query.get(planet_id)   # Recupera il pianeta dal database

    body = request.json

    new_fav = Favorites(user_id= user_id, planet_id = planet_id, planet_name = body["planet_name"], people_id=None, people_name=None )
    db.session.add(new_fav) 
    db.session.commit()
     
    return jsonify(), 200









# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
