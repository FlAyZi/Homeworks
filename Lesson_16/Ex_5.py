'''Given a list of words, create a dictionary where keys are words, and values are
their lengths, but only for words with lengths greater than 3'''


def len_worlds(lst):
    return {i: len(i) for i in lst if len(i) > 3}
