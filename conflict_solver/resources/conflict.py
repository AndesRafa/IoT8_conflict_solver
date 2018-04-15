from flask import request, make_response
from flask_restful import Resource

from kaz_json import json

from models.conflict import Conflict as ConflictModel
from services.database import selectAll, selectOne

class Conflict(Resource):
        

    def get(self):
        data = selectAll(ConflictModel)
        resp = make_response(json.toJSON(data))
        resp.headers['content-type'] = 'application/json'
        return resp


    #def post(self):
    #    conflictJSON = request.get_json(force=True)
    #    conflictObj = conflict.ConflictModel.fromJSON(conflictJSON) 
    #    db = DBManager().getDatabase()
    #    query = db.execute(conflict.insert(conflictObj))
    #    return 
