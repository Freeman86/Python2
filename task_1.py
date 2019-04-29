
import random

nums = [random.randint(2, 99) for _ in range(10)]

digits = [2, 3, 4, 5, 6, 7, 8, 9, ]
count = 0
count_gen = []

for i in range(len(digits)):
    digit = digits[i]
    count = 0
    for j in range(len(nums)):
        if nums[j] % digit == 0:
            count += 1
    count_gen.append(count)
    print(f' Число {digits[i]} кратно {count_gen[i]}')


