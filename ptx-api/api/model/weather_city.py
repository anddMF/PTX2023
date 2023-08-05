from marshmallow import fields, Schema

class WeatherCity(object):
    def __init__(self, key, localizedName, country, administrativeArea):
        self.key = key
        self.localizedName = localizedName
        self.country = country
        self.administrativeArea = administrativeArea

class WeatherCitySchema(Schema):
    key = fields.Str()
    localizedName = fields.Str()
    country = fields.Dict()
    administrativeArea = fields.Dict()