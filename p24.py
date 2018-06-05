from itertools import permutations
print list(enumerate(''.join(p) for p in permutations('0123456789')))[999999]
