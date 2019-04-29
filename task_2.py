import random

nums = [random.randint(1, 100) for _ in range(10)]

even = []

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        even += str(i)

print(f' Индекс четных чисел: {even} \n '
      f'в массиве {nums} ' )