from flask import Flask 
from firebase import firebase
import requests

firebase = firebase.FirebaseApplication('https://cookme.firebaseio.com/', None)
app = Flask(__name__)

@app.route("/")
def tempRecipe():
	result = firebase.get('',None)
	print result
	return "result"


@app.route("/GET/<recipeName>")
def getRecipe(recipeName):
	recipe = firebase.get('/recipes/'+recipeName+'/'+recipeName+'',None)
    print "instructions are : " + recipe["instructions"]
    ingredients = recipe["ingredients"][0]
    return render_template('layout.html',recipe=recipe, ingredients = ingredients)


if __name__ == '__main__':
	app.run(port=4000)
