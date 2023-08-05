from marshmallow import Schema, fields

class WeatherDaily(object):
    def __init__(self, date, temperature, day, night, link):
        self.date = date
        self.temperature = temperature
        self.day = day
        self.night = night
        self.link = link

class WeatherDailySchema(Schema):
    Date = fields.Str()
    Temperature = fields.Dict()
    Day = fields.Dict()
    Night = fields.Dict()
    Link = fields.Str()