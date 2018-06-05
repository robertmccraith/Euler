import itertools
from math import sqrt

primes = [2,3]

def isPrime(x):
    p = primes[-1]

    while x > primes[-1]:
        p += 2
        if len(filter(lambda a: p%a == 0, primes)) == 0:
            primes.append(p)

    return x in primes




for i in itertools.count(9, 2):
    if isPrime(i):
        continue

    s = map(lambda a: (i, a, sqrt(float(i-a)/2)) if (i-a) > 0 else (), primes)



    s = filter(lambda a: a[2].is_integer() if len(a) > 0 else False, s)

    if len(s) == 0:
        print i
        break
