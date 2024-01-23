'''Write a Python program that calculates the sum of all even numbers between 1 and 100
using a while loop.'''
i = 0
c = 0
while i != 101:
    if i % 2 == 0:
        c += i
    i += 1
print(c)