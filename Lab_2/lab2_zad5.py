promile = float(input("Podaj ilość promili: "))

if promile >= 0.2 and promile <= 0.5:
    print('Stan „wskazujący na spożycie alkoholu”.')
elif promile > 0.5:
    print("Stan nietrzeźwości.")
else:
    print("Trzeźwość.")