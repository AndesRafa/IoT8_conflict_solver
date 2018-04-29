from flask import request, make_response
from flask_restful import Resource

from kaz_json import json
from kaz_sql.services.database import DBManager, Database

from models.taxonomy import Taxonomy as TaxonomyRep


class Taxonomy(Resource):

    def get(self):
        db = DBManager().getDatabase()
        taxonomies = db.selectAll(TaxonomyRep) 
        print(json.toJSON(taxonomies))
        resp = make_response(json.toJSON(taxonomies))
        resp.headers['content-type'] = 'application/json'
        return resp

