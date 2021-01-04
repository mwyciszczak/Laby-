def kalkulator(x):
    binary = bin(x)
    binary = binary[2:]
    octal = oct(x)
    octal = octal[2:]
    hexadec = hex(x)
    hexadec = hexadec[2:]
    return "Liczba {} w systemie dziesiętnym to {} w systemie dwójkowym, {} w systemie ósemkowym i {} w systemie " \
           "szesnastkowym".format(x, binary, octal, hexadec)

inp_dec = int(input("Podaj liczbę w systemie dziesiętnym: "))
print(kalkulator(inp_dec))
