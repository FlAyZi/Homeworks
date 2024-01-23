"""7. Write a Python program to print the floating numbers upto 2 decimal places
(number must be not greater than 10)
Example:
Sample = 2.145548
Expected - 2.14
_______________________
Sample = 9.5748
Expected - 9.57 """

def str_7(int_000):
    if int_000 >= 10:
        return int_000
    else:
        int_000 = str(int_000)[:4]
        return float(int_000)

