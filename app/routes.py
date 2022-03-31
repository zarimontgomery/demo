from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')

def index():  # put application's code here
        user = {'username': 'Zari'}
        classes = [{'classInfo': {'code': 'CSC324', 'title': 'DevOps'}, 'instructor': 'Baoqiang Yan'},
                   {'classInfo': {'code': 'CSC254', 'title': 'Object Oriented Programming'},'instructor': 'Evan Noynaert'},
                   {'classInfo': {'code': 'CSC300', 'title': 'Introduction to Cybersecurity'}, 'instructor': 'Yipkei Kwok'}]
        return render_template('index.html', title='Home', user=user, classes=classes)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)



