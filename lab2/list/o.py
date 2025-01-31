juices = ["Cola", "Pepsi", "Sprite", "Holiday", "Fanta"]
nums = [1,2,3,4,5]
lst = juices + nums
print(lst)
for x in nums:
    juices.append(x)
print(juices)
nums.extend(juices)
print(nums) 