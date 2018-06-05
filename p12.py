import itertools
from math import sqrt

def divisors(n):
    ds = [1,n]
    for i in range(2,int(sqrt(n))):
        if n%i == 0:
            ds.append(i)
            ds.append(n/i)
    return len(ds)



for i in itertools.count():
    s = ((i+1)*i)/2

    d = divisors(s)
    if d>500:
        print s
        break
