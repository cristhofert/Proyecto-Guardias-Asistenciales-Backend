from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://app_user:app0987user@localhost:3306/sggdb?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    code = db.Column(db.String(10), unique=True)

    def __init__(self, name, code):
        self.name = name
        self.code = code

db.create_all()

class ServiceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'code')

service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)

@app.route("/services", methods=["POST"])
def add_service():
    name = request.json['name']
    code = request.json['code']

    new_service = Service(name, code)

    db.session.add(new_service)
    db.session.commit()

    return service_schema.jsonify(new_service)

@app.route("/services", methods=["GET"])
def get_services():
    all_services = Service.query.all()
    result = services_schema.dump(all_services)
    return jsonify(result)     

@app.route("/services/<id>", methods=["GET"])
def get_service(id):
    service = Service.query.get(id)
    return service_schema.jsonify(service)

@app.route("/services/<id>", methods=["PUT"])
def update_service(id):
    service = Service.query.get(id)

    name = request.json['name']
    code = request.json['code']

    service.name = name
    service.code = code

    db.session.commit()
    return service_schema.jsonify(service)

@app.route("/services/<id>", methods=["DELETE"])
def delete_service(id):
    service = Service.query.get(id)
    db.session.delete(service)
    db.session.commit()

    return service_schema.jsonify(service)

if __name__ == "__main__":
    app.run(debug=True)