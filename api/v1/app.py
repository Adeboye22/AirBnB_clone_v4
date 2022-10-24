#!/usr/bin/python3
<<<<<<< HEAD
"""flask"""
from flask import Flask, render_template, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")
host = getenv('HBNB_API_HOST') if getenv('HBNB_API_HOST') else '0.0.0.0'
port = getenv('HBNB_API_PORT') if getenv('HBNB_API_PORT') else 5000
cors = CORS(app, resources={'/*': {'origins': '0.0.0.0'}})


@app.teardown_appcontext
def teardown_db(self):
    """teardown"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """404ed"""
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
=======
"""create instance of flask, import storage from models, app_views from api.v1.views"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import make_response
from flask import jsonify
from flask_cors import CORS
import os


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """ Handler for 404 errors that returns a JSON 404 status code"""
    return make_response(jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def close_session(db):
    """This method allow close the session"""
    storage.close()


if __name__ == "__main__":
    hst = os.getenv("HBNB_API_HOST", default="0.0.0.0")
    prt = int(os.getenv("HBNB_API_PORT", default=5000))
    app.run(host=hst, port=prt, threaded=True)
>>>>>>> master
