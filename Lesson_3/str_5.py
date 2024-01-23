"""5. Write a Python function to get a string made of 4 copies of the last two characters of a
specified string (length must be at least 2).
Example:
Sample = ‘Python'
Expected onononon
________________
Sample 'Exercises'
Expected eseseses """

def str_5(str_000):
    if len(str_000) <= 2:
        return str_000
    else:
        return (str_000[-2] + str_000[-1]) * 4

