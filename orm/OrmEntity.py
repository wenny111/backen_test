from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usertable(db.Model):
    __tablename__ = 'usertable'
    userId = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable=False)
    passwd = db.Column(db.String(80),nullable=False)

    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd

    def __repr__(self):
        return '<User %r>' % self.username

class TodoTable(db.Model):
    __tablename__ = 'todotable'
    todoId = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('usertable.userId'))

    def __init__(self, text, status):
        self.text = text
        self.status = status

    def __repr__(self):
        return '<User %r>' % self.text
    
