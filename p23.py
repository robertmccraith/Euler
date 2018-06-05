from math import sqrt

def abundant(n):
    s = 1
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
                s += i + n/i
                if i**2 == n:
                    s -= i

    return s > n





abundants = filter(abundant, range(1,28123))


sumAbundants = [a+b for a in abundants for b in abundants if a+b <= 28123]


xs = set(range(1,28123))
for i in sumAbundants:
    xs.discard(i)


print sum(xs)
