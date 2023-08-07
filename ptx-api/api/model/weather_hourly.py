from marshmallow import Schema, fields

class WeatherHourly(object):
    def __init__(self, date, icon, phrase, precipitation, is_day_light, temperature, link):
        self.date = date
        self.icon = icon
        self.phrase = phrase
        self.precipitation = precipitation
        self.is_day_light = is_day_light
        self.temperature = temperature
        self.link = link

class WeatherHourlySchema(Schema):
    DateTime = fields.Str()
    WeatherIcon = fields.Int()
    IconPhrase = fields.Str()
    PrecipitationProbability = fields.Number()
    IsDayLight = fields.Boolean()
    Temperature = fields.Dict()
    Link = fields.Str()
