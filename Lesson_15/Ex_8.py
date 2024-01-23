'''Create a dictionary of book titles and their authors. Write a function to search for a book
by its title and return the author's name'''


def authors_books(dict_0, book):
    result = ''
    for i in dict_0.items():
        if i[0] == book:
            result = i[1]
    return result

