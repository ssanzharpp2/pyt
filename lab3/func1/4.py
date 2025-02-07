def filter_prime(lst):
    for x in lst:
        if x<=1:
            continue
        b = True
        for y in range(2, x//2 + 1):
            if y != 0 and x % y == 0:
                b = False
                break
            
        if b:
            print(x)
        
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
filter_prime(lst)