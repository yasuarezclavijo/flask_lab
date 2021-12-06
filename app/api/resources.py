from flask_restful import Api, Resource
from werkzeug.wrappers.response import Response
from .schemas import PokemonSchema
from .models import Pokemon
from . import api_bp
from services import app_db
from flask import abort

pokemon_schema = PokemonSchema()
api = Api(api_bp)

class PokemonListResource(Resource):
    def get(self):
        pokemons = app_db.session.query(Pokemon).order_by(Pokemon.id).all()
        result = pokemon_schema.dump(pokemons, many=True)
        return result

class PokemonResource(Resource):
    def get(self, pokemon_id):
        pokemon = app_db.session.query(Pokemon).get(pokemon_id)
        if pokemon:
            resp = pokemon_schema.dump(pokemon)
        else:
            abort(404,'Pokemon no encontrado')
        return resp

api.add_resource(PokemonListResource, '/api/pokemon/', endpoint='pokemon_list_resource')
api.add_resource(PokemonResource, '/api/pokemon/<int:pokemon_id>', endpoint='pokemon_resource')