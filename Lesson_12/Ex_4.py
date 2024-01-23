''' Write a Python program to find intersection of two given arrays using
Lambda.'''

list_1 = [1,2,3]
list_2 = [3,4,5]
print(list(filter(lambda num: num in list_2, list_1)))
