prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x//2) + 1))
x = input().split()
for y in range(len(x)):
    x[y] =int(x[y])
l = list(filter(prime, x))
print(l)