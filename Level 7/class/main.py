number = 1
while number <= 10:
    if number == 7:
        print('Number found')
    else:
        print('Number:' ,number)

    number += 1

for i in range(1, 10):
    if i % 2 == 0: 
         print('Even')
    else:
        print('Odd')

number = int(input('Enter your number:'))
if number > 5:
    if number % 2 == 0:
        print('Your number is more than 5 and Even')
    else:
        print('Your number is just more than 5')
else:
    print('Your number is none of them')
