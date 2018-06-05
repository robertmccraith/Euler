from math import sqrt
primes = [2]
primes.extend(range(3,1000000, 2))

def is_prime(n):

    if n%2 ==0 and n != 2: return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

primes = filter(is_prime, primes)




def rotations(n):
    s = list(str(n))
    if '0' in s: return []

    rots = []
    for i in range(0, len(s)):
        rots.append(int(''.join(s[i:])  + ''.join(s[:i])))
        if not rots[-1] in primes:
            return []
    return rots




cycles = map(rotations, primes)






print len(set([x for y in cycles for x in y ]))
