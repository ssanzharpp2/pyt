def hist():
    x = input().split()
    for y in range(len(x)):
        x[y] =int(x[y])
    for a in x:
        print(a*"*")
hist()