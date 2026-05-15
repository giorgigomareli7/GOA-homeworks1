nums = [12, 7, 19, 24, 33, 40, 55]
evens = []
for i in nums:
    if i % 2 == 0:
        evens.append(i)
print(evens)


brands = ['addidas','polo','gucci','offwhite','nike']
if 'nike' in brands:
    index = brands.index('nike')
    print(f'nike ნაპოვნია ინდექსზე {index}')

else:
    brands.append('nike')
    print(brands)


names = ['anano','nika','giorgi','anano','luka','anano']
count = names.count('anano')
while count > 1:
    count -= 1
    names.remove('anano')
print(names)


nums = [10, 20, 30, 40, 50]
total_nums = 0
while len(nums) > 2:
    removed_nums = nums.pop()
    total_nums += removed_nums
print(nums)
print(total_nums)


class1 = [2,6,8,9,9,10,7,4,10,8]
class2 = [4,5,10,1,3,9,8,10,7,5]
class1.extend(class2)
class1.sort(reverse = True)
print(class1)


letters = ['A', 'B', 'C', 'D']
index = 1
for i in range(len(letters) - 1):
    letters.insert(index ,'_')
    index += 2
print(letters)


id = [101, 102, 103]
archive_orders = id.copy()
if id ==  archive_orders:
    id.clear()
print(id)


letters = ['r', 'a', 'd', 'a', 'r']
copy = letters.copy()
copy.reverse()
if letters == copy:
    print('სიტყვა პალინდრომია')
else:
    print('სიტყვა არარის პალინდრომია')


nums = [5, 15, 25]
while len(nums) < 7:
    nums.append(nums[-1] + 10)
print(nums)


fruits = ['apple','kiwi','banana','cherry','grapes','lemon']
copy = fruits.copy()
for fruit in copy:
    if 'a' in fruit:
        fruits.remove(fruit)
print(fruits)