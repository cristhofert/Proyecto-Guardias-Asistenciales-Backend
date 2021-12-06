def is_empty(data):
    for key in data:
        if type(data[key]) == str:
            if data[key] == '':
                return True
    return False