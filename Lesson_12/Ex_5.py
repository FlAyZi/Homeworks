''' Write a Python program to add two given lists using map and
lambda.(map-y kara function-ic heto mekic avel hajordakanutyun
ynduni, orinak erku list)'''


list_1 = [1, 2, 3]
list_2 = [3, 2, 1]
print(list(map(lambda num_1, num_2: num_1 + num_2, list_1, list_2)))
