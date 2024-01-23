"""4. Write a Python program to change a given string to a new string where the first and last chars
have been exchanged.
Example:
Sample: ‘abcdefgh’
Expected: ‘hbcdefga’ """

def str_4(str_000):
    return str_000[-1] + str_000[1:-1] + str_000[0]

