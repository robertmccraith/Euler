sumSquares = reduce(lambda a,b: a+b*b, range(1,101), 0)

squareSums = sum(range(1,101))**2

print squareSums - sumSquares
