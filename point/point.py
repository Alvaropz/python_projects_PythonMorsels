class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __str__(self):
        return "Point(x={}, y={}, z={})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "Point(x={}, y={}, z={})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, another_point):
        return Point(self.x  + another_point.x, self.y  + another_point.y, self.z  + another_point.z)

    def __sub__(self, another_point):
        return Point(self.x  - another_point.x, self.y  - another_point.y, self.z  - another_point.z)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n, self.z * n)

    def __rmul__(self, n):
        return Point(n * self.x,  n * self.y, n * self.z)