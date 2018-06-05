primes = [2,3,5,7,11,13]

import itertools

for i in itertools.count(15, 2):
    if len([p for p in primes if i%p==0]) == 0:
        primes.append(i)
        print len(primes)
        if len(primes) == 10001:
            break

print primes[-1]
