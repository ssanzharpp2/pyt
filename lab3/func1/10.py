def uni():
    x = input().split()
    for y in range(len(x)):
        x[y] =int(x[y])
    lst = []
    for a in x:
        if a not in lst:
            lst.append(a)
    print(lst)
uni()