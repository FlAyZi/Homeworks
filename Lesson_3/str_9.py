"""9. Append new string in the middle of a given (even number of characters) string
Example:
Sample = ‘python’
new_string = ‘new’
Expected ‘pytnewhon """

def str9(str_000, new_str):
    if len(str_000) % 2 == 0:
        midlle_str = len(str_000) // 2
        result = str_000[:midlle_str] + new_str + str_000[midlle_str:]
        return result
    else:
        return str_000
