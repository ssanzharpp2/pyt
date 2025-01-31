juices = ["Cola", "Pepsi", "Sprite", "Holiday", "Fanta"]
lst = []
for x in juices:
    if "e" in x:
        lst.append(x)
print(lst)
print("-----")
nlst = [x for x in juices if "l" in x]
print(nlst)
print("-----")
a = [x for x in juices if x != "Cola"]
print(a)
