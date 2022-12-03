from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
  print('Request for index page received')
  return render_template('index.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
  username = request.form.get('username')

  if username:
      print('Request for hello page received with username=%s' % username)
      return render_template('hello.html', username = username)
  else:
      print('Request for hello page received with no name or blank name -- redirecting')
      return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
  return render_template('dashboard.html')


if __name__ == '__main__':
   app.run(debug=True)