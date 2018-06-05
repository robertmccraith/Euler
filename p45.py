import itertools
from math import sqrt

def roots(a,b,c):
    return ((-b+sqrt(b**2-4*a*c))/(2*a), (-b-sqrt(b**2-4*a*c))/(2*a))

def check(x):
    pent = roots(3, -1, -2*x)
    if not (pent[0].is_integer() and pent[0] > 0) or (pent[1].is_integer() and pent[1] > 0):
        return False

    he = roots(2, -1, -x)
    if not (he[0].is_integer() and he[0] > 0) or (he[1].is_integer() and he[1] > 0):
        return False

    return True



for n in itertools.count(286):
    if check(n*(n+1)/2):
        print n*(n+1)/2
        break
