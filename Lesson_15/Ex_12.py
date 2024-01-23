'''Write a function that returns the nth largest element from a list.'''


def n_element(list_1, n):
    sort_list = sorted(list_1)
    return sort_list[-n]
