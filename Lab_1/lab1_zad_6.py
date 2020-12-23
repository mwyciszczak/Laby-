def predkosc(dystans, czas):
    v = dystans/czas * 60
    print("Prędkość to {} km/h.".format(v))
    return v

x = predkosc(30, 15)
y = predkosc(30, 12)
print('Średnia prędkość to {} km/h.'.format((x+y)/2))

