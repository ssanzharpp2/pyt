from functools import reduce
from operator import mul
lst = [1,2,3,4,5,6,7,8,9]
print(reduce(mul, lst))



st = str(input())
def let(s):
    up =0
    low = 0
    for x in s:
        if x.isupper():
            up += 1
        elif x.islower():
            low += 1
    return up,low
upp, loww = let(st)
print(f"Uppercase leters: {upp}")
print(f"Lowwercase leters: {loww}")


st = str(input("Write a word: "))
st.lower()
strev = st[::-1]
strev.lower()
if st == strev :
    print("Word is palindrome")
else:
    print("Word is not palindrome")


import time
import math
num = int(input())
ms = int(input())
seconds = float(ms / 1000)
time.sleep(seconds)
res = math.sqrt(num)
print(f"Square root of {num} after {ms}  miliseconds is {res}")



tup1 = (1, True, 0)
res = all(tup1)
print(tup1)
if res:
    print("True")
else:
    print("False")
