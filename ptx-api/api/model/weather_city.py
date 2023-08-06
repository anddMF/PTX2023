from marshmallow import fields, Schema

class WeatherCity(object):
    def __init__(self, key, localizedName, country, administrativeArea):
        self.key = key
        self.localizedName = localizedName
        self.country = country
        self.administrativeArea = administrativeArea

class WeatherCitySchema(Schema):
    Key = fields.Str()
    LocalizedName = fields.Str()
    Country = fields.Dict()
    AdministrativeArea = fields.Dict()