'''Write a python program which concat 2 dicts
'''


def dicts(dict_1, dict_2):
    for k, v in dict_2.items():
        dict_1[k] = v
    return dict_1

