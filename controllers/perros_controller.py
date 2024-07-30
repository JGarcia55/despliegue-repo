from flask_restful import Resource
from models.perros import Perros
from flask import render_template, make_response

class PerrosController(Resource):
    def get(self):
        perros = Perros.query.all()
        return make_response(render_template('perros.html', perros = perros))