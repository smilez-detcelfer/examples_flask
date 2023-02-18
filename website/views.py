from flask import Blueprint, render_template, session
from flask_sqlalchemy import SQLAlchemy
from .models import User
from . import db
import time
#db = SQLAlchemy()


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')

#render template and passing list from backend
@views.route('/passing_list')
def passing_list():
    backend_list = [12, 11233456, 'firststring', 'secnd', 'sr']
    return render_template('render_list.html', list = backend_list)

@views.route('/<usertochange>')
def change_balance(usertochange):
    #user = User.query.filter_by(username = usertochange).first()
    user = db.session.query(User).filter_by(username=usertochange).with_for_update().first()
    print(f"{usertochange}  balance was: {user.balance}")
    user.balance += 5
    time.sleep(20)
    db.session.commit()
    #user = User.query.filter_by(username=usertochange).first()
    print(f'{usertochange} new balance: {user.balance}')
    return f"User {usertochange}!"

@views.route('/test/<usertochange1>')
def change_balance1(usertochange1):
    user = db.session.query(User).filter_by(username=usertochange1).with_for_update().first()
    print(f"{usertochange1}  balance was: {user.balance}")
    user.balance += 5
    db.session.commit()
    #user = User.query.filter_by(username=usertochange).first()
    print(f'{usertochange1} new balance: {user.balance}')
    return f"User {usertochange1}!"