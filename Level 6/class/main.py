name = 'Giorgi'
password = '777'

name = input('Enter your namme:')
password = input('Enter your password:')
while(name != 'Giorgi' and password != '777'):
    print('Try again')
    name = input('Enter your namme:')
    password = input('Enter your password:')
print('Access Granted')
