from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Travis'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Umatilla!',
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie sucked!',
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
