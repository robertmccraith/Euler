import itertools


primes = [2,3]

def prime_factors(x):
    p = primes[-1]

    while x/4 > primes[-1]:
        p += 2
        if len(filter(lambda a: p%a == 0, primes)) == 0:
            primes.append(p)

    return filter(lambda a: x%a == 0, primes)


for i in itertools.count(100000):
    len4 = len(prime_factors(i+3))
    if len4 != 4:
        i += 4
        continue
    if len(prime_factors(i)) == 4 and len(prime_factors(i+1)) == 4 and len(prime_factors(i+2)) == 4 and len(prime_factors(i+3)) == 4:
        print i
        break
