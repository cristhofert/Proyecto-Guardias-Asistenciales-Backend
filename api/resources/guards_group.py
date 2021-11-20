#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse, inputs, fields
from flask_jwt_extended import jwt_required, current_user
from models.guards_group import GuardsGroupModel

class GuardsGroup(Resource):

    def __init__(self):
        pass

    @jwt_required()
    def get(self, id):
        groups = GuardsGroupModel.find_by_id(id)
        if groups and (groups.json()['institution'] == current_user.json()['institution']):
            return groups.guards_json(), 201
        return {'message': 'this not found'}, 404


class GuardsGroupList(Resource):

    def __init__(self):
        pass

    @jwt_required()
    def get(self):
        return {'guards': [guard.json() for guard in GuardsGroupModel.query.filter_by(institution_id=current_user.json()['institution']).all()]}
