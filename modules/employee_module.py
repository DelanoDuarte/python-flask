from flask import Blueprint, request
from domains.employee import Employee, EmployeeSchema

employee_blueprint = Blueprint("employee", __name__)

@employee_blueprint.route("/")
def index():
    return {"employee": "index"}

@employee_blueprint.route("/list")
def list():
    employees = Employee.query.all()
    return {"employees": [emp.json() for emp in employees]}


@employee_blueprint.route("/add", methods=['POST'])
def add():
    employee = EmployeeSchema()
    employee_data = employee.load(request.get_json())
    employee_data.save()

    return {"employee": employee_data.json()}

