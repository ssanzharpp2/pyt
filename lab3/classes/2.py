class Shape():
    def __init__(self):
        self.length = 0
    def area(self):
        print(0)
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length**2)
ln = int(input())
ob = Shape()
ob.area()
ob2 = Square(ln)
ob2.area()
