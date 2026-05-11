scores = [10,20,45,60,62,73,92]
total_scores = 0
for i in scores:
    print('ქულა',i)
    if i <= 50:
        print('თქვენ ჩაიჭერით!')
    elif i <= 90:
        print('თქვენ ჩააბარეთ გამოცდა!')
    else:
        print('ფრიადი')
    total_scores += i
    საშუალო = total_scores / len(scores)


numbers = [20,54,60,29,61,72]
total = 0
for i in numbers:
    total += i
print('total',total)

numbers = [1,42,51,21,7,72,11,4,9,35]
if 7 in numbers:
    print('7 არის სიაში')
else:
    print('7 არარის სიაში')

values = [10,5.6,'hello',77,'goodbye']
count = 0
for i in values:
    count += i

print(f'სიაში არის {count} მნიშვნელობები')