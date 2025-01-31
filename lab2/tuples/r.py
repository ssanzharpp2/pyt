x = (1,2,3,4)
y = list(x)
y[0] = "a"
y.append(9)
y.remove(2)
x = tuple(y)
print(x)
z = ('b', 'c', 'd')
x += z
print(x)
del x

