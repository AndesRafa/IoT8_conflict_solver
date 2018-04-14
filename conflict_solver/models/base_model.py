from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('conflict_solver', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

class BaseModel():

    def toJSON(self):
        template = env.get_template('to_json_template.tmpl')
        json = template.render(items=vars(self).iteritems())
        return json


    def selectAll(self):
        template = env.get_template('sql_select_all.tmpl')
        items = vars(self).iterkeys()
        table = self.getEntityName()
        query = template.render(columns=items, table=table)
        return query


    def selectByID(self):
        template = env.get_template('sql_select_by_id.tmpl')
        items = vars(self).iterkeys()
        table = self.getEntityName()
        selectors = dict({ "id":self.id }).iteritems()
        query = template.render(columns=items, table=table, selectors=selectors)
        return query


    def insertOne(self):
        template = env.get_template('sql_insert.tmpl')
        columns = vars(self).iterkeys()
        values = vars(self).itervalues()
        table = self.getEntityName()
        query = template.render( table=table, columns=columns, values=values)
        return query


    def getEntityName(self):
        name = self.__class__.__name__
        if name.upper().endswith('MODEL'):
            name = name[:-5]

        return name
