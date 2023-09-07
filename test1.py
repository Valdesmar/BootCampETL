from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# Creating a Flask App
app = Flask(__name__)
# Creating a API object
api = Api(app)


# Class for the http methods 
class Test(Resource):
    
    # GET request
    def get(self):
        return jsonify({'message': 'hello world'})
    

    # POST request
    def post(self):
        data = request.get_json()       # Status Code
        return jsonify({'data': data}), 201


api.add_resource(Test, '/')


# driver function
if __name__ == '__main__':
        app.run(debug = True)

