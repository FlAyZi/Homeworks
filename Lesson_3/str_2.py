"""2. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string
is less than 3, leave it unchanged.
Example:
Sample String : 'abc'
Expected Result : 'abcing'
_______________________
Sample String : 'string'
Expected Result : 'stringly' """

def str_2(str_001):
    if len(str_001) <= 3:
        return str_001
    elif str_001[::-1] == 'gni':
        return str_001 + 'ly'
    else:
        return str_001 + 'ing'

