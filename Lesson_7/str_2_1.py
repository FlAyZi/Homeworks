''' 1.Arrange:
Arrange string characters such that lowercase letters should come first '''

str_1 = input()
k = ''
f = ''
str_2 = str_1.replace(' ', '')
for i in str_2:
    if i == i.lower():
        k += i
    else:
        f += i
print(k + f)


