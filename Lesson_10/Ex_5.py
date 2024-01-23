'''Write a Python program that calculates the Fibonacci sequence up to a given number n
using a while loop. The Fibonacci sequence is a series of numbers where each number
is the sum of the two preceding ones.'''

i = [0, 1]
n = int(input())
while i[-1] + i[-2] <= n:
    i.append(i[-1] + i[-2])
print(i)