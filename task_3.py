import random

nums = [random.randint(1, 100) for _ in range(10)]

max = 0
index_max = 0
index_min = 0
min = nums[0]
nums_new = nums[:]

for i in range(len(nums)):
    if nums[i] > max:
        max = nums[i]
        index_max = i
    if nums[i] < min:
        min = nums[i]
        index_min = i

nums_new[index_min] = max
nums_new[index_max] = min


print(f' Оригинальный массив: {nums}, \n '
      f'       Hовый массив: {nums_new}, \n'
      f' Максимальное и минимальное значения: {max, min}, \n'
      f' И их индексы: {index_max, index_min}')