primes = [2,3]

def prime_under(x):
    p = primes[-1]

    while x > primes[-1]:
        p += 2
        if len(filter(lambda a: p%a == 0, primes)) == 0:
            primes.append(p)

def permutation(a,b,c):
    return set(str(a)) == set(str(b)) and set(str(b)) == set(str(c))


prime_under(10000)
primes = filter(lambda a: a>1000, primes)

for p in primes:
    diffs = map(lambda a: a-p, primes)
    diffs = filter(lambda a: a>0, diffs)
    for d in diffs:
        if (p+2*d) in primes and permutation(p, p+d, p+2*d):
            print p, p+d, p+2*d, d
