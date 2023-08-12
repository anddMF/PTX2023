import datetime as dt

from marshmallow import Schema, fields


class News(object):
    def __init__(self, title, author, url, description, published_at, image, category, country, language, source):
        self.title = title
        self.description = description
        self.url = url
        self.author = author
        self.published_at = published_at
        self.image = image
        self.source = source
        self.category = category
        self.country = country
        self.language = language

    def __repr__(self):
        return '<News(name={self.content!r})>'.format(self=self)


class NewsSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    url = fields.Str()
    author = fields.Str()
    published_at = fields.Str()
    image = fields.Str()
    source = fields.Str()
    category = fields.Str()
    country = fields.Str()
    language = fields.Str()
