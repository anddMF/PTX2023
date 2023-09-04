from marshmallow import Schema, fields

class WeatherCurrent(object):
    def __init__(self, date, text, icon, has_precipitation, precipitation_type, precipitation_intensity, is_day_time, temperature, link):
        self.date = date
        self.text = text
        self.icon = icon
        self.has_precipitation = has_precipitation
        self.precipitation_type = precipitation_type
        self.precipitation_intensity = precipitation_intensity
        self.is_day_time = is_day_time
        self.temperature = temperature
        self.link = link

class WeatherCurrentSchema(Schema):
    DateTime = fields.Str()
    WeatherText = fields.Str()
    WeatherIcon = fields.Str()
    HasPrecipitation = fields.Str()
    PrecipitationType = fields.Str()
    PrecipitationIntensity = fields.Str()
    IsDayTime = fields.Str()
    Temperature = fields.Number()
    Link = fields.Str()
