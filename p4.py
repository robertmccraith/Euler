products = [x*y for x in range(100,999) for y in range(100,999)]

products = sorted(set(products))


def palindrome(n):
    s = str(n)
    while s is not "" and s[0] == s[-1]:
        s = s[1:-1]
    return s is ""


print [a for a in products if palindrome(a)][-1]
