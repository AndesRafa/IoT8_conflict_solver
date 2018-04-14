from flask import request
from flask_jsonpify import jsonify
from flask_restful import Resource

from models import conflict_model as conflict
from services.database_service import DBManager, Database

class ConflictResource(Resource):
        

    def get(self):
        db = DBManager().getDatabase()
        query = db.execute(conflict.selectAll())
        conflicts = conflict.conflictsFromCursor(query.cursor.fetchall())
        return jsonify([con.toJSON() for con in conflicts])


    def post(self):
        conflictJSON = request.get_json(force=True)
        conflictObj = conflict.ConflictModel.fromJSON(conflictJSON) 
        db = DBManager().getDatabase()
        query = db.execute(conflict.insert(conflictObj))
        return 
