from flask import render_template, flash, redirect, url_for
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

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for for user {}, remember_me={}'.format(
      form.username.data, form.remember_me.data))
    return redirect(url_for('index'))
  return render_template('login.html', title='Login', form=form)

@app.route('/unicorns')
def unicorns():
  return render_template('unicorns.html', title='Unicorns')