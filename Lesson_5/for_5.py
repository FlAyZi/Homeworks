"""5.Duplicates: Write a Python program to remove duplicates from a list"""

list_1 = [1, 1, 1, 2, 3]
k = list_1[0] + 1
f = []
for i in list_1:
    if i != k:
        k = i
        f.append(k)
print(f)
