primes = [2,3,5,7,11,13,17]

from itertools import permutations

perms = list(permutations(list("1234567890")))
total = 0

for i in perms:
    s = ''.join(i)
    x = int(s)
    divides = True
    for j in range(1, len(s)-2):
        if int(s[j:(j+3)])%primes[j-1] != 0:
            divides = False
            break
    if divides:
        total += x

print total
