def pandigital(s, i):
    ns = set(list("123456789")[:i])

    return len(str(s)) == i and set(list(str(s))) == ns


from math import sqrt
def is_prime(n):
    if n == 2 or n == 3: return True
    if n%2 == 0 or n < 3: return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True


import itertools

l = 0

for i in itertools.count(11):
    if is_prime(i):
        for j in range(2,10):
            if pandigital(i, j) and i > l:
                l = i
                print l
    if len(str(i))> 9:
        break
