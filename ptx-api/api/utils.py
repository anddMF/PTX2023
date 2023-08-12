import re


def check_date_format(date):
    pattern = "^\d{4}-\d{2}-\d{2}$"
    response = re.match(pattern, date)
    return response

def add_route_param(values_list, param_name, url):
    if values_list[0] != '':
        url += f'&{param_name}=' + values_list[0]
        del values_list[0]
        for value in values_list:
            url += ',' + value
    
    return url