import datetime
from mongoengine import Document, StringField, DateTimeField, EmailField, BinaryField, EmbeddedDocumentField

class User(Document):
    email = EmailField(required=True)
    password = BinaryField(required=True)
    name = StringField(required=True)
    api_token = StringField(required=True)
    date_created = DateTimeField(default=datetime.datetime.utcnow)
    date_accessed = DateTimeField(default=datetime.datetime.utcnow)
    twitter_access_token = StringField(required=False)
    twitter_access_token_secret = StringField(required=False)
