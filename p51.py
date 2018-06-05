primes = [2,3]

def prime_under(x):
    p = primes[-1]

    while x > primes[-1]:
        p += 2
        if len(filter(lambda a: p%a == 0, primes)) == 0:
            primes.append(p)


import itertools
from math import sqrt

# for x in itertools.count(10000001,2):
    # print x

x = 56003
replacements = []
for i in range(len(str(x))):
    rep = []
    for j in range(i, len(str(x))):
        st = str(x)
        for k in range(10):
            st[i] = str(k)
            st[j] = str(k)
            rep.append(int(st))
    replacements.append(rep)

    primes_under(sqrt(i))
