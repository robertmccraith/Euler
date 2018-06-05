import itertools

def fact(n):
    if n <2:
        return 1
    return n*fact(n-1)


s = 0
for i in range(3,100000):
    f = sum(map(lambda a: fact(int(a)), list(str(i))))
    if i == f:
        s+=i
        print s
