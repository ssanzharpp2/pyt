juices = ["Cola", "Pepsi", "Sprite", "Holiday", "Fanta"]
for x in juices:
    print(x)
print("---------")
for i in range(len(juices)):
    print(juices[i])
print("---------")
i= 0
while i < len(juices):
    print(juices[i])
    i +=1
print("---------")
[print(x) for x in juices]