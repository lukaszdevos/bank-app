from database.db import db


class Test(db.Document):
    username = db.StringField()