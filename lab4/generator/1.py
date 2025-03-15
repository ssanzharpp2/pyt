def num(n):
    for x in range(1, n+1):
        yield x**2
n = int(input())
x = num(n)
while n > 0:
    print(next(x))
    n -= 1


def evens(n):
    for x in range(1, n+1):
        if x%2 == 0:
            yield x
        else:
            continue
n = int(input())
print(*evens(n), sep=', ')



def it(n):
    for x in range(1, n+1):
        if x%12== 0:
            yield x
        else:
            continue
n = int(input())
print(*it(n), sep=', ')


def squares(a, b):
    for x in range(a, b+1):
        yield x**2
a = int(input())
b = int(input())
n = squares(a, b)
for sq in n:
    print(sq)



def inv(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
a = inv(n)
while n > 0:
    print(next(a))
    n -= 1