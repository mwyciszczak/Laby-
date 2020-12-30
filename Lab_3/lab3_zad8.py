y = 0
for x in range(0, 1000):
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
        y = x
print(y)
