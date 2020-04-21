from flask_appbuilder import ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.filters import BaseFilter
from sqlalchemy import or_

from . import appbuilder, db
from .models import Language

db.create_all()

class LanguageModelApi(ModelRestApi):
    resource_name = 'languages'
    datamodel = SQLAInterface(Language)
    add_columns = ['name', 'code']
    edit_columns = ['name', 'code']
    list_columns = ['name', 'code']

    def response_422(self, message):
        m = message.split(": ")

        return  self.response(422, message={m[1].replace("language.",""):m[0]})

appbuilder.add_api(LanguageModelApi)


