'''Write a function that capitalizes the first letter of each word in a sentence.'''


def first_letter(str_1):
    lst = []
    list_word = str_1.split()
    for i in list_word:
        lst.append(i.capitalize())
    return ' '.join(lst)
