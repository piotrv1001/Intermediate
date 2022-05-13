import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({x}, {y})".format(x = self.x, y = self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def lineLength(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

p1 = Point(1, 3)
p2 = Point(2, 5)
print(p1)
print(p2)
print(p1 + p2)
print(p2 - p1)
line = p1.lineLength(p2)
print(f"Line {p1} and {p2} is {line:.2f}")
