"""Server for web-blogs app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Blog, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_blogs():

    stats=crud.get_blogs()
    
    blog_post_id=[q[0] for q in db.session.query(Blog.blog_post_id).all()]

    channel_name=[q[0] for q in db.session.query(Blog.channel_name).all()]

    posted_by=[q[0] for q in db.session.query(Blog.posted_by).all()]

    date_posted=[q[0] for q in db.session.query(Blog.date_posted).all()]

    title=[q[0] for q in db.session.query(Blog.title).all()]

    content=[q[0] for q in db.session.query(Blog.content).all()]

    views=[q[0] for q in db.session.query(Blog.views).all()]

    hearts=[q[0] for q in db.session.query(Blog.hearts).all()]
      
    date_updated=[q[0] for q in db.session.query(Blog.date_updated).all()]

    return render_template('blog_posts.html', blog_post_id=blog_post_id, channel_name=channel_name, posted_by=posted_by, date_posted=date_posted, title=title, content=content, views=views, hearts=hearts, date_updated=date_updated)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()