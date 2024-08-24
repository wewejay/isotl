from peewee import *

db = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class Image(Model):
    rel_path = CharField()
    name = CharField()
    size = IntegerField()
    md5 = CharField()


class File(Model):
    rel_path = CharField()
    name = CharField()
    size = IntegerField()
    image = ForeignKeyField(Image)
