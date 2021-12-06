import logging
import os
from flask.helpers import url_for
from flask_restful import Api, Resource
from werkzeug.wrappers.response import Response

from settings import UPLOAD_FOLDER
from .schemas import PokemonSchema
from .models import Pokemon
from . import api_bp
from services import app_db, csrf
from flask import abort, request
from werkzeug.utils import secure_filename

pokemon_schema = PokemonSchema()
api = Api(api_bp, decorators=[csrf.exempt])

def upload_image_pokemon():
    if 'photo' in request.files:
        try:
            file = request.files['photo']
            filename = secure_filename(file.filename)
            path_file = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path_file)
            return url_for('upload_dir', path=filename,  _external=True)
        except Exception as e:
            logging.critical(e)
            return abort(400, 'Problem with upload file')
class PokemonListResource(Resource):
    def get(self):
        pokemons = app_db.session.query(Pokemon).order_by(Pokemon.id).all()
        result = pokemon_schema.dump(pokemons, many=True)
        return result

    def post(self):
        new_pokemon = Pokemon(
            name=request.form.get('name'),
            photo = upload_image_pokemon()
        )
        app_db.session.add(new_pokemon)
        app_db.session.commit()
        return pokemon_schema.dump(new_pokemon)

class PokemonResource(Resource):
    def get(self, pokemon_id):
        pokemon = app_db.session.query(Pokemon).get(pokemon_id)
        if pokemon:
            resp = pokemon_schema.dump(pokemon)
        else:
            abort(404,'Pokemon no encontrado')
        return resp

    def patch(self, pokemon_id):
        pokemon = app_db.session.query(Pokemon).get(pokemon_id)
        if 'name' in request.form:
            pokemon.name = request.form.get('name'),
        if 'photo' in request.files:
            pokemon.photo =upload_image_pokemon()

        app_db.session.commit()
        return pokemon_schema.dump(pokemon)

api.add_resource(PokemonListResource, '/api/pokemon/', endpoint='pokemon_list_resource')
api.add_resource(PokemonResource, '/api/pokemon/<int:pokemon_id>', endpoint='pokemon_resource')