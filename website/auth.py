from flask import Blueprint, redirect, url_for, render_template, request, session
import string
import random
from captcha.image import ImageCaptcha


# write the image on the given file and save it

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # image = ImageCaptcha(width=280, height=90)
    # captcha_text = ''.join(random.choices(string.digits, k=5))
    # data = image.generate(captcha_text)
    # image.write(captcha_text, 'CAPTCHA.png')

    if request.method == 'GET':
        passcode = ''.join(random.choices(string.digits, k=5))
        print('GET received')
        print('capcha code:' + passcode)
        session['passcode'] = passcode
        return render_template('login.html', passcode=passcode)

    if request.method == 'POST':
        print('POST received')
        user_captcha = request.form.get('user_captcha')
        username = request.form.get('username')
        password = request.form.get('password')
        print("username:" + username)
        print("password:" + password)
        print("captcha:" + user_captcha)

        print('old passcode: ' + session['passcode'])
        if user_captcha == session['passcode']:
            capcha = 'Accepted'
        else:
            capcha = 'Failed'
        return render_template('login.html', capcha=capcha)


@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/sign-up')
def sign_up():
    return render_template('signup.html')


