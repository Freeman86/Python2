#python -m timeit -n 100 -s "import prime_nums" "prime_nums.prime()"

import cProfile

def prime(num):
    prime = []
    for i in range(2, num + 1):

        for j in prime:
            if i % j == 0:
                break
        else:
            prime.append(i)


#"prime_nums.prime(10)"
#100 loops, best of 3: 2.67 usec per loop

# "prime_nums.prime(100)"
# 100 loops, best of 3: 41 usec per loop

# "prime_nums.prime(1000)"
# 100 loops, best of 3: 1.28 msec per loop

cProfile.run('prime(1000)')


#cProfile.run('prime(10)')

# 8 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 prime_nums.py:5(prime)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#cProfile.run('prime(100)')

# 29 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 prime_nums.py:5(prime)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run('prime(1000)')

# 172 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 prime_nums.py:5(prime)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}