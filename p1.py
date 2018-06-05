print reduce(lambda a, b: a+b, [a for a in range(1,1000) if (a%3==0 or a%5==0)], 0)
