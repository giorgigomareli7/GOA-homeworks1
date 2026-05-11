positive = 0
negative = 0
for i in range(5):
    number = int(input('Enter your number:'))
    
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
print('Total numbers of positive ones:',positive)
print('Total numbers of negative ones:',negative)


Even = 0
n = int(input('Enter your number:'))
for i in range(1, n):
    if i % 2 == 0:
        Even += 1
print('Total amount of Evens:', Even)

number = 77
guess = int(input('Guess the number:'))
if guess == number:
    print('Correct')
else:
    print('Inncorrect')


for i in range(3):
    number = int(input('Enter number:'))
    average = (number + number + number) // 3

if average > 50:
    print('Passed')

else:
    print('Failed')


    