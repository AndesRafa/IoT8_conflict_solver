from flask import request, make_response
from flask_restful import Resource

from kaz_json import json

from models.adaptation import Adaptation as AdaptationModel
from services.database import selectAll, selectOne


class Adaptation(Resource):

    def put(self):
        reqJSON = request.get_json()
        apiname = reqJSON['ApiName']
        apiresource = reqJSON['ApiResource']
        data = selectAll(AdaptationModel, [
                ('ApiName', apiname),
                ('ApiResource', apiresource)
            ])
        resp = make_response(json.toJSON(data))
        resp.headers['content-type'] = 'application/json'
        return resp


class AdaptationList(Resource):

    def get(self): 
        data = selectAll(AdaptationModel)
        resp = make_response(json.toJSON(data))
        resp.headers['content-type'] = 'application/json'
        return resp
