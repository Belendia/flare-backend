from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView

from .models import Language, Subscriber

from . import appbuilder, db

class SubscriberModelView(ModelView):
    datamodel = SQLAInterface(Subscriber)

    add_columns = ['telephone', 'language']
    edit_columns = ['telephone', 'language']
    list_columns = ['telephone','language']


    def __repr__(self):
        return self.telephone

appbuilder.add_view(
    SubscriberModelView,
    "Subscribers",
    icon = "fa-users",
    category = "Settings",
    category_icon = "fa-cog"
)

class LanguageModelView(ModelView):
    datamodel = SQLAInterface(Language)

    add_columns = ['name', 'code']
    edit_columns = ['name', 'code']
    list_columns = ['name','code']
    show_columns = ['code','name','created_by', 'created_on', 'changed_by','changed_on']
    related_views = [SubscriberModelView]


appbuilder.add_view(
    LanguageModelView,
    "Language",
    icon = "fa-globe",
    category = "Settings",
    category_icon = "fa-cog"
)

"""
    Application wide 404 error handler
"""

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
