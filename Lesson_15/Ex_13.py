'''Write a function that checks if two sets are disjoint (have no common elements).'''


def two_sets(set_1, set_2):
    result = list(filter(lambda x: x in set_1, set_2))
    if result == []:
        return True
    return False
