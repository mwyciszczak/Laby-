tuple = ("pies", "kot", "kuna", "jenot", "ryś", "dzik")

print("pies" in tuple)#nie do końca rozumiem polecenie chyba
print(tuple.index("pies"))

fraszkawielkiegowieszcza = 'Służba zdrowia, wielki obszar, o którym można bardzo dugo mówić... emmm prawda... we ' \
          'fraszce Kochanowskiego "Szlachetne zdrowie"... emm prawda... "ile cię trzeba cenić" czy jak ' \
          'emm... mmm... tak emm... "jako smakujesz, aż się zepsujesz" prawda... i wtedy dopiero wiemy, kiedy ' \
          'brakuje nam tego zdrowia, emmm... jak ono jest absolutnie kluczowe'

slowo = input("Podaj słowo: ")
if slowo in fraszkawielkiegowieszcza:
    print("Słowo występuje w tekście.")
else:
    print("Słowo nie występuje w tekście.")
