from marshmallow import Schema, fields

class WeatherHourly(object):
    def __init__(self, date, icon, phrase, precipitation, is_day_light, temperature, precipitation_type, precipitation_intensity, link):
        self.date = date
        self.icon = icon
        self.phrase = phrase
        self.precipitation = precipitation
        self.is_day_light = is_day_light
        self.temperature = temperature
        self.precipitation_type = precipitation_type
        self.precipitation_intensity = precipitation_intensity
        self.link = link

class WeatherHourlySchema(Schema):
    DateTime = fields.Str()
    WeatherIcon = fields.Int()
    IconPhrase = fields.Str()
    PrecipitationProbability = fields.Number()
    IsDaylight = fields.Boolean()
    Temperature = fields.Dict()
    PrecipitationType = fields.Str()
    PrecipitationIntensity = fields.Str()
    Link = fields.Str()
