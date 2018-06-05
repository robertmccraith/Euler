from math import sqrt

l = 0
pl = 0

for p in range(10, 1000):
    s = 0
    for a in range(1,p):
        for b in range(a, p):
            c = sqrt(a**2+b**2)
            if a+b+c == p:
                s+=1
    if s>l:
        pl = p
        l = s
print pl
