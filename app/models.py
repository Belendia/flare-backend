import datetime

from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin
from sqlalchemy import Table, Column, DateTime, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, backref


class Language(AuditMixin, Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    code = Column(String(10), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Subscriber(AuditMixin, Model):
    id = Column(Integer, primary_key=True)
    telephone = Column(String(20), unique=True, nullable=False)
    language_id = Column(Integer, ForeignKey('language.id'), nullable=False)
    language = relationship("Language")

    def __repr__(self):
        return self.telephone

class Survey(AuditMixin, Model):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    questions = Column(String, nullable=False)
    translations = Column(String)
    published = Column(Boolean, nullable=False)

    def __repr__(self):
        return self.title

assoc_subscriber_result = Table(
    "result",
    Model.metadata,
    Column("sub_id", Integer, ForeignKey("subscriber.id"), primary_key=True),
    Column("survey_id", Integer, ForeignKey("survey.id"), primary_key=True),
    Column('result', String, nullable=False)
)

# class Result(Model):
#     id = Column(Integer, primary_key=True)
#     result = Column(String)
#     survey_id = Column(Integer, ForeignKey('survey.id'), nullable=False)
#     survey = relationship("Survey")
#     subscriber_id = Column(Integer, ForeignKey('subscriber.id'), nullable=False)
#     subscriber = relationship("Subscriber")

#     def __repr__(self):
#         return self.result

class Message(AuditMixin, Model):
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    translations = Column(String)

    def __repr__(self):
        return self.content

assoc_subscriber_message = Table(
    "message_sent",
    Model.metadata,
    Column("sub_id", Integer, ForeignKey("subscriber.id"), primary_key=True),
    Column("message_id", Integer, ForeignKey("message.id"), primary_key=True),
    Column('sent', Boolean, nullable=False),
    Column('read', Boolean, nullable=True)
)
