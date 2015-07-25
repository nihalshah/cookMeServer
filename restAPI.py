from flask import Flask
from flask_restful import Resource, Api
from firebase import firebase

app = Flask(__name__)
api = Api(app)

firebase = firebase.FirebaseApplication('https://cookme.firebaseio.com/', None)

class HelloWorld(Resource):
    def get(self):
    	result = firebase.get('',None)
        return result


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')