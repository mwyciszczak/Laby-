i = 0
sum = 0

while i < 12:
    i += 1
    sum = (sum + 333) * 1.08

print("Pracownik zaoszczędzi {} złotych.".format(round(sum, 2)))

#chciałbym takie oprocentowanie, a nie jakiś paskudny 1 promil w millenium