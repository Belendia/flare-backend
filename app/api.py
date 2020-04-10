from flask_appbuilder import ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Language

db.create_all()

class LanguageModelApi(ModelRestApi):
    resource_name = 'languages'
    datamodel = SQLAInterface(Language)
    add_columns = ['name', 'code']
    edit_columns = ['name', 'code']
    #list_columns = ['name', 'address']

appbuilder.add_api(LanguageModelApi)


