from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

# test = YourClassNameHereInTitleCaseSingular(channel_name='WinningCheckers', email_date='2020-01-31',number_subscribers = '1', month_end_at='2019-12-31', subscribers='0', views='1', minutes_watched='2', likes='3', comments='4', posts='5', shares='6')

class Blog(db.Model):
    """A class for creator ."""
    
    __tablename__ = 'blogs'

    blog_post_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    channel_name = db.Column(db.String)
    
    posted_by = db.Column(db.String)

    date_posted = db.Column(db.Date)

    title = db.Column(db.String)

    content = db.Column(db.String)

    views = db.Column(db.Integer)

    hearts = db.Column(db.Integer)

    date_updated = db.Column(db.Date)

    def __repr__(self):
        return f'<Blog blog_post_id={self.blog_post_id} channel_name={self.channel_name}>'

def connect_to_db(flask_app, db_uri='postgresql:///web_blog', echo=True):
   
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
   
    flask_app.config['SQLALCHEMY_ECHO'] = echo
   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)