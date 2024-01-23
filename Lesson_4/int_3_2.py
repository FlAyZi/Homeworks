"""3.Digit Sum: Input a two-digit natural number and output the sum of its digits. You can
assume that the input will be a two-digit number and need not check that
programmatically."""

a = int(input())
a_1 = a // 10
a_2 = a % 10
print(a_1 + a_2)