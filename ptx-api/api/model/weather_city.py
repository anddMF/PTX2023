from marshmallow import fields, Schema

class WeatherCity(object):
    def __init__(self, key, localized_name, country, administrative_area):
        self.key = key
        self.localized_name = localized_name
        self.country = country
        self.administrative_area = administrative_area

class WeatherCitySchema(Schema):
    Key = fields.Str()
    LocalizedName = fields.Str()
    Country = fields.Dict()
    AdministrativeArea = fields.Dict()