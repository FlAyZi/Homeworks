'''Write a function that checks if a given string is a valid email address.'''


def email(str_1):
    str_2 = str_1.split('@')
    str_3 = str_2[1].split('.')
    if len(str_3) == 2:
        return True
    return False
