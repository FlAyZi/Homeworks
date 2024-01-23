'''Given two dictionaries, merge them into a new dictionary, excluding any keys
that start with an underscore.'''


def not_start_an_underscore(dct_1, dct_2):
    new_dct = dct_1 | dct_2
    return {k: v for k, v in new_dct.items() if k[0] != '_'}
