


a = {'hours': 13, 'minutes': 23}
b = {'hours': 23, 'minutes': 42}

def add_times(a, b):
    m = a['minutes'] + b['minutes']
    h = (0 if m < 60 else 1) + a['hours'] + b['hours']
    return {'hours': h, 'minutes': m % 60}


print(add_times(a, b))