import os

from conflict_solver.models import conflict_model as conflict


def solveConflict():

    print('Reading settings...')
    port = int(os.getenv(key='CONFLICT_SOLVER_PORT') or "5000")
    databaseCon = str(os.getenv(key='CONFLICT_SOLVER_DATABASE'))

    print('Initiating modules')
    DBManager().setConnection(databaseCon)

    db = DBManager().getDatabase()
    query = db.execute(conflict.selectAll())
    conflicts = conflict.conflictsFromCursor(query.cursor.fetchall())
    for con in conflicts:
        print(con)
