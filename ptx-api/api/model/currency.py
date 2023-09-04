from marshmallow import Schema, fields

class Currency(object):
    def __init__ (self, rate, date):
        self.rate = rate
        self.date = date

class CurrencySchema(Schema):
    rate: fields.Number()
    date: fields.Str()