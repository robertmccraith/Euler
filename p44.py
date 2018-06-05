from math import fabs, sqrt
ps = []




def pent(n):
    if not n*(3*n-1)/2 in ps:
        ps.append(n*(3*n-1)/2)
    return n*(3*n-1)/2

def checkPent(x):
    while ps[-1] < x:
        pent(len(ps)+1)

    return x in ps






minD = 1000000

import itertools
for i in itertools.count(1):
    x = pent(i)
    p = filter(lambda a: a<x, ps)
    
    s = map(lambda a: (x,a,x+a,fabs(x-a)), p)

    s = filter(lambda a: checkPent(a[2]) and checkPent(a[3]) , s)
    if len(s) > 0:
        print s
        break
