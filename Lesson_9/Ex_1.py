# Print the even numbers from 0 to 20 using a for loop and the range function

f = []
for i in range(0, 21):
    if i % 2 == 0:
        f.append(i)
print(f)
