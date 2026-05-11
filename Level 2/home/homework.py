#დღეს ჩვენ ვისწავლეთ variable-ცვლადი.ცვლადები გამოიყენება იმისათვის რომ შიგნით შევინახოთ ინფორმაცია.ცვლადები შედგება სამი ნაწილისაგან:1.ცვლადის დასახელება 2.ტოლობის ნიშანი და 3.მნიშვნელობა.
#ასევე ვისწავლეთ კონკატინაცია.კონკატინაცია არის მოვლენა როდესაც ჩვენ სტრინგებს ერთმანეთს ვუმატებთ.

#Variables:
name = 'Giorgi'
print(name)
country = 'Georgia'
print(country)
age = 15
print(age)
favourite_food = 'shawarma'
print(favourite_food)
favourite_sport = 'wrestling'
print(favourite_sport)
height = 1.85
print(height)
city = 'Tbilisi'
print(city)
info = f"Hello,my name is {name},i'm {age} years old,my height is {height},i live in {country},{city},my favourite food's {favourite_food},and favourite sport's {favourite_sport}"
print(info)

#concatination კონკატინაცია
name = 'giorgi'
last_name = ' gomareli'
print(name + last_name)

name = 'khvicha'
last_name = ' kvaratskhelia'
print(name + last_name)

name = 'Ilia Topuria'
sport = 'UFC'
info = f"{name} {sport}'ს მოჩხუბარეა"
print(info)


number = 12
year = 2026
temperature = 20
grade = 100
age = 41
print(number + year)
print(grade - temperature)
print(number * grade)
print(grade // temperature)
print(grade / temperature)
print(year % age)
print(number ** temperature)