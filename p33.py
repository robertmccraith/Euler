num = []
denom = []

for i in [float(x) for x in range(10,100)]:
    for j in [float(x) for x in range(int(i)+1,101)]:

        if (not (i%10 == 0 or j%10 == 0)) and int(i/10)/(j%10) == i/j and i%10 == int(j/10):
            num.append(i)
            denom.append(j)

n = reduce(lambda a,b: a*b, num, 1)
m = reduce(lambda a,b: a*b, denom, 1)

print n, m
