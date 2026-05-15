nums = [2,42,5,15,63,77,9,15,86,11,34,2,15]
nums.append(100)
nums.append(90)
nums.append(80)
nums.append(70)
print(nums)

nums.remove(2)
nums.remove(42)
print(nums)

print(nums.count(15))

nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

fruits = ['orange','apple','banana','kiwi','mango']
nums.extend(fruits)
print(nums)

copy_nums = nums.copy()
print(copy_nums)

nums.clear()
print(nums)