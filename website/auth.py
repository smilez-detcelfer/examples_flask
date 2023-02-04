from flask import Blueprint, redirect, url_for, render_template, request, session, flash
import string
import random
from captcha.image import ImageCaptcha
from PIL import Image
import base64
import io

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        #captcha generation and saving in session
        captcha_text = ''.join(random.choices(string.digits, k=5))
        session['captcha_text'] = captcha_text
        #image generation
        image = ImageCaptcha(width=280, height=90)
        image.generate(captcha_text)
        image.write(captcha_text, 'CAPTCHA.png')
        # image file to raw data
        im = Image.open('CAPTCHA.png')
        data = io.BytesIO()
        im.save(data, "PNG")
        encoded_img_data = base64.b64encode(data.getvalue())
        ###
        return render_template('login.html', img_data=encoded_img_data.decode('utf-8'))
    if request.method == 'POST':
        print('POST received')
        user_captcha = request.form.get('user_captcha')
        username = request.form.get('username')
        password = request.form.get('password')
        captcha_result = 'Accepted' if user_captcha == session['captcha_text'] else 'Failed'
        return redirect(url_for("user"))

@auth.route('/logout')
def logout():
    flash("you're logged out", "info")
    return redirect(url_for('auth.login'))


@auth.route('/sign-up')
def sign_up():
    return render_template('signup.html')


@auth.route("user")
def user():
        return render_template('auth.user.html')