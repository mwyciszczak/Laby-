import random

A = ()
B = ()
id1 = (id(A), id(B))
while len(A) < 100:
    losowa1 = random.randint(0, 1000)
    losowa2 = random.randint(0, 1000)
    if losowa1 % 2 == 0 and losowa2 % 2 == 0:
        A = A + (losowa1, losowa2)

while len(B) < 100:
    losowa1 = random.randint(0, 100)
    losowa2 = random.randint(0, 100)
    if losowa1 % 2 != 0 and losowa2 % 2 != 0:
        B = B + (losowa1, losowa2)

A = A + B
print(len(A))

if 0 in A:
    print("Liczba 0 występuje w krotce.")
if 100 in A:
    print("Liczba 100 występuje w krotce.")

print("Początkowy adres krotek A i B to odpowiednio {}, zaś aktualny adres krotki połączonej to {}.".format(id1, id(A)))