'''Given a string, create a dictionary where keys are characters, and values are
their ASCII values.'''


def ASCII_values(string):
    return {i: ord(i) for i in string}
