def capital_str(x):
    if not isinstance(x, str):
        raise TypeError('pls provide a string input')
    return x.capitalize()