def cycleLen(d):
    remainders = []

    x = 10**(len(str(d)))
    while (x%d) not in remainders:
        remainders.append(x%d)
        x = x%d
        if x == 0:
            break
        while x<d:
            remainders.append(0)
            x *= 10
        if len(remainders)%2 == 0 and remainders[:len(remainders)/2] == remainders[len(remainders)/2:]:
            break
    return len(remainders)/2




import numpy as np

print np.argmax(map(cycleLen, range(1,1000)))+1
