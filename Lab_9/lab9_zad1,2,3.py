import random
zespoly = ["Iowa Cubs","Memphis Redbirds","Nashville Sounds","Oklahoma City Dodgers","Round Rock Express","Omaha Storm Chasers",
           "Buffalo Bisons","Lehigh Valley IronPigs","Charlotte Knights","Durham Bulls","Syracuse Mets","Norfolk Tides","Atlanta Braves",
           "Los Angeles Dodgers","San Diego Padres","San Francisco Giants","Colorado Rockies","Texas Rangers","Tacoma Rainiers",'Richmond Flying Squirrels']

set1 = {0}
set2 = {0}
set3 = {0}
set4 = {0}
set1.discard(0)
set2.discard(0)
set3.discard(0)
set4.discard(0)

while len(set4) < 10 or len(set3) < 10 or len(set2) < 10 or len(set1) < 10:
    w1 = random.choice(zespoly)
    w2 = random.choice(zespoly)
    w3 = random.choice(zespoly)
    w4 = random.choice(zespoly)
    if w1 not in set1 and len(set1) < 10:
        set1.add(w1)
    if w2 not in set2 and len(set2) < 10:
        set2.add(w2)
    if w3 not in set3 and len(set3) < 10:
        set3.add(w3)
    if w4 not in set4 and len(set4) < 10:
        set4.add(w4)

print(set1, set2, set3, set4)
#intersection
set12 = set1.intersection(set2)
set34 = set3.intersection(set4)
intersection_set = set12.intersection(set34)
print(intersection_set)
#difference

print(len(set1), len(set2), len(set3), len(set4))
