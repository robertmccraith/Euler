fact = reduce(lambda a,b: a*b, range(1,101), 1)

print sum(map(int,list(str(fact))))
