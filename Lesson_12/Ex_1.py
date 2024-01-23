'''Write a Python program to square and cube every number in a given list of
integers using Lambda. '''

list_1 = [1, 2, 3, 4, 5]
print(list(map(lambda num: num**2, list_1)))
print(list(map(lambda num: num**3, list_1)))
