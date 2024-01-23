'''Given a string, create a dictionary where keys are characters and values are their
frequencies in the string.'''


def dct(string):
    return {k: string.count(k) for k in string}
