tuple = (1, 2, 3, "a", "b", "c")
print(len(tuple))
print(id(tuple))

tuple = tuple + (2, "d")
print(tuple)
print(id(tuple))

tuple = list(tuple)
print(id(tuple))
