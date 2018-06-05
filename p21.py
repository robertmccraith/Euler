from math import sqrt

def d(n):
    s = 1
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            s += (i + n/i)
    return s




s = 0
for i in range(2,10000):
    if i == d(d(i)) and d(i) != i:
        s += i

print s
