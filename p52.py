import itertools



def checkSame(xs):
    ys = map(lambda a: set(str(a)), xs)

    return reduce(lambda a,b: a + (b == ys[0]), ys, 0) == len(xs)





for i in itertools.count(10):
    multiples = [i, i*2, i*3, i*4, i*5, i*6]
    if checkSame(multiples):
        print i
        break
