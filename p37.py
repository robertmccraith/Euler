from math import sqrt

def is_prime(n):
    if n == 2 or n == 3: return True
    if n%2 == 0 or n < 3: return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

import itertools

truncatable = []

for i in itertools.count(8):
    if len(truncatable) > 10:
        break

    if not is_prime(i):
        continue

    s = str(i)
    for j in range(1, len(s)):
        if not (is_prime(int(s[j:])) and is_prime(int(s[:j]))):
            break
        if j == len(s)-1:
            truncatable.append(i)
            print i

print sum(truncatable)
