def spy():
    x = input().split()
    for y in range(len(x)):
        x[y] =int(x[y])
    lst = []
    for a in x:
        if a == 0:
            lst.append(a)
        elif a == 7:
            lst.append(a)
            break       
    if lst == [0,0,7]:
        print("True")
    else: print("False")
spy()