xs = range(1,1000000)


def collatzSeq(n):
    i = 0
    while n != 1:
        i +=1
        if n %2 == 0:
            n = n/2
        else:
            n = 3*n+1
    return i

import numpy as np

print xs[np.argmax(map(lambda a: collatzSeq(a), xs))]
