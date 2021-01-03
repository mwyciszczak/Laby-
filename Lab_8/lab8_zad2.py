kontakty = {
    'Aleksander': 123456789,
    'Stanisław': 234567890,
    'Jakub': 345678901,
    'Leon': 4567890123,
    'Adam': 5678901234,
    'Zuzanna': 6789012345,
    'Julia': 7890123456,
    'Maja': 8901234567,
    'Zofia': 9012345678,
}
tab = []

print(kontakty)
kontakty.clear()
kontakty["Jan"] = 112233445
kontakty["Zbigniew"] = 566778899
print(kontakty)

for key, value in kontakty.items():
    tab.append(key + " " + str(value))
print(tab)