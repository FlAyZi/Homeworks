"""6. Write a Python function to get a string made of its first three characters of a specified string. If
the length of the string is less than 3 then return the original string.
Example:
Sample ='ipy'
Expected ipy
______________
Sample ='python'
Expected pyt """

def str_6(str_000):
    if len(str_000) <= 3:
        return str_000
    else:
        return str_000[:3]

