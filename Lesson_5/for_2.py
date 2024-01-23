"""2.Largest: Write a Python program to get the largest
number from a list."""

list_1 = [-1, -2, -3, -4]
max_1 = list_1[0] - 1
for i in list_1:
    if i > max_1:
        max_1 = i
print(max_1)
