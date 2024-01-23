"""3. Write a Python program to remove the n-th index character from a nonempty string.
Example:
Sample string: ‘abcdefgh’
n - 3
Expected result: abcefgh """

def str_3(str_000, n):
    if n < 0 or n >= len(str_000):
        return str_000
    else:
        return str_000[:n] + str_000[n+1:]

