class x():
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())
ob = x()
ob.getString()
ob.printString()
