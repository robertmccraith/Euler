n = 600851475143

from math import sqrt
factors = set()

for i in range(2, int(sqrt(n))):
    while n%i == 0:
        factors.add(i)
        n = n/i


print sorted(factors)[-1]
