#!/usr/bin/env python3

# --------- USED SOURCES ---------
# The bootstap template is used from
# https://startbootstrap.com/templates/simple-sidebar/

# The login fuctionality is mainly used from Udacity
# https://github.com/udacity/Full-Stack-Foundations/tree/master/Lesson-3

from flask import render_template, request, redirect, url_for, flash, jsonify
from flask import Flask
from sqlalchemy import create_engine, Unicode
from sqlalchemy.orm import joinedload, relationship, sessionmaker
from database_setup import Base, Generation, Pokemon, User
# login requirements
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__) 
engine = create_engine('postgresql://catalog:catalog@18.196.63.184/pkmnCatalog')
Base.metadata.bind = engine
CLIENT_ID = json.loads(open('client_secrets.json', 'r')
                       .read())['web']['client_id']
APPLICATION_NAME = "Pokemon Catalog Application"
DBSession = sessionmaker(bind=engine)
session = DBSession()


# api endpoint to get all pokemon data grouped by generation
@app.route('/api/v1/pokemonCatalog')
def pokemonCatalogJSON():
    generations = session.query(Generation).options(
                                joinedload(Generation.pokemons)).all()
    return jsonify(PokemonCatalog=[dict(c.serializable,
                   pokemons=[i.serializable for i in c.pokemons])
                   for c in generations])


# api endpoint to get specific pokemon data of a generation
# e.g. http://localhost:8000/api/v1/generations/1/1
@app.route('/api/v1/generations/<int:generation_id>/<int:pokemon_id>')
def pokemonJSON(generation_id, pokemon_id):
    generation = session.query(Generation).filter_by(id=generation_id).one()
    pokemon = session.query(Pokemon).filter_by(id=pokemon_id).one()
    return jsonify(Pokemon=[pokemon.serializable])


# route to login page
@app.route('/login')
def showLogin():
    generations = session.query(Generation)
    # Create anti forgery state token in order to prevent CSRF attacks
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state, generations=generations)


# login-connect logic and redirect
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/'
           'tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
                                'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    # add name, picture and mail to login_session. This is
    # required to continue to work with it in this
    # application.
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    # add login_session as true for template.
    # Required in the template to switch between
    # login and logout button.
    login_session['loged_in'] = True
    generations = session.query(Generation)
    return render_template('index.html', generations=generations)


# User functions to store new data from logedin user.
# Returns user id created in data base.
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# Uses user.id from createUser function and returns user object.
def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


# returns the user.id by checking for email
# data which is used as input paramter.
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# login-disconnect logic and redirect.
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    # check if access token exists. Negative case:
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user '
                                 'not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # In case access token exists, request to revoke the token at google.
    address = 'https://accounts.google.com/o/oauth2/revoke?token='
    url = str(address + login_session['access_token'])
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    # response for positive revoke request
    if result['status'] == '200':
        # delete all data stored in login_session (clear)
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        # add login_session as false for template.
        # Required in the template to switch between
        # login and logout button -> login.
        login_session['loged_in'] = False
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash("Successfully disconnected!")
        # redirect
        generations = session.query(Generation)
        return render_template('index.html', generations=generations)
    # response for negative revoke request
    else:
        response = make_response(json.dumps('Failed to revoke '
                                 'token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# routing to index page
@app.route('/', methods=['GET'])
def noGeneration():
    generations = session.query(Generation)
    if request.method == 'GET':
        return render_template('index.html', generations=generations)


# routing to pkmn overview grouped by generation
@app.route('/<int:generation_id>/')
@app.route('/generations/<int:generation_id>/')
def generations(generation_id):
    generation = session.query(Generation).filter_by(id=generation_id).one()
    generations = session.query(Generation)
    pokemons = session.query(Pokemon).filter_by(generation_id=generation_id)
    return render_template('pkmn.html',
                           generation=generation,
                           generations=generations,
                           pokemons=pokemons,
                           generation_id=generation_id)


# routing to 'create new pkmn'
@app.route('/generations/<int:generation_id>/new/', methods=['GET', 'POST'])
def newPkmn(generation_id):
    # check if user is logged in in order to create pkmn
    if 'username' not in login_session:
        return redirect('/login')
    generation = session.query(Generation).filter_by(id=generation_id).one()
    generations = session.query(Generation)
    if request.method == 'POST':
        session.add(Pokemon(pkmn_id=request.form['pkmn_id'],
                    pkmn_picture=request.form['pkmn_picture'],
                    pkmn_name=request.form['pkmn_name'],
                    pkmn_type=request.form['pkmn_type'],
                    user_id=login_session['user_id'],
                    generation_id=generation_id))
        session.commit()
        flash("A new pokemon has been created.")
        return redirect(url_for('generations', generation_id=generation_id))
    else:
        return render_template('newPkmn.html',
                               generation_id=generation_id,
                               generations=generations,
                               generation=generation)


# routing to 'edit pkmn'
@app.route('/generations/<int:generation_id>'
           '/<int:pokemon_id>/edit/', methods=['GET', 'POST'])
def editPkmn(generation_id, pokemon_id):
    editedPkmn = session.query(Pokemon).filter_by(id=pokemon_id).one()
    generation = session.query(Generation).filter_by(id=generation_id).one()
    generations = session.query(Generation)
    # check if user is logged in in order to edit pkmn
    if 'username' not in login_session:
        return redirect('/login')
    # check if user has permission to edit pkmn
    if editedPkmn.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized"
        " to edit this pokemon. Please create your own pokemon in order to "
        "edit.');}</script><body onload='myFunction()''>"
    # persist all data inserted in editPkmn.html
    if request.method == 'POST':
        if request.form['pkmn_id']:
            editedPkmn.pkmn_id = request.form['pkmn_id']
            session.add(editedPkmn)
            session.commit()
        if request.form['pkmn_picture']:
            editedPkmn.pkmn_picture = request.form['pkmn_picture']
            session.add(editedPkmn)
            session.commit()
        if request.form['pkmn_name']:
            editedPkmn.pkmn_name = request.form['pkmn_name']
            session.add(editedPkmn)
            session.commit()
        if request.form['pkmn_type']:
            editedPkmn.pkmn_type = request.form['pkmn_type']
            session.add(editedPkmn)
            session.commit()
        flash("The pokemon information has been edited.")
        return redirect(url_for('generations', generation_id=generation_id))
    else:
        return render_template(
            'editPkmn.html', generation_id=generation_id,
            pokemon_id=pokemon_id,  editedPkmn=editedPkmn,
            generations=generations, generation=generation)


# routing to 'delete pkmn'
@app.route('/generations/<int:generation_id>/'
           '<int:pokemon_id>/delete/', methods=['GET', 'POST'])
def deletePkmn(generation_id, pokemon_id):
    generation = session.query(Generation).filter_by(id=generation_id).one()
    generations = session.query(Generation)
    pkmnToDelete = session.query(Pokemon).filter_by(id=pokemon_id).one()
    # check if user is logged in in order to delete pkmn
    if 'username' not in login_session:
        return redirect('/login')
    # check if user has permission to delete pkmn
    if pkmnToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are "
        "not authorized to delete this pokemon. Please create your "
        "own pokemon in order to delete.');}</script><body "
        "onload='myFunction()''>"
    if request.method == 'POST':
        # delete specific pokemon stored
        # as "pkmnToDelete" result.
        session.delete(pkmnToDelete)
        session.commit()
        flash("The pokemon has been deleted.")
        return redirect(url_for('generations', generation_id=generation_id))
    else:
        return render_template('deletePkmn.html',
                               pkmnToDelete=pkmnToDelete,
                               generations=generations,
                               generation=generation)

if __name__ == '__main__':
    app.secret_key = 'my_secret_key_placeholder'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
