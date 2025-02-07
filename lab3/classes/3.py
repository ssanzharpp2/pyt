class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length*self.width)
ln = int(input())
wd = int(input())
ob = Rectangle(ln, wd)
ob.area()