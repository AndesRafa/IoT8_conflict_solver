from flask import request, make_response
from flask_restful import Resource

from kaz_json import json
from kaz_sql.services.database import DBManager, Database

from models.differentials import ApiDifferential, ElementDifferential,\
        Differential as DiffRep


class Differential(Resource):

    #def get(self):


    def post(self):
        itemJSON = request.get_json(force=True)
        itemObj = json.fromJSON(ApiDifferential, itemJSON) 
        diffs = []
        for diff in itemObj.element_differentials:
            element_differential = json.fromJSON(ElementDifferential, diff)
            diffRep = DiffRep.fromDifferentials(itemObj,
                    element_differential)
            diffs.append(diffRep)

        db = DBManager().getDatabase()
        query = db.insert(DiffRep, diffs)
        return 

