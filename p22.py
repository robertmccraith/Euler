f = open('p022_names.txt').read()

n = f.split(",")

n = map(lambda a: a.replace("\"",""), n)

n = sorted(n)

n = map(lambda a: reduce(lambda b,c: b+ord(c)-64, list(a), 0), n)

vals = [(x+1)*y for x,y in enumerate(n)]

print reduce(lambda a,b: a+b, vals)
