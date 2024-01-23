"""6.Comparison: Input two positive integers, and output a line describing their relation.
Follow the sample format."""

a = int(input())
b = int(input())
if a > b:
    print(a, '>', b)
elif a < b:
    print(a, '<', b)
else:
    print(a, '=', b)