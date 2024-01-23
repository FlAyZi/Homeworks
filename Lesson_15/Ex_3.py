'''Given a list of numbers, write a function to find the sum of all numbers in the list that
can be divided by 7.'''


def sum_in_list(list_1):
    result = 0
    for i in list_1:
        if i % 7 == 0:
            result += i
    return result
