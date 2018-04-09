
class ConflictModel():

    def __init__(self):
        self.id = 0
        self.api_name = ''
        self.old_api_version = ''
        self.new_api_version = ''
        self.path = ''
        self.old_value = ''
        self.new_value = ''


    def toJSON(self):
        return {
                    'id': self.id,
                    'api_name': self.api_name,
                    'old_api_version': self.old_api_version,
                    'new_api_version': self.new_api_version,
                    'path': self.path,
                    'old_value': self.old_value,
                    'new_value': self.new_value,
                }


    @classmethod
    def fromJSON(cls, json):
        print(type(json))
        if type(json) is list:
            return [cls.fromDict(dic) for dic in json]

        return cls.fromDict(json)


    @classmethod
    def fromDict(cls, dic):
        cls = ConflictModel()
        cls.api_name = dic['api_name']
        cls.old_api_version = dic['old_api_version']
        cls.new_api_version = dic['new_api_version']
        cls.path = dic['path']
        cls.old_value = dic['old_value']
        cls.new_value = dic['new_value']
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
