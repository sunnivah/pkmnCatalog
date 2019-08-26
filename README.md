# Pokemon Catalog

Pokemon Catalog is an online database to document'em all. Right now, there are pokemon from first to sixth generation maintained. You are invited to help to complete the catalog!

#### Frameworks
Pokemon Catalog is developed with following tools and frameworks:
* python 3
* Bootstrap
* Flask
* SQLAlchemy
* httplib2
* json
* requests
* oauth2client.client
* string
* random

## Installation
#### Prerequsites
In order to run News Reporting, you have to download:
* [install virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [install vagrant](https://www.vagrantup.com/downloads.html)

#### VM Configuration
How to configure virtualbox and vagrant is documented [here](https://classroom.udacity.com/nanodegrees/nd004-ent/parts/72d6fe39-3e47-45b4-ac52-9300b146094f/modules/0f94ae26-c39d-4231-924b-b1eb6e06cf41/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0).

#### Database Setup
navigate into the `/catalog` root directory and execute the following commands:
* `$python database_setup.py`
This command creates the tables "user", "generation" and "pokemon" in an sqllite database pkmnCatalog.db.

* `$python populate_db.py`
This command does an initial population of the tables "user", "generation" and "pokemon".

## Usage
#### Starting the Application
In order to start Pokemon Catalog, `navigate into the `/catalog` root directory and execute the following commands:
* `$python main.py`

Now, you can access Pokemon Catalog `http://localhost:8000/`.

#### Accessing the Pokemon Catalog API
An API is accessible under following link:
* `http://localhost:8000/api/v1/pokemonCatalog`
The API gives you an output of all persisted Pokemon grouped by Generation.

* `https://localhost:8000/api/v1/generations/<int:generation_id>/<int:pokemon_id>`
The API gives you the information on a specific pokemon of a specific generation (e.g.: http://localhost:8000/api/v1/generations/1/1)

#### Edit, Delete and Create Pokemon
In order to create, delete and edit data, you need to log in with you google account. You can create an account here: [Google Sign Up](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp])

Note that you can only edit and delte pokemon that you have crwated yourself!
