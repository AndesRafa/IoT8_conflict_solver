import os

from kaz_restful.server import Server
from kaz_sql.services.database import DBManager

from resources.conflict import Conflict
from resources.adaptation import Adaptation, AdaptationList

def main():
    print('*************************************')
    print('          CONFLICT SOLVER')
    print('*************************************')

    print('Reading settings...')
    port = int(os.getenv(key='CONFLICT_SOLVER_PORT') or "5000")
    databaseCon = str(os.getenv(key='CONFLICT_SOLVER_DATABASE'))

    print('Initiating modules')
    DBManager().setConnection(databaseCon)

    print('Initiating server')
    server = Server(port=port)

    print('Loading resources')
    server.addResources([
            (Conflict, '/conflict'),
            (AdaptationList, '/adaptations'),
            (Adaptation, '/adaptation'),
            #'/adaptation/apiname/<string:apiname>/resource/<string:apiresource>'),
        ])

    print('Starting server')
    server.serve()


if __name__ == '__main__':
    main()
