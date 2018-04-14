from base_model import BaseModel

class ResolutionModel(BaseModel):

    def __init__(self):
        self.id = 0
        self.conflictID = 0
        self.taxonomyID = 0
        self.hostName = ''
        self.path = ''


    @classmethod
    def fromJSON(cls, json):
        cls = ConflictModel()
        cls.apiName = json['api_name']
        cls.apiVersion = json['api_version']
        cls.path = json['path']
        cls.value = json['value']
        return cls


    @classmethod
    def fromCursorItem(cls, cur):
        cls = ConflictModel()
        cls.id = cur[0]
        cls.apiName = cur[1]
        cls.apiVersion = cur[2]
        cls.path = cur[3]
        cls.value = cur[4]
        return cls


def selectByID(id):
    return 'SELECT ID, ApiName, ApiVersion, Path, Value FROM Conflict' + \
            'WHERE ID = {}'.format(id);


def selectAll():
    return 'SELECT ID, ApiName, ApiVersion, Path, Value FROM Conflict;'


def insert(item):
    return 'INSERT INTO Conflict(ApiName, ApiVersion, Path, Value)' + \
            ' VALUES (\'{}\',\'{}\',\'{}\',\'{}\');' \
            .format(item.apiName, item.apiVersion, item.path, item.value)


def conflictsFromCursor(items):
    results = []
    for item in items:
        results.append(ConflictModel.fromCursorItem(item))

    return results
