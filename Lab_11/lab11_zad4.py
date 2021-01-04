def stopy(x):
    cm = x * 30.48
    m = cm / 100
    mm = cm * 10
    km = m / 1000
    return "{} stóp to: {} centymetrów, {} metrów, {} milimetrów, {} kilometrów".format(x, cm, m, mm, km)


def cale(x):
    cm = x * 2.54
    m = cm / 100
    mm = cm * 10
    km = m / 1000
    return "{} cali to: {} centymetrów, {} metrów, {} milimetrów, {} kilometrów".format(x, cm, m, mm, km)


ile_stop = float(input("Podaj ile stóp: "))
ile_cali = float(input("Podaj ile cali: "))

print(stopy(ile_stop))
print(cale(ile_cali))
