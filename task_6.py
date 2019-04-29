import random

nums = [random.randint(1, 50) for _ in range(10)]

summ = 0
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

if index_max < index_min:
    arr = nums[index_max + 1 : index_min]
else:
    arr = nums[index_min + 1 : index_max]


for i in range(len(arr)):
    summ += arr[i]

print(f' Оригинальный массив: {nums}, \n '
      f'Срез промежутка: {arr}, \n'
      f' Сумма среза: {summ}')
print(max, min)