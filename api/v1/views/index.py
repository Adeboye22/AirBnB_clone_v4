#!/usr/bin/python3
<<<<<<< HEAD
"""following directions"""
from api.v1.views import app_views
from flask import jsonify, Blueprint, render_template, abort
from models import storage
from models.amenity import Amenity
=======
"""Index of the application"""
from api.v1.views import app_views
from models.amenity import Amenity
from models.base_model import BaseModel
>>>>>>> master
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
<<<<<<< HEAD


@app_views.route('/status', methods=['GET'])
def status():
    """status"""
    return (jsonify({"status": "OK"}))


@app_views.route('/stats', methods=['GET'])
def stats():
    return (jsonify({"amenities": storage.count(Amenity),
                     "cities": storage.count(City),
                     "places": storage.count(Place),
                     "reviews": storage.count(Review),
                     "states": storage.count(State),
                     "users": storage.count(User)}))
=======
from models import storage
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def Index():
    """Function index"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def number_objects():
    """counts the number of objects for each model"""

    classes = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User}
    dictionary = {}
    for key, cl in classes.items():
        numb = storage.count(cl)
        dictionary[key] = numb
    return jsonify(dictionary)
>>>>>>> master
