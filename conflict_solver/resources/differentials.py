from flask import request, make_response
from flask_restful import Resource

from kaz_json import json
from kaz_sql.services.database import DBManager, Database

from models.differentials import ApiDifferential, ElementDifferential,\
        Differential as DiffRep
from models.adaptation_node import AdaptationNode

from services.api_element import apiElementTypeFromElementPath,\
        apiResourceFromElementPath, differentialTimingFromElementPath
from services.differential_adaptation import adaptDifferentials


class Differential(Resource):

    def get(self):
        db = DBManager().getDatabase()
        diffs = db.selectAll(DiffRep)
        resp = make_response(json.toJSON(diffs))
        resp.headers['content-type'] = 'application/json'
        return resp

    def post(self):
        itemJSON = request.get_json(force=True)
        itemObj = json.fromJSON(ApiDifferential, itemJSON) 
        diffs = []
        for diff in itemObj.element_differentials:
            element_differential = json.fromJSON(ElementDifferential, diff)
            diffRep = DiffRep.fromDifferentials(itemObj,
                    element_differential)
            diffRep.DifferentialTimingID = \
                    differentialTimingFromElementPath(diffRep.ElementPath).value
            diffRep.ApiResource = \
                    apiResourceFromElementPath(diffRep.ElementPath)
            diffRep.ApiElementTypeID = \
                    apiElementTypeFromElementPath(diffRep.ElementPath).value

            diffs.append(diffRep)

        db = DBManager().getDatabase()
        query = db.insert(DiffRep, diffs)
        adaptDifferentials()
        return

