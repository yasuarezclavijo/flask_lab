from enum import auto
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey,  Integer, String, Table
from sqlalchemy.orm import relationship

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    duration_minutes = Column(Integer)
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates='movies')
    actors = relationship('Actor', secondary='actor_per_movie')


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    movies = relationship(
        'Movie', back_populates='category', order_by=Movie.name)


class Actor(Base):
    __tablename__ = 'actor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    movies = relationship(Movie, back_populates='actors', secondary='actor_per_movie')


class ActorPerMovie(Base):
    __tablename__ = 'actor_per_movie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    actor_id = Column(
        Integer,
        ForeignKey('actor.id'),
        primary_key = True
    )

    movie_id = Column(
        Integer,
        ForeignKey('movie.id'),
        primary_key = True
    )
