from flask import Flask
from flask_restful import Resource, Api
from firebase import firebase
import json
from datetime import datetime

app = Flask(__name__)
api = Api(app)

firebase = firebase.FirebaseApplication('https://cookme.firebaseio.com/', None)

class getByRecipeName(Resource):
    def get(self, recipeName):
    	recipe = firebase.get('/recipes/'+recipeName+'/'+recipeName+'',None)
    	ingredients = recipe["ingredients"][0]
        return recipe

class getByIngredient(Resource):
    def get(self, ingredientInput):
        recipeTree = firebase.get('/recipes',None)
        recipeList = []
        for shallowRoot in recipeTree:
            for deepRoot in recipeTree[shallowRoot]:
                recipe = recipeTree[shallowRoot][deepRoot]
                for ingredient in recipe["ingredients"]:
                    ingredientName = ingredient["ingredient name"]
                    if ingredientName == ingredientInput:
                        recipeList.append(recipe)
    		 		   

    	return recipeList
        
class getDefaultRecipes(Resource):
    def get(self):
        # dt = datetime.now()
        # print dt.microsecond
        default = ['Donut', 'Bagel','Waffles', 'Suarez', 'Eduardk']
        
       	ret = []
        for recipeName in default:
            ret.append(firebase.get('/recipes/'+recipeName+'/'+recipeName+'',None))

        print len(ret)
        return ret

api.add_resource(getByIngredient, '/ingredient/<string:ingredientInput>')
api.add_resource(getByRecipeName, '/recipe/<string:recipeName>')
api.add_resource(getDefaultRecipes, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
