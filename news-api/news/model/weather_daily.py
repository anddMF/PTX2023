from marshmallow import Schema, fields

class WeatherDaily(object):
    def __init__(self, date, temperature, day, night, link):
        self.date = date
        self.temperature = temperature
        self.day = day
        self.night = night
        self.link = link

class WeatherDailySchema(Schema):
    date = fields.Str()
    temperature = fields.Dict()
    day = fields.Dict()
    night = fields.Dict()
    link = fields.Str()