'''Write a program that takes a list of numbers as input and
counts the number of even numbers in the list. Use a for
loop, an if statement, and the modulus operator (%) to
determine if a number is even or odd.'''


lst = [1, 2, 3, 4, 5]
result = []
for i in lst:
    if i % 2 == 0:
        result.append(i)

