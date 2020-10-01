import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_user import UserMixin

from database.db import db


class User(db.Document, UserMixin):
    email = db.EmailField(required=True, max_length=100, unique=True)
    first_name = db.StringField(required=True, max_length=100)
    last_name = db.StringField(required=True, max_length=100)
    password = db.StringField(required=True, min_lenght=6)
    phone_number = db.IntField(required=True, max_length=9)
    created_at = db.DateTimeField(default=datetime.datetime.now())
    cash_bank = db.IntField(default=0)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)