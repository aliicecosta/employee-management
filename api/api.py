from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine, select, update, delete
from sqlalchemy.orm import Session
from database.models import Employee

from utils import schema_NewEmployee
from jsonschema import validate, ValidationError

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
    Receive information about new Employees and insert into the database.
    JSON format:
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

        # Get and validate request data
        data = request.get_json()
        try:
            validate(data, schema_NewEmployee)
        except ValidationError as ex:
            return "Validation Error! " + str(ex.message), 500

        # Insert new employee using ORM Session
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
    Update one, or more, employees data.
    JSON format:
        data = {
            "registration" : id,
            "args" : [],
            "values" : []
        }
    """
    def post(self):
        data = request.get_json()

        # Build a dict with values to update
        values = {}
        for i in range(len(data['args'])):
            values[data['args'][i]] = data['values'][i]
        
        # Create and execute query to update database with new values
        with engine.connect() as conn:
            stmt = update(Employee).where(Employee.registration == data['registration']).values(values)
            conn.execute(stmt)

        return "Data has been updated successfully!", 201

class DeleteEmployee(Resource):
    """
    Delete from the database a employee by its registration.
    """
    def post(self, registration):

        with engine.connect() as conn:
            stmt = delete(Employee).where(Employee.registration == registration)
            conn.execute(stmt)

        return "Data has been deleted successfully!", 201

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
        with engine.connect() as conn:
            for row in conn.execute(stmt):

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
api.add_resource(DeleteEmployee, '/deleteEmployee/<registration>')
api.add_resource(GetEmployee, '/getEmployee', '/getEmployee/<registration>')


if __name__ == '__main__':
    from database.models import Base
    Base.metadata.create_all(engine)
    app.run(debug=True, host='0.0.0.0')