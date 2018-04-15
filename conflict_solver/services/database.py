from kaz_sql.services.database import DBManager

def selectAll(model, criteria=None):
    db = DBManager().getDatabase()
    return db.selectAll(model, criteria)


def selectOne(model, criteria):
    db = DBManager().getDatabase()
    return db.selectOne(model, criteria)

