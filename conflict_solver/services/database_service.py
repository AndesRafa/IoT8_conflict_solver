from sqlalchemy import create_engine

class Database():

    def __init__(self, databaseCon):
        self.dbConnect = create_engine(databaseCon)


    def execute(self, query):
        con = self.dbConnect.connect()
        return con.execute(query)


    def __del__(self):
        print('\t\tTerminating database component...')


class DBManagerSingleton(type):

    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(DBManagerSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class DBManager():
    __metaclass__ = DBManagerSingleton
    
    def __init__(self):
        self.databaseCon = ''


    def setConnection(self, databaseCon):
        self.databaseCon = databaseCon


    def getDatabase(self):
        print(self.databaseCon)
        return Database(self.databaseCon)

