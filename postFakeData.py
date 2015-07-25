from flask import Flask 
from firebase import firebase
import json
from pprint import pprint
import requests
app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://cookme.firebaseio.com', None)

with open("testdata.json") as jsonFile:
	data = json.load(jsonFile)

for recipes in data['recipes']:
	data = {recipes['name']:recipes}
	result = requests.put('https://cookme.firebaseio.com/recipes/'+recipes['name']+'.json', json.dumps(data))
	print result.status_code
