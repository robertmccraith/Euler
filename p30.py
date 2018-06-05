import itertools

s = 0

for i in range(2,200000):
    a = [int(x) for x in str(i)]
    a = reduce(lambda x,y: x+y**5, a, 0)
    if i == a:
        print a
        s += a

print s
