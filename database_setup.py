#!/usr/bin/env python3
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


# class and table definition
class Generation(Base):
    __tablename__ = 'generation'

    id = Column(Integer, primary_key=True)
    generation_name = Column(String(20), nullable=False)

    @property
    def serializable(self):
        return {
            'generations': self.generation_name
        }


class Pokemon(Base):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True)
    pkmn_id = Column(String(20), nullable=False)
    pkmn_picture = Column(String(250), nullable=False)
    pkmn_name = Column(String(20), nullable=False)
    pkmn_type = Column(String(20), nullable=False)
    generation_id = Column(Integer, ForeignKey('generation.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    generation_relationship = relationship(Generation, backref='pokemons')
    user_relationship = relationship(User, backref='pokemons')

    @property
    def serializable(self):
        return {
            'pkmn_id': self.pkmn_id,
            'pkmn_name': self.pkmn_name,
            'pkmn_type': self.pkmn_type
        }


engine = create_engine('postgresql://catalog:catalog@18.196.63.184/pkmnCatalog')
Base.metadata.create_all(engine)
