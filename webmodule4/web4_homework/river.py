from mongoengine import Document, StringField, ListField
#để hứng những cái Document từ db

class River(Document):
    name = StringField()
    continent = StringField()
    length = StringField()
