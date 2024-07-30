from flask_restful import Resource
from models.guarderias import Guarderias
from flask import render_template, make_response, request
from db import db

class GuarderiasController(Resource):
    def get(self):
        guarderias = Guarderias.query.all()
        return make_response(render_template('guarderia.html', guarderias=guarderias))
    
    def post(self):
        data = request.json
        guarderia = Guarderias(nombre=data["nombre"], direccion=data["direccion"], telefono=data["telefono"])
        db.session.add(guarderia)
        db.session.commit()

    def delete(self):
        data = request.json
        guarderia = Guarderias.query.get(data["id"])
        db.session.delete(guarderia)
        db.session.commit()