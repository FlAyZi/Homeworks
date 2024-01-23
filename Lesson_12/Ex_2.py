'''Write a Python program to find if a given string starts with a given
character using Lambda '''

list_1 = ['q', 'w', '1', '2', 'm']
print(list(map(lambda x: x in set('1qqqwqfdq2'), list_1)))
