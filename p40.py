s = ""
i = 1
while len(s) < 1000000:
    s += str(i)
    i += 1


ns = map(lambda a: 10**a, range(0, 6))



print reduce(lambda a,b: a*int(s[b-1]), ns, 1)
