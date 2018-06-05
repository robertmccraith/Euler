def pandigital(x,y,z):
    s = list(str(x)+str(y)+str(z))

    return len(s) == 9 and len(set(s)) == 9 and '0' not in s



s = 0
import itertools
from math import sqrt

for i in range(2, 10000):

    for j in range(2, int(sqrt(i))+1):
        if i%j == 0:
            p = pandigital(i, j, i/j)

            if p >0:
                print i/j, j, i
                s += i
                print s
                break
