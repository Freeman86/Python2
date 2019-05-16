#python -m timeit -n 100 -s "import task_3" "task_3.func()

import cProfile

def func(digit):
    import random

    nums = [random.randint(1, 100) for _ in range(10)]

    even = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even += str(i)

# "task_3.func(10)
# 100 loops, best of 5: 19.1 usec per loop

# "task_3.func(100)
# 100 loops, best of 5: 18.9 usec per loop

# "task_3.func(1000)
# 100 loops, best of 5: 18.9 msec per loop

# "task_3.func(10000)
# 100 loops, best of 5: 18.9 msec per loop

#אכדמנטעל O(n)

cProfile.run('func(10)')

cProfile.run('func(10)')
# 59 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:218(randint)
#        10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task_1.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:7(func)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('func(100)')

# 61 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:218(randint)
#        10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task_1.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:7(func)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        15    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('func(1000000)')

# 57 function calls in 0.000 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:218(randint)
#        10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task_1.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:7(func)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        11    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}