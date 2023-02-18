from . import db
from datetime import datetime
from flask_login import UserMixin
import secrets

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Integer, default=0)
    def __init__(self, username):
        self.username = username

    def __repr__(self) -> str:
        return 'User >> {self.username}'