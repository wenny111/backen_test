from flask import Flask
from controller.router import router
from flask import render_template

from orm.OrmEntity import db, Usertable


import logging
import sys
sys.path.append('.')

app = Flask(__name__)
app.register_blueprint(router)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Aa_123456!@localhost/test'
with app.app_context():
	db.init_app(app)
	db.create_all()


if __name__ == '__main__': 
	app.run(host="0.0.0.0", port='8888')
