from flask import render_template
# From the app package we are importing the app flask object
from app import app
from app.forms import LoginForm

# The syntax here is that the '@app.route' decoration creates an association between the url that's passed in as the parameter with the following function
@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Jim'}
  posts = [
      {
          'author': {'username': 'John'},
          'body': 'Beautiful day in Portland!'
      },
      {
          'author': {'username': 'Susan'},
          'body': 'The Avengers movie was so cool!'
      }
  ]
  return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
  form = LoginForm()
  render_template('login.html', title='Login', form=form)