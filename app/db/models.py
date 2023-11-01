from app.conf import settings
from bson.objectid import ObjectId
from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    EmailField,
    ListField,
    DateTimeField,
    BooleanField,
    DictField,
    EmbeddedDocumentField,
    ObjectIdField
)


class Notification(EmbeddedDocument):
    id = ObjectIdField(required=True, default=ObjectId)
    timestamp = DateTimeField()
    is_new = BooleanField()
    user_id = StringField()
    key = StringField()
    target_id = StringField()
    data = DictField()


class User(Document):
    username = StringField()
    email = EmailField()
    notif_list = ListField(EmbeddedDocumentField(Notification), max_length=30)
