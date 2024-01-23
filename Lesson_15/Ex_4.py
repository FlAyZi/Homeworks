'''Write a function that takes two lists and returns a new list containing only the common
elements. (without using set)'''


def common_list(list_1, list_2):
    result = list(filter(lambda x: x in list_1, list_2))
    return result
