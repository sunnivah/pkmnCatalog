#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Generation, Pokemon, User


engine = create_engine('postgresql://catalog:catalog@18.196.63.184/pkmnCatalog')
Base.metadata.bind = engine
# bind code and engine
DBSession = sessionmaker(bind=engine)
# create instance of DBSession()
session = DBSession()

# Create dummy user
User1 = User(name="Nathalia Mustermann", email="natalie.koop@bmw.de",
             picture='https://www.w3schools.com/w3images/avatar2.png')
session.add(User1)
session.commit()

# add generations
gen1 = Generation(generation_name='Generation I')
session.add(gen1)
gen2 = Generation(generation_name='Generation II')
session.add(gen2)
gen3 = Generation(generation_name='Generation III')
session.add(gen3)
gen4 = Generation(generation_name='Generation IV')
session.add(gen4)
gen5 = Generation(generation_name='Generation V')
session.add(gen5)
gen6 = Generation(generation_name='Generation VI')
session.add(gen6)
session.commit()

# add pokemon of gen 1
session.add(Pokemon(
            pkmn_id="#001",
            pkmn_picture="https://cdn.bulbagarden.net/upload/e/ec/001MS.png",
            pkmn_name="Bulbasaur",
            pkmn_type="Grass, Poison",
            generation_relationship=gen1,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#002",
            pkmn_picture="https://cdn.bulbagarden.net/upload/6/6b/002MS.png",
            pkmn_name="Ivysaur",
            pkmn_type="Grass, Poison",
            generation_relationship=gen1,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#003",
            pkmn_picture="https://cdn.bulbagarden.net/upload/d/df/003MS.png",
            pkmn_name="Venusaur",
            pkmn_type="Grass, Poison",
            generation_relationship=gen1,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#004",
            pkmn_picture="https://cdn.bulbagarden.net/upload/b/bb/004MS.png",
            pkmn_name="Charmander",
            pkmn_type="Fire",
            generation_relationship=gen1,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#005",
            pkmn_picture="https://cdn.bulbagarden.net/upload/d/dc/005MS.png",
            pkmn_name="Charmeleon",
            pkmn_type="Fire",
            generation_relationship=gen1,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#006",
            pkmn_picture="https://cdn.bulbagarden.net/upload/0/01/006MS.png",
            pkmn_name="Charizard",
            pkmn_type="Fire, Flying",
            generation_relationship=gen1,
            user_id=1)
            )
session.commit()

# add pokemon of gen 2
session.add(Pokemon(
            pkmn_id="#152",
            pkmn_picture="https://cdn.bulbagarden.net/upload/7/79/152MS.png",
            pkmn_name="Chikorita",
            pkmn_type="Grass",
            generation_relationship=gen2,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#153",
            pkmn_picture="https://cdn.bulbagarden.net/upload/3/31/153MS.png",
            pkmn_name="Bayleef",
            pkmn_type="Grass",
            generation_relationship=gen2,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#154",
            pkmn_picture="https://cdn.bulbagarden.net/upload/8/89/154MS.png",
            pkmn_name="Meganium",
            pkmn_type="Grass",
            generation_relationship=gen2,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#155",
            pkmn_picture="https://cdn.bulbagarden.net/upload/3/39/155MS.png",
            pkmn_name="Cyndaquil",
            pkmn_type="Fire",
            generation_relationship=gen2,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#156",
            pkmn_picture="https://cdn.bulbagarden.net/upload/3/36/156MS.png",
            pkmn_name="Quilava",
            pkmn_type="Fire",
            generation_relationship=gen2,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#157",
            pkmn_picture="https://cdn.bulbagarden.net/upload/5/56/157MS.png",
            pkmn_name="Typhlosion",
            pkmn_type="Fire",
            generation_relationship=gen2,
            user_id=1)
            )
session.commit()

# add pokemon of gen 3
session.add(Pokemon(
            pkmn_id="#252",
            pkmn_picture="https://cdn.bulbagarden.net/upload/c/cf/252MS.png",
            pkmn_name="Treecko",
            pkmn_type="Grass",
            generation_relationship=gen3,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#253",
            pkmn_picture="https://cdn.bulbagarden.net/upload/a/a5/253MS.png",
            pkmn_name="Grovyle",
            pkmn_type="Grass",
            generation_relationship=gen3,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#254",
            pkmn_picture="https://cdn.bulbagarden.net/upload/f/ff/254MS.png",
            pkmn_name="Sceptile",
            pkmn_type="Grass",
            generation_relationship=gen3,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#255",
            pkmn_picture="https://cdn.bulbagarden.net/upload/d/d5/255MS.png",
            pkmn_name="Torchic",
            pkmn_type="Fire",
            generation_relationship=gen3,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#256",
            pkmn_picture="https://cdn.bulbagarden.net/upload/4/4d/256MS.png",
            pkmn_name="Combusken",
            pkmn_type="Fire, Fighting",
            generation_relationship=gen3,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#257",
            pkmn_picture="https://cdn.bulbagarden.net/upload/3/3e/257MS.png",
            pkmn_name="Blaziken",
            pkmn_type="Fire, Fighting",
            generation_relationship=gen3,
            user_id=1)
            )
session.commit()

# add pokemon of gen 4
session.add(Pokemon(
            pkmn_id="#387",
            pkmn_picture="https://cdn.bulbagarden.net/upload/2/27/387MS.png",
            pkmn_name="Turtwig",
            pkmn_type="Grass",
            generation_relationship=gen4,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#388",
            pkmn_picture="https://cdn.bulbagarden.net/upload/4/40/388MS.png",
            pkmn_name="Grotle",
            pkmn_type="Grass",
            generation_relationship=gen4,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#389",
            pkmn_picture="https://cdn.bulbagarden.net/upload/1/1f/389MS.png",
            pkmn_name="Torterra",
            pkmn_type="Grass, Ground",
            generation_relationship=gen4,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#390",
            pkmn_picture="https://cdn.bulbagarden.net/upload/9/93/390MS.png",
            pkmn_name="Chimchar",
            pkmn_type="Fire",
            generation_relationship=gen4,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#391",
            pkmn_picture="https://cdn.bulbagarden.net/upload/7/70/391MS.png",
            pkmn_name="Monferno",
            pkmn_type="Fire, Fighting",
            generation_relationship=gen4,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#392",
            pkmn_picture="https://cdn.bulbagarden.net/upload/f/f5/392MS.png",
            pkmn_name="Infernape",
            pkmn_type="Fire, Fighting",
            generation_relationship=gen4,
            user_id=1)
            )
session.commit()

# add pokemon of gen 5
session.add(Pokemon(
            pkmn_id="#494",
            pkmn_picture="https://cdn.bulbagarden.net/upload/0/0c/494MS.png",
            pkmn_name="Victini",
            pkmn_type="Psychich, Fire",
            generation_relationship=gen5,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#495",
            pkmn_picture="https://cdn.bulbagarden.net/upload/2/23/495MS.png",
            pkmn_name="Snivy",
            pkmn_type="Grass",
            generation_relationship=gen5,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#496",
            pkmn_picture="https://cdn.bulbagarden.net/upload/8/8f/496MS.png",
            pkmn_name="Servine",
            pkmn_type="Grass",
            generation_relationship=gen5,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#497",
            pkmn_picture="https://cdn.bulbagarden.net/upload/2/2e/497MS.png",
            pkmn_name="Serperior",
            pkmn_type="Grass",
            generation_relationship=gen5,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#498",
            pkmn_picture="https://cdn.bulbagarden.net/upload/6/6f/498MS.png",
            pkmn_name="Tepig",
            pkmn_type="Fire",
            generation_relationship=gen5,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#499",
            pkmn_picture="https://cdn.bulbagarden.net/upload/2/29/499MS.png",
            pkmn_name="Pignite",
            pkmn_type="Fire, Fighting",
            generation_relationship=gen5,
            user_id=1)
            )
session.commit()

# add pokemon of gen 6
session.add(Pokemon(
            pkmn_id="#650",
            pkmn_picture="https://cdn.bulbagarden.net/upload/6/67/650MS.png",
            pkmn_name="Chespin",
            pkmn_type="Psychich, Fire",
            generation_relationship=gen6,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#651",
            pkmn_picture="https://cdn.bulbagarden.net/upload/b/bf/651MS.png",
            pkmn_name="Quilladin",
            pkmn_type="Grass",
            generation_relationship=gen6,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#652",
            pkmn_picture="https://cdn.bulbagarden.net/upload/1/1c/652MS.png",
            pkmn_name="Chesnaught",
            pkmn_type="Grass, Fighting",
            generation_relationship=gen6,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#653",
            pkmn_picture="https://cdn.bulbagarden.net/upload/f/f9/653MS.png",
            pkmn_name="Fennekin",
            pkmn_type="Fire",
            generation_relationship=gen6,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#654",
            pkmn_picture="https://cdn.bulbagarden.net/upload/6/62/654MS.png",
            pkmn_name="Braixen",
            pkmn_type="Fire",
            generation_relationship=gen6,
            user_id=1)
            )
session.add(Pokemon(
            pkmn_id="#655",
            pkmn_picture="https://cdn.bulbagarden.net/upload/f/f8/655MS.png",
            pkmn_name="Delphox",
            pkmn_type="Fire, Psychic",
            generation_relationship=gen6,
            user_id=1)
            )
session.commit()
