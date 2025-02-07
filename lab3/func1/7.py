def b():
    x = input().split()
    cnt = 0
    dd = False
    for y in range(len(x)):
        x[y] =int(x[y])
    for a in x:
        if a == 3:
            cnt += 1
            continue
        if cnt == 2:
            dd = True
            break
        else:
            cnt = 0
    if dd:
        print("True")
    else:
        print("False")
b()
        
            
