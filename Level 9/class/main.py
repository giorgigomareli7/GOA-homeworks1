numbers = [12,-45,61,63,-79,63,17,22,96,-56,69,44,-52,6,1,97]
Evens = []
Odds = []
Positives = []
Negatives = []
Multiplied = []
Total = 0
Divisible_by_97 = []
for i in numbers:
    if i % 2 == 0:
        Evens.append(i)
    else:
        Odds.append(i)

    if i > 0:
        Positives.append(i)
    else:
        Negatives.append(i)
    Multiplied.append(i * 10)
    Total += i

    if i % 97 == 0:
        Divisible_by_97.append(i)

print('Evens:',Evens)
print('Odds:',Odds)
print('Positives:',Positives)
print('Negatives:',Negatives)
print('Multiplied:',Multiplied)
print('Total',Total)
print('Divisible_by_97',Divisible_by_97)
