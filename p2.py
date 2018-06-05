fibs = [1,2]


while fibs[-1] < 4000000:
    fibs.append(fibs[-1]+fibs[-2])


print reduce(lambda a,b: a+b, [a for a in fibs if a%2 ==0 ],0)
