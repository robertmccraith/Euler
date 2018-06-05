
from math import sqrt

def is_prime(n):
    if n < 2 or n%2 == 0: return False
    for i in range(3,int(sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True


maxLen = 0
prod = 0

def f(a,b):
    n = 0
    y = n**2 + a*n + b

    while is_prime(y):
        n += 1
        y = n**2+a*n+b
    return n


for a in range(-1000, 1001):
    for b in range(-1000, 1001):

        seqLen = f(a,b)

        if seqLen > maxLen:
            maxLen = seqLen
            prod = a*b
print prod
