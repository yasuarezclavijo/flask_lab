"""
schemas.py
Archivo para serializar los modelos. Seriealización es el proceso de controlar a traves de objetos
la respuesta y manejo de los atributos de la API.
"""
from marshmallow import fields
from services import ma
from .models import Pokemon

class PokemonSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "photo")
        model = Pokemon