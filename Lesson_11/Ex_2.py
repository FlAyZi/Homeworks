'''Write a Python function to calculate count of each letter in string'''


def count_letters(string):
    result = {}
    for i in string:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

