import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorites = relationship("Favorites", ForeignKey('favorites.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    fav_by_id = Column(Integer, ForeignKey('user.id'))
    character = Column(Integer, ForeignKey('character.id'))
    habitate = Column(Integer, ForeignKey('habitat.id'))

class Character(Base):
    __tablename__ = 'character'
    id=Column(Integer, primary_key=True)
    char_name = Column(String(250), nullable=False)
    char_description = Column(String(250), nullable=False)
    char_habitat = Column(Integer, ForeignKey('habitat.id'))
    char_img_url = Column(String(250), nullable=True)

class Habitat(Base):
    __tablename__ = 'habitat'
    id=Column(Integer, primary_key=True)
    habitat_name = Column(String(250), nullable=False)
    habitat_description = Column(String(250), nullable=False)
    inhabitants = Column(Integer, ForeignKey('character.id'))







    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
