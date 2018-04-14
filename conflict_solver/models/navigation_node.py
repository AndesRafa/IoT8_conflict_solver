from jinja2 import Template
import services
#from conflict_solver.services.database import DBManager, Database

from conflict import selectByID, ConflictModel

template = Template('Hello {{ name }}')
greeting = template.render( name='Jose' )

print(greeting)

class Sample():

    def __init__(self, id):
        self.id = id

nodeNavigationString = '\
    {\
        "id":"{{obj.id}}"\
    }\
'
db = DBManager().getDatabase()
query = db.execute(selectByID(1))
print(dir(query.cursor))
#conflict = dir(query.cursor
#sampleTemplate = Template(nodeNavigationString)
#json = sampleTemplate.render( obj=Sample(2) )
#print(json)
