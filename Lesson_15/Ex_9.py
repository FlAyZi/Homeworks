'''Write a function that finds the key with the maximum value in a dictionary.'''


def max_key(dict_0):
    l = []
    result = ()
    for i in dict_0.items():
        l.append(i)
    k = (0, l[1][1] - 1)
    for i in l:
        if k[1] < i[1]:
            k = i
            result = i
    return result[0]
