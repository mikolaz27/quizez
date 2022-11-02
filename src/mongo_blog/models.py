import datetime

from mongoengine import (Document, EmbeddedDocument, StringField,
                         DateTimeField, ListField, EmbeddedDocumentField)


class Blog(EmbeddedDocument):
    name = StringField(max_length=255)
    text = StringField()


class Entry(Document):
    blogs = ListField(EmbeddedDocumentField(Blog))
    timestamp = DateTimeField(default=datetime.datetime.now())
    headline = StringField(max_length=255)
