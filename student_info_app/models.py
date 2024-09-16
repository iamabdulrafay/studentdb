from mongoengine import Document, fields

class StudentModel(Document):
    name = fields.StringField(required=True)
    age = fields.IntField(required=True)
    father_name=fields.StringField(required=True)
    class_level=fields.StringField(required=True)
    
