juices = ["Cola", "Pepsi", "Sprite", "Holiday", "Fanta"]
lst = [x.upper() for x in juices]
print(lst)
print("------")
lst1 = ['hello' for x in juices]
print(lst1)
print("------")
lst2 = [x if x != "Fanta" else "Cola" for x in juices]
print(lst2)