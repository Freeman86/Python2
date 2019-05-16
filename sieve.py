#python -m timeit -n 100 -s "import prime_nums" "prime_nums.prime()"

import cProfile

def sieve(num):

    a = [i for i in range(num + 1)]
    a[1] = 0
    s = []

    i = 2
    while i <= num:
        if a[i] != 0:
            s.append(a[i])
            for j in range(i, num + 1, i):
                a[j] = 0
        i += 1

# "sieve.sieve(10)"
# 100 loops, best of 3: 5.97 usec per loop
#
# "sieve.sieve(100)"
# 100 loops, best of 3: 41.7 usec per loop
#
# "sieve.sieve(1000)"
# 100 loops, best of 3: 424 usec per loop

cProfile.run('sieve(1000)')

#cProfile.run('sieve(10)')

# 9 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 sieve.py:5(sieve)
#         1    0.000    0.000    0.000    0.000 sieve.py:7(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run('sieve(100)')

# 30 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 sieve.py:5(sieve)
#         1    0.000    0.000    0.000    0.000 sieve.py:7(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run('sieve(1000)')

# 173 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 sieve.py:5(sieve)
#         1    0.000    0.000    0.000    0.000 sieve.py:7(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}