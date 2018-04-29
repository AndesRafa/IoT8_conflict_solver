from flask import request, make_response
from flask_restful import Resource

from kaz_json import json
from kaz_sql.services.database import DBManager, Database

from models.adaptation_node import AdaptationNode as AdaptationNodeModel


class AdaptationNode(Resource):

    def get(self):
        db = DBManager().getDatabase()
        nodes = db.selectAll(AdaptationNodeModel)
        resp = make_response(json.toJSON(nodes))
        resp.headers['content-type'] = 'application/json'
        return resp

