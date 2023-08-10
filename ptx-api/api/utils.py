import re


def check_date_format(date):
    pattern = "^\d{4}-\d{2}-\d{2}$"
    response = re.match(pattern, date)
    return response
