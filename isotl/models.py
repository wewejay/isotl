from peewee import *

db = SqliteDatabase('isotl.db')


class Image(Model):
    rel_path = CharField()
    name = CharField()
    size = IntegerField()
    md5 = CharField()

    class Meta:
        database = db


class File(Model):
    rel_path = CharField()
    name = CharField()
    size = IntegerField()
    md5 = CharField()
    image = ForeignKeyField(Image)

    class Meta:
        database = db