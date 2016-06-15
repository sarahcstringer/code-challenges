from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import or_, func, desc, update
from datetime import datetime, timedelta

db = SQLAlchemy()

###########################
# Model definitions

class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(25), nullable=False )
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    home_lat = db.Column(db.String(40), nullable=True)
    home_long = db.Column(db.String(40), nullable=True)
    home_address = db.Column(db.String(250), nullable=True)
    home_id = db.Column(db.String(100), nullable=True)
    date_created = db.Column(db.DateTime, nullable=False)

    def __repr__(self):

        return "<User user_id={}, username={}".format(self.user_id, 
                                                        self.username)
def connect_to_db(app, db_uri='postgresql:///sqlmanagers'):

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."