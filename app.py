from flask import Flask
import dbhelper
import json


app = Flask(__name__)

@app.get('/animals')
# created a function called get_animals
def get_animals():
# calls the procedure get_animals and stores it as results
    results = dbhelper.run_statment('CALL get_animals()')
    if(type(results) == list):
# takes results and changes it into json, and stores in as variable animals_json. default=str puts it as a string if it cant make it into json
        animals_json = json.dumps(results, default=str)
#returns the variable animals_json
        return animals_json
    else:
        return 'sorry something unexpected has happened'


@app.get('/dogs')
# created a function called get_dogs
def get_dogs():
    # calls the procedure get_dogs and stores it as results
    results = dbhelper.run_statment('CALL get_dogs()')
    if(type(results) == list):
        # takes results and changes it into json, and stores in as variable dogs_json. default=str puts it as a string if it cant make it into json
        dogs_json = json.dumps(results, default=str)
        #returns the variable dogs_json
        return dogs_json
    else:
        return 'sorry something unexpected has happened'


@app.get('/cats')
# created a function called get_cats
def get_cats():
    # calls the procedure get_cat and stores it as results
    results = dbhelper.run_statment('CALL get_cat()')
    if(type(results) == list):
        # takes results and changes it into json, and stores in as variable cats_json. default=str puts it as a string if it cant make it into json
        cats_json = json.dumps(results, default=str)
         #returns the variable cats_json
        return cats_json
    else:
        return 'sorry something unexpected has happened'

app.run(debug=True)