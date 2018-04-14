
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
        cls.path = [x.encode("utf-8") for x in dic['path']]
        cls.old_value = dic['old_value']
        cls.new_value = dic['new_value']
        return cls


    @classmethod
    def fromCursorItem(cls, cur):
        cls = ConflictModel()
        cls.id = cur[0]
        cls.api_name = cur[1]
        cls.old_api_version = cur[2]
        cls.new_api_version = cur[3]
        cls.path = cur[4]
        cls.old_value = cur[5]
        cls.new_value = cur[6]
        return cls


def selectByID(id):
    return 'SELECT ID, ApiName, OldApiVersion, ' +\
            'NewApiVersion, Path, OldValue, NewValue ' +\
            'FROM Conflict' +\
            'WHERE ID = {};'.format(id)


def selectAll():
    return 'SELECT ID, ApiName, OldApiVersion, ' +\
            'NewApiVersion, Path, OldValue, NewValue ' +\
            'FROM Conflict;'


def insert(item):
    if type(item) is list:
        return insertBulk(item)

    return insertSingle(item)


def insertSingle(item):
    return 'INSERT INTO Conflict( '+\
            'ApiName, OldApiVersion, NewApiVersion, ' +\
            'Path, OldValue, NewValue)' + \
            ' VALUES (\
"{}","{}","{}",\
"{}","{}","{}");' \
            .format(
                    item.api_name, 
                    item.old_api_version, 
                    item.new_api_version,
                    item.path,
                    item.old_value,
                    item.new_value)


def insertBulk(items):
    if not len(items) > 0:
        raise Exception('Nothing to bulk insert')

    query = 'INSERT INTO Conflict( \
ApiName, OldApiVersion, NewApiVersion, \
Path, OldValue, NewValue ) \
VALUES '

    for item in items:
        query += \
'("{}","{}","{}",\
"{}","{}","{}"),' \
                .format(
                    item.api_name,
                    item.old_api_version,
                    item.new_api_version,
                    item.path,
                    item.old_value,
                    item.new_value)

    query = query[:len(query) - 1] + ';'
    return query


def conflictsFromCursor(items):
    results = []
    for item in items:
        results.append(ConflictModel.fromCursorItem(item))

    return results

