"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb web_blog')

os.system('createdb web_blog')

model.connect_to_db(server.app)

model.db.create_all()


# Create YourModelNameLowerCasedHere table's initial data.

with open('data/blog_post.json') as f:

    blog_data = json.loads(f.read())

blog_in_db = []

for blog in blog_data:
    channel_name, posted_by, date_posted, title, content, views, hearts, date_updated = (
                                   blog['channel_name'],
                                   blog['posted_by'],
                                   blog['date_posted'],
                                   blog['title'],
                                   blog['content'],
                                   blog['views'],
                                   blog['hearts'],
                                   blog['date_updated'])

    db_blog = crud.create_blog(
                                 channel_name,
                                 posted_by,
                                 date_posted,
                                 title,
                                 content,
                                 views,
                                 hearts,
                                 date_updated)

    blog_in_db.append(db_blog)
