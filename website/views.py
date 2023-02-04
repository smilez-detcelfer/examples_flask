from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

#render template and passing list from backend
@views.route('/passing_list')
def passing_list():
    backend_list = [12, 11233456, 'firststring', 'secnd', 'sr']
    return render_template('render_list.html', list = backend_list)

