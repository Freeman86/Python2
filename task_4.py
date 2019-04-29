import random

nums = [random.randint(1, 10) for _ in range(10)]

num = nums[0]
count = 0
count_gen = 0
index = 0

for i in range(len(nums)):
    num = nums[i]
    count = 0
    for j in range(len(nums)):
        if num == nums[j]:
            count += 1
            if count_gen < count:
                count_gen = count
                index = j


print(f'{nums},\n Число {nums[index]} всречается {count_gen} раза')