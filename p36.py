def palindrome(n, b):

    if str(n) == str(n)[::-1] and b == b[::-1]:
        return True
    return False


s = 0


for i in range(0, 1000000):
    s += i if palindrome(i, bin(i)[2:]) else 0
print s
