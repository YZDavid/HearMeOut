from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David'}
    conversions = [
        {'input': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
         'output': 'Lorem ipsum dolor sit amet'},
        {'input': 'Non quam lacus suspendisse faucibus interdum. Lectus nulla at volutpat diam ut venenatis tellus in. Consequat interdum varius sit amet mattis vulputate. Vulputate eu scelerisque felis imperdiet proin fermentum leo. Blandit volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque.',
         'output': 'Non quam lacus suspendisse faucibus interdum.'}
    ]
    return render_template('index.html', user=user, title="Home", conversions=conversions)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)