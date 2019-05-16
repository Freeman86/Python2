#python -m timeit -n 100 -s "import task_1" "task_1.func()

import cProfile

def func(num):

    import random

    nums = [random.randint(1, 50) for _ in range(num)]

    summ = 0
    max = 0
    index_max = 0
    index_min = 0
    min = nums[0]


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

# "task_1.func(10)
# 100 loops, best of 5: 19.9 usec per loop

# "task_1.func(100)
# 100 loops, best of 5: 161 usec per loop

# "task_1.func(1000)
# 100 loops, best of 5: 1.62 msec per loop

#אכדמנטעל O(n**2)

cProfile.run('func(1000)')

# cProfile.run('func(10)')

# 59 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:218(randint)
#        10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task_1.py:6(func)
#         1    0.000    0.000    0.000    0.000 task_1.py:8(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('func(100)')

# 533 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:218(randint)
#       100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task_1.py:6(func)
#         1    0.000    0.000    0.000    0.000 task_1.py:8(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       126    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('func(1000)')

#  5265 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:218(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.002    0.002 task_1.py:6(func)
#         1    0.000    0.000    0.002    0.002 task_1.py:8(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1258    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}