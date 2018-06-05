primes = [2,3]

def prime_under(x):
    p = primes[-1]

    while x > primes[-1]:
        p += 2
        if len(filter(lambda a: p%a == 0, primes)) == 0:
            primes.append(p)


prime_under(100000)

print primes
prime = 0
maxLen = 0

for i in range(0, len(primes)):
    s = primes[i]
    if len(primes) - i < maxLen:
        break
    for j in range(i+1, len(primes)):
        s += primes[j]
        if s > 1000000:
            break
        if ((s in primes) or len(filter(lambda a: s%a == 0, primes)) == 0)   and j-i >= maxLen:
            maxLen = j-i+1
            prime = s
            print prime, maxLen
