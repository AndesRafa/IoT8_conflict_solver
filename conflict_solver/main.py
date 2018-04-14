import os

from server import Server
from resources.conflict_resource import ConflictResource
from services.database_service import DBManager

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
    server.addResources([(ConflictResource, '/conflict')])

    print('Starting server')
    server.serve()


if __name__ == '__main__':
    main()
