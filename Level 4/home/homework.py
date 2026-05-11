#logical operator
age = 10
print(age > 20 and age<20)
print(10 > 5  and 40 == 30 and  7 < 3 and 20 >= 50)
print(10 < 5  and 40 != 30  and 7 > 3  and 20 <= 50)
temperature = 38
print(37>temperature or temperature<39)
print(3>4 or 10<20 or 20==20 or 100!=99)
wins = 10
ties = 5
print(wins>4 or ties>4)
username = 'giorgi'
print(username == 'giorgi' or username == 'Nika')
print(username == 'giorgi' and username == 'Nika')
height = 1.80
print(10>height and 2<height)
favourite_food = 'pizza'
print(favourite_food == 'shawarma' or favourite_food == 'pizza')

#logical operator and comparasion operator
print(10>5 or 5<20)
print(15==14 or 49!=40)
print(6 >=7 or 10 <= 20)
print(9 == 9 or 100>101)
print(83 != 82 or 7<47)

print(10>5 and 5<20)
print(15==14 and 49!=40)
print(6 >=7 and 10 <= 20)
print(9 == 9 and 100>101)
print(83 != 82 and 7<47)
 
 #input არის ფუნქცია რისი საშუალებითაც ჩვენ მომხმარებელს მივუთითებთ დასმულ კითხვაზე პასუხის გაცემისაკენ.input-ს მაგალითებია კოდები რასაც ჩვენ კომპიუტერში შეგვყავს,ხმა რომელიც კომპიუტერში შედის მიკროფონის საშუალებით და ა.შ

#logical operator,comparasion operator and input
name1 = (input('Enter your name:'))
wins1 = (name1 + input('Enter your wins:'))
name2 = (input('Enter your name:'))
wins2 = (name2 + input('Enter your wins:'))
print(wins1 > wins2 or wins1 < wins2)

age = input('Enter your age:')
weight = input('Enter your weight:')
print(age>weight and age != weight)

last_name = input('Enter your last name:')
first_name = input('Enter your first name:')
print(last_name == 'topuria' or first_name == 'ilia')

