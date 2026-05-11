word = input('Enter your word:')
for i in range(15):
    print(word)

secret_number = 12
guess = int(input('Enter your number:'))
while guess != secret_number:
    print('Try again')
    guess = int(input('Enter your number:'))    

print('Correct')

number = int(input('Enter your number:'))
while number <= 150:
    number *= 2

    print(number)

number1 = int(input('Enter your number:'))
number2 = int(input('Enter your number:'))
number3 = int(input('Enter your number:'))
number4 = int(input('Enter your number:'))
number5 = int(input('Enter your number:'))
print(number1 + number2 + number3 + number4 + number5)
