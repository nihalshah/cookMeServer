from flask import Flask
from flask_restful import Resource, Api
from firebase import firebase

app = Flask(__name__)
api = Api(app)

firebase = firebase.FirebaseApplication('https://cookme.firebaseio.com/', None)

class getByRecipeName(Resource):
    def get(self, recipeName):
    	recipe = firebase.get('/recipes/'+recipeName+'/'+recipeName+'',None)
    	ingredients = recipe["ingredients"][0]
        return recipe

class getByIngredient(Resource):
    def get(self, ingredient):
    	recipeTree = firebase.get('/recipes',None)
    	recipeList = []
    	# ingredients = recipe["ingredients"][0]
    	for shallowRoot in recipeTree:
    		#print type(recipeTree[shallowRoot])
    		for deepRoot in recipeTree[shallowRoot]:
    		 	recipe = recipeTree[shallowRoot][deepRoot]
    		 	ingredientName = recipe["ingredients"][0]["ingredient name"]

    		 	if ingredientName == ingredient:
    		 		recipeList.append(recipe)

        return recipeList


api.add_resource(getByIngredient, '/ingredient/<string:ingredient>')
api.add_resource(getByRecipeName, '/recipe/<string:recipeName>')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
