wins = int(input('Enter your wins:'))
ties = int(input('Enter your ties:'))

points = wins + ties * 0.5
print(points)

bill = int(input('Enter your bill:'))
tip = bill*20/100
print(tip)