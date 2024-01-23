"""8.Create a string made of the first, middle and last character of given string with odd number of
symbols
Example:
Sample = ‘Sevak’
Expected ‘Svk’ """

def str_8(str_000):
    if len(str_000) % 2 != 0:
        middle_element = len(str_000) // 2
        str_000 = str_000[0] + str_000[middle_element] + str_000[-1]
        return str_000
    else:
        return str_000

