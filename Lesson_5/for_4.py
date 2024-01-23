"""4.Second smallest: Write a Python program to find the second
smallest number in a list"""

list_1 = [5, 7, 3, 4, 11]
a = list_1[0] + 1
b = list_1[0] + 1
for i in list_1:
    if i < a:
        b = a
        a = i
    elif i < b and a != i:
        b = i

print(b)
