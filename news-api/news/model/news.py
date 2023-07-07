import datetime as dt

from marshmallow import Schema, fields

class News(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content
        # self.created_at = dt.datetime.now()
    
    def __repr__(self):
        return '<News(name={self.content!r})>'.format(self=self)
    
class NewsSchema(Schema):
    title = fields.Str()
    content = fields.Str()
