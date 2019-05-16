#python -m timeit -n 100 -s "import task_2" "task_2.func()

import cProfile

def func(digit):
    import random

    nums = [random.randint(1, 10) for _ in range(digit)]

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

# "task_2.func(10)
# 100 loops, best of 5: 29 usec per loop

# "task_2.func(100)
# 100 loops, best of 5: 893 usec per loop

# "task_2.func(1000)
# 100 loops, best of 5: 83 msec per loop

#אכדמנטעל O(n**2)

cProfile.run('func(1000)')

# cProfile.run('func(10)')

# 71 function calls in 0.000 seconds
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
#        11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        15    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('func(100)')

# 659 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:218(randint)
#       100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.001    0.001    0.001    0.001 task_1.py:6(func)
#         1    0.000    0.000    0.000    0.000 task_1.py:8(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       153    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('func(1000)')

# 6557 function calls in 0.085 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.085    0.085 <string>:1(<module>)
#      1000    0.001    0.000    0.002    0.000 random.py:174(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:218(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.083    0.083    0.085    0.085 task_1.py:6(func)
#         1    0.000    0.000    0.002    0.002 task_1.py:8(<listcomp>)
#         1    0.000    0.000    0.085    0.085 {built-in method builtins.exec}
#      1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1551    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}