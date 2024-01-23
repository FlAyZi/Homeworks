'''You are given three lists, list1, list2, and list3. Your task is to implement a
programm that takes these lists and prints the following:
The set of elements that are common to all three lists.
The set of elements that are present in at least two of the three lists, but not in all
three.
The set of elements that are unique to each list (present in only one list) '''

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
c = [2, 3, 4, 5, 6, 9]
s = set(a) & set(b) & set(c)
v = (set(a) & set(b)) | (set(a) & set(c)) | (set(b) & set(c))
f_1 = set(a) - (set(b) | set(c))
f_2 = set(b) - (set(a) | set(c))
f_3 = set(c) - (set(a) | set(b))

#The set of elements that are common to all three lists.
print(s)

#The set of elements that are present in at least two of the three lists, but not in all three.
print(v)

#The set of elements that are unique to each list (present in only one list)
print(f_1)
print(f_2)
print(f_3)