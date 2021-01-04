import pytemp as t

x = int(input("Podaj temperaturę w Celsjuszach: "))

def czy_wrze(temp_cel):
    if t.pytemp(temp_cel, "c", "f") <= 32:
        print("Woda jest zamarznięta i ma {} stopni Fahrenheita.".format(t.pytemp(temp_cel, "c", "f")))
    elif t.pytemp(temp_cel, "c", "f") >= 212:
        print("Woda wrze i ma {} stopni Fahrenheita.".format(t.pytemp(temp_cel, "c", "f")))
    else:
        print("Woda jest spokojna xd i ma {} stopni Fahrenheita.".format(t.pytemp(temp_cel, "c", "f")))

czy_wrze(x)

kel = int(input("Podaj temperaturę w Kelwinach: "))
cel = t.pytemp(kel, "k", "c")
fahr = t.pytemp(kel, "k", "f")

print("{} Kelwinów to {} Fahrenheitów. {} Fahrenheitów to {} Kelwinów. {} Kelwinów to {} Celsjuszy. {} Celsjuszy to {} \
kelwinów.".format(round(kel, 2), round(fahr), round(fahr), round(kel), round(kel), round(cel), round(cel), round(kel)))