x = ("a", "b", "c", "d")
(first, second, third, fourth) = x
print(third)

y = ("a", "b", "c", "d")
(first, *letters) = x
print(letters)