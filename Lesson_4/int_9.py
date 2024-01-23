"""9.Line Segment: You are given four real numbers - the coordinates of two points on a
plane. The first two numbers are the x and y coordinates of the first point,
and the last two numbers are the x and y coordinates of the second point.
Output the length of the line segment bounded by the two points."""

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
result = (((x_2 - x_1)**2) + ((y_2 - y_1)**2))**0.5
print(result)