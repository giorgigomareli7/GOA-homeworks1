name = 'gIOrGi'
print(name.capitalize())

email = (input('შეიყვანეთ თქვენი იმეილი:'))
if email.endswith('.com'):
    print('იმეილი მოიძებნა')
else:
    print('ხელახლა სცადეთ')

name = ' giorgi '
print(name.strip())

text = 'მე მიყვარს ჯავასკრიპტი'
text = text.replace('ჯავასკრიპტი','პითონი')
print(text)

list = 'butter,bread,apple,cheess,meat'
products_list = list.split(',')
print('total products:',len(products_list))

date = ['2026','05','15']
date1 = '/'.join(date)
print(date1)

text = 'სასწრაფო შეტყობინება: შეცდომა სისტემაში'
print(text.find('შეცდომა'))

phone_number = input('Enter your phone number:')
if phone_number.isdigit():
    print('correct')
else:
    print('Enter just digits')

text = 'აი ია, კარგად იარეო'
check = text.count('ა')
print(check)

web = input('Enter your website link:')
if web.startswith('https://"/'):
    print('safe link')
else:
    ('The link is unsafe')



