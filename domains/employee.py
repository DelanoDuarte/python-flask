from database.repository import db 
from marshmallow import Schema, fields, post_load

class Employee(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


    def json(self):
        return {
            "id":self.id,
            "name": self.name,
            "surname": self.surname,
            "age": self.age
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

class EmployeeSchema(Schema):

    name = fields.Str()
    surname = fields.Str()
    age = fields.Integer()

    @post_load
    def make_user(self, data, **kwargs):
        return Employee(**data)