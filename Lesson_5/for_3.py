"""3.Smallest: Write a Python program to get the smallest number from a list"""

list_1 = [1234, 99, 10, -123, 23]
min_1 = list_1[0] + 1
for i in list_1:
    if i < min_1:
        min_1 = i
print(min_1)
