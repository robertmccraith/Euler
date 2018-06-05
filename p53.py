factorials = [1, 1, 2, 6]

def calcFact(x):
    if len(factorials) > x:
        return factorials[x]
    factorials.append(x*calcFact(x-1))
    return factorials[x]

def c(n,r):
    return calcFact(n) / (calcFact(r)*calcFact(n-r))

count = 0
for n in range(1,101):
    for r in range(1,n):
        count += 1 if c(n, r) > 1000000 else 0

print count
