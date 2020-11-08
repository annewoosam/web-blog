"""CRUD operations."""

from model import db, Blog, connect_to_db

import datetime


def create_blog(channel_name, posted_by, date_posted, title, content, views, hearts, date_updated):
   

    blog = Blog(channel_name=channel_name,
                  posted_by=posted_by,
                  date_posted=date_posted,
                  title=title,
                  content=content,
                  views=views,
                  hearts=hearts,
                  date_updated=date_updated)

    db.session.add(blog)

    db.session.commit()

    return blog

def get_blogs():
    """Return all rows of blog monthly data."""

    return Blog.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
