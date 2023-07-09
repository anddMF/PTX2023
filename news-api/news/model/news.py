import datetime as dt

from marshmallow import Schema, fields


class News(object):
    def __init__(self, title, content, keywords, creator, video_url, description, pubDate, image_url, source_id, category, country, language):
        self.title = title
        self.content = content
        self.keywords = keywords
        self.creator = creator
        self.video_url = video_url
        self.description = description
        self.pubDate = pubDate
        self.image_url = image_url
        self.source_id = source_id
        self.category = category
        self.country = country
        self.language = language

    def __repr__(self):
        return '<News(name={self.content!r})>'.format(self=self)


class NewsSchema(Schema):
    title = fields.Str()
    content = fields.Str()
    keywords = fields.List(fields.Str())
    creator = fields.List(fields.Str())
    video_url = fields.Str()
    description = fields.Str()
    pubDate = fields.Str()
    image_url = fields.Str()
    source_id = fields.Str()
    category = fields.List(fields.Str())
    country = fields.List(fields.Str())
    language = fields.Str()
