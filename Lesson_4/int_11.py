"""11.Rounding - 2: Given a real number, round it to the nearest whole."""

a = float(input())
if a - int(a) >= 0.5:
    print(int(a) + 1)
else:
    print(int(a))