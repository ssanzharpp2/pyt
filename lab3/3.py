def f(nmh, nml):
    for x in range(nmh+1):
        if (4*x+2*(nmh-x) == nml):
            print(x,"rabbits and", nmh - x, "chickens")
            break
        else:
            continue

heads = 35
legs = 94
f(heads, legs)