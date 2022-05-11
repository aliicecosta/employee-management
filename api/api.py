from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from database.models import Employee

engine =  create_engine("postgresql://admin:root@postgres_container:5432/employees")

app = Flask(__name__)
api = Api(app)

# Adds an argument to requests
parser = reqparse.RequestParser()
parser.add_argument('registration')
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
        with Session(engine) as session:
            new = Employee(
                registration = data['registration'],
                name = data['name'],
                surname = data['surname'],
                role = data['role'],
                leader = data['leader'],
                salary = data['salary'],
                password = data['password'],
                status = data['status']
            )
            session.add(new)
            session.commit()
        return "New registration successfully completed.", 201

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

class GetEmployee(Resource):
    """
    Return data from on or all employees.
    If any registration number is passed, it returns all the registered employees.
    """

    def get(self, registration=None):
        employees = []

        # Create the SQL Query
        if registration:
            stmt = select(Employee).where(Employee.registration == registration)
        else:
            stmt = select(Employee)

        # Execute Query
        with engine.connect() as session:
            for row in session.execute(stmt):
                
                # Get data from database response
                data = {
                    "registration" : row[0],
                    "name" : row[1],
                    "surname" : row[2],
                    "role": row[3],
                    "leader" : row[4],
                    "salary" : row[5],
                    "password" : row[6],
                    "status" : row[7]        
                }
                employees.append(data)
                
        return employees, 200

api.add_resource(HelloWorld, '/')
api.add_resource(AddNewEmployee, '/addNewEmployee')
api.add_resource(UpdateEmployeeData, '/updateEmployeeData')
api.add_resource(DeleteEmployee, '/deleteEmployee')
api.add_resource(GetEmployee, '/getEmployee', '/getEmployee/<registration>')


if __name__ == '__main__':
    from database.models import Base
    Base.metadata.create_all(engine)
    app.run(debug=True, host='0.0.0.0')