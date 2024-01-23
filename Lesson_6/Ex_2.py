'''Write a program that takes a string as input and counts the
number of vowels (a, e, i, o, u) in the string. Use a for
loop, an if statement, and the in operator to check if a
character is a vowel.'''


str_1 = 'arenaa'
result = 0
for i in str_1:
    if i in 'AaEeIiOoUu':
        result += 1
