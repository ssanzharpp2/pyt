def filter_prime(lst):
    for x in lst:
        if x<=1:
            continue
        b = True
        for y in range(x//2):
            if y != 0 and x % y == 0:
                b = False
                break
            
        if b:
            print(x)
        
lst = [1,2,3,4,5,6,7,8,9,10]
filter_prime(lst)