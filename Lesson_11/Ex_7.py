'''Write a python function which create dict from 2
lists with the same length'''


def dict_in_2_list(list_key, list_value):
    result = {}
    for key in list_key:
        for value in list_value:
            result[key] = value
            list_value.remove(value)
            break
    return result
