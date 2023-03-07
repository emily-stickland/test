# import Flask and jsonify
from flask import Flask, jsonify

# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse

my_app = Flask(__name__)
my_api = Api(my_app)

class Greet(Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'name'
        parser.add_argument('name', type=str)

        # parse 'name'
        name = parser.parse_args().get('name')

        if name:
            output_message = f'Hi {name}!'
        else:
            output_message = 'Hi person without name!'

        # make json from greeting string 
        return jsonify(greeting_key = output_message)
    
# assign endpoint
my_api.add_resource(Greet, '/greet',)

if __name__ == '__main__':
    my_app.run(debug=True)