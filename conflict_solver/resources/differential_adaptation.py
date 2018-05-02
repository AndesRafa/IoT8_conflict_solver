from flask import request, make_response
from flask_restful import Resource

from kaz_sql.services.database import DBManager
from kaz_json import json

from models.differential_adaptation import \
        DifferentialAdaptation as DifferentialAdaptationRep


class DifferentialAdaptation(Resource):

    def get(self): 
        db = DBManager().getDatabase()
        das = db.selectAll(DifferentialAdaptationRep)
        #das = assembleDifferentialAdaptations()
        resp = make_response(json.toJSON(das))
        resp.headers['content-type'] = 'application/json'

        return resp
