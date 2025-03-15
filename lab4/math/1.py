import math
a = int(input("Input degree: "))
print("Output degree:", math.radians(a))


import math
h = int(input("Height: "))
b1 = int(input("Base, first value: "))
b2 = int(input("Base, second value: "))
print("Expected Output:",(b1+b2)/2 * h)


import math
n = int(input("Input number of sides: "))
l = int(input("Input the lengh of a side: "))
A = (l**2 * n)/(4 * math.tan(math.pi/n))
print(f"The area of the polygon is:", A)


import math
a = int(input("Lengh of base: "))
h = int(input("Height of parallelogram: "))
print(a*h)