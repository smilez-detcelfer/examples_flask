from flask import Blueprint, redirect, url_for, render_template, request, session
import string
import random

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        passcode = ''.join(random.choices(string.digits, k=5))
        print('GET received')
        print('capcha code:' + passcode)
        session['passcode'] = passcode
        return render_template('login.html', passcode=passcode)

    if request.method == 'POST':
        print('POST received')
        user_input = request.form.get('user_input')
        print("user input:" + user_input)
        print('old passcode: ' + session['passcode'])
        if user_input == session['passcode']:
            capcha = 'Пройдена'
        else:
            capcha = 'Провалена'
        return render_template('login.html', capcha=capcha)


@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/sign-up')
def sign_up():
    return render_template('signup.html')

