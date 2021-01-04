import math as m

x = float(input("Podaj kąt: "))


def tryg(kat):
    y = m.radians(kat)
    sin = round(m.sin(y), 4)
    cos = round(m.cos(y), 4)
    if kat != 90:
        tg = round(m.tan(y), 4)
    if kat == 90:
        tg = "BRAK"
    ctg = round(m.atan(y), 4)
    print("Sinus kąta {} to {}, jego cosinus to {}, tangens to {}, a cotangens {}".format(kat, sin, cos, tg, ctg))


tryg(x)
tryg(70)
tryg(90)
tryg(35)
tryg(180)
tryg(240)
tryg(360)
