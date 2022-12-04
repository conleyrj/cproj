from datetime import datetime, timedelta
import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "cloudcomp"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'
SQLALCHEMY_BINDS = {
  'Households': 'sqlite:///Households.sqlite3',
  'Products': 'sqlite:///Products.sqlite3',
  'Transactions': 'sqlite:///Transactions.sqlite3'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class Users(db.Model):
  id = db.Column("id", db.Integer, primary_key=True)
  username = db.Column(db.String(100))
  password = db.Column(db.String(100))
  email = db.Column(db.String(100))

  def __init__(self, username, password, email):
    self.username = username
    self.password = password
    self.email = email

class Households(db.Model):
  __bind_key__ = 'Households'
  id = db.Column("id", db.Integer, primary_key=True)
  HSHD_NUM = db.Column(db.Integer, primary_key=True)
  L = db.Column(db.Boolean)
  AGE_RANGE = db.Column(db.String(5))
  MARITAL = db.Column(db.String(10))
  INCOME_RANGE = db.Column(db.String(10))
  HOMEOWNER = db.Column(db.String(10))
  HSHD_COMPOSITION = db.Column(db.String(25))
  HH_SIZE = db.Column(db.String(5))
  CHILDREN = db.Column(db.String(5))
  def __init__(self, HSHD_NUM, L, AGE_RANGE, MARITAL,INCOME_RANGE, HOMEOWNER, HSHD_COMPOSITION, HH_SIZE, CHILDREN):
    self.HSHD_NUM = HSHD_NUM
    self.L = L
    self.AGE_RANGE = AGE_RANGE
    self.MARITAL = MARITAL
    self.INCOME_RANGE = INCOME_RANGE
    self.HOMEOWNER = HOMEOWNER
    self.HSHD_COMPOSITION = HSHD_COMPOSITION
    self.HH_SIZE = HH_SIZE
    self.CHILDREN = CHILDREN

class Products(db.Model):
  __bind_key__ = 'Products'
  id = db.Column("id", db.Integer, primary_key=True)
  PRODUCT_NUM = db.Column(db.Integer)
  DEPARTMENT = db.Column(db.String(10))
  COMMODITY = db.Column(db.String(25))
  BRAND_TY = db.Column(db.String(10))
  NATURAL_ORGAINIC_FLAG = db.Column(db.String(1))
  def __init__(self, PRODUCT_NUM, DEPARTMENT, COMMODITY, BRAND_TY,NATURAL_ORGAINIC_FLAG):
    self.PRODUCT_NUM = PRODUCT_NUM
    self.DEPARTMENT = DEPARTMENT
    self.COMMODITY = COMMODITY
    self.BRAND_TY = BRAND_TY
    self.NATURAL_ORGAINIC_FLAG = NATURAL_ORGAINIC_FLAG

class Transactions(db.Model):
  __bind_key__ = 'Transactions'
  id = db.Column("id", db.Integer, primary_key=True)
  BASKET_NUM = db.Column(db.Integer)
  HSHD_NUM = db.Column(db.Integer, primary_key=True)
  PURCHASE = db.Column(db.Date)
  PRODUCT_NUM = db.Column(db.Integer, primary_key=True)
  SPEND = db.Column(db.Numeric)
  UNITS = db.Column(db.Integer)
  STORE_R = db.Column(db.String(10))
  WEEK_NUM = db.Column(db.Integer)
  YEAR = db.Column(db.Integer)
  def __init__(self, BASKET_NUM, HSHD_NUM, PURCHASE, PRODUCT_NUM, SPEND, UNITS, STORE_R, WEEK_NUM, YEAR):
    self.BASKET_NUM = BASKET_NUM
    self.HSHD_NUM = HSHD_NUM
    self.PURCHASE = PURCHASE
    self.PRODUCT_NUM = PRODUCT_NUM
    self.SPEND = SPEND
    self.UNITS = UNITS
    self.STORE_R = STORE_R
    self.WEEK_NUM = WEEK_NUM
    self.YEAR = YEAR


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

@app.route('/data_pull_10', methods=['GET', 'POST'])
def data_pull_10():
  return render_template('data_pull_10.html')


if __name__ == '__main__':
  app.run(debug=True)