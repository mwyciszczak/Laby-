inp = int(input("Na jakiej wysokości lecimy? [w metrach]: "))

if inp < 5000:
    print("{} km to za nisko".format(inp/1000))
else:
    print("Na tej wysokości jesteś już bezpieczny")