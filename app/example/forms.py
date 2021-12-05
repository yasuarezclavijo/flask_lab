# forms.py
from flask_wtf import  FlaskForm
from wtforms import  IntegerField, StringField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import InputRequired, Length
from wtforms_alchemy import model_form_factory
from .models import Movie, Actor, Category
from services import app_db

ModelForm = model_form_factory(FlaskForm)

class CategoryForm(ModelForm):
    class Meta:
        model = Category

class MovieFormMixin(ModelForm):
    class Meta:
        model = Movie

    category = QuerySelectField(
        query_factory=lambda: app_db.session.query(Category).all(),
        get_pk=lambda category: category.id,
        get_label=lambda category: category.name,
        allow_blank=False,
    )

    actors = QuerySelectMultipleField(
        query_factory=lambda: app_db.session.query(Actor).all(),
        get_pk=lambda actor: actor.id,
        get_label=lambda actor: f"{actor.first_name} {actor.last_name}",
        allow_blank=False,
    )

class MovieNewForm(MovieFormMixin):
    submit = SubmitField('Guardar')

class MovieEditForm(MovieFormMixin):
    submit = SubmitField('Actualizar')
