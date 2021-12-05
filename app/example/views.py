from os import abort
from flask import render_template, redirect, url_for
from flask.helpers import flash
from . import example_bp
from .models import Movie
from .forms import MovieEditForm, MovieNewForm
from services import app_db

@example_bp.route("/", methods=['GET'])
def home_page():
    movies = app_db.session.query(Movie).order_by(Movie.name).all()
    thead_th_items = [
        {'col_title': '#'},
        {'col_title': 'Nombre'},
        {'col_title': 'Duración'},
        {'col_title': 'Categoria'},
        {'col_title': 'Actores'},
        {'col_title': 'Acciones', 'col_span':2}
    ]
    return render_template("example/movies.html", title='Movies', movies = movies, th_items=thead_th_items)

@example_bp.route("/movie/new", methods=['GET', 'POST'])
def new_movie():
    item = Movie()
    form = MovieNewForm()

    if form.validate_on_submit():
        form.populate_obj(item)
        app_db.session.add(item)
        app_db.session.commit()
        flash('Pelicula añadida: '  +  item.name, 'info')
        return redirect(url_for('example.home_page'))

    return  render_template("example/display_form.html", form=form)

@example_bp.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit_movie(movie_id):
    item = app_db.session.query(Movie).filter(Movie.id == movie_id).first()
    if item is  None:
        abort(403)

    form = MovieEditForm(obj=item)

    if form.validate_on_submit():
        form.populate_obj(item)
        app_db.session.commit()
        flash('Pelicula actualizada: '  +  item.name, 'info')
        return redirect(url_for('example.home_page'))

    return  render_template('example/display_form.html', title='Edit friend', form=form)