fibs = [1,1]
n = 2

while len(str(fibs[-1])) < 1000:
    fibs.append(sum(fibs))
    fibs = fibs[-2:]
    n += 1

print n
