''' 2.Count:
Count all letters, digits, and special symbols from a given string '''

str_1 = input()
str_2 = str_1.replace(' ', '')
a = 0
b = 0
c = 0
for i in str_2:
    if i.isdigit():
        a += 1
    elif i.isalpha():
        b += 1
    else:
        c += 1

print(f'Chars = {b}')
print(f'Digits = {a}')
print(f'Symbol = {c}')