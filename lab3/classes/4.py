import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, x1, y1):
        self.x = x1
        self.y = y1
        print(self.x, self.y)
    def distance(self, initial):
        d = math.sqrt((self.x - x)**2 + (self.y - y)**2)/2
        print(d)
x = int(input())
y = int(input())
point = Point(x,y)
point.show()
ipoint = Point(0, 0)
x1 = int(input())
y1 = int(input())
point.move(x1, y1)
point.distance(ipoint)