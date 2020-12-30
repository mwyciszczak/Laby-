zdanie = 'Długo na szturm i szaniec poglądał w milczeniu. Na koniec rzekł; "Stracona"'

indeks = 0
for x in zdanie:
    indeks+= 1
    if x == ".":
        print(zdanie[:indeks])

list = ["Zwinny", "lis", "przeskoczył", "nad", "leniwym", "psem", "."]


cale_zdanie = ' '.join(list)
a = len(cale_zdanie)

cale_zdanie = cale_zdanie [:a-2] + cale_zdanie [a-1:]

print(cale_zdanie)