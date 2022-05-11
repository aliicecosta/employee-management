from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class AddNewEmployee(Resource):
    """
    Receive information about new Employees.
    data = {
        "name" : string,
        "surname" : string,
        "registration" : int,
        "role": string,
        "leader" string,
        "salary" : float,
        "password" : string,
        "status" : bool        
    }
    """
    def post(self):
        data = request.get_json()
        
        return data, 201

class UpdateEmployeeData(Resource):
    """
    data = {
        "registration" : id,
        "args" : [],
        "values" : []
    }
    """
    def post(self):
        data = request.get_json()

        return data, 201

class DeleteEmployee(Resource):
    """
    data = {
        "registration" : int
    }
    """
    def post(self):
        data = request.get_json()
        
        return data, 201

parser = reqparse.RequestParser()
parser.add_argument('registration')
class GetEmployee(Resource):
    def get(self, registration=None):
        if registration:
            return 'Only one employee', 200
        else:
            return 'All employees', 200


api.add_resource(HelloWorld, '/')
api.add_resource(AddNewEmployee, '/addNewEmployee')
api.add_resource(UpdateEmployeeData, '/updateEmployeeData')
api.add_resource(DeleteEmployee, '/deleteEmployee')
api.add_resource(GetEmployee, '/getEmployee', '/getEmployee/<registration>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')