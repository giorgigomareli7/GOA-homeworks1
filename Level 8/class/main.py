password = 1234
balance = 100
attemps = 3
for enter_password in range(3):
    enter_password = int(input('Enter password:'))
    if password == enter_password:
        print('Correct password')
        withdraw = float(input('How much money do you want to withdraw?'))
        if withdraw <= balance:
            balance = balance - withdraw
            print(f'You got {balance} left on your balance')
        else:
            print("You don't have enough money on your balance!")
        break
    else:
        print('Incorrect password!Try again')
        attemps -= 1
else:
    print('Your bank is blocked')