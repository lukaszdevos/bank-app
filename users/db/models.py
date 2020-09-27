from database.db import db


class UserModel(db.Document):
    username = db.StringField()