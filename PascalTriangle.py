from math import factorial


def generate(numRows):
    r = []
    for n in range(numRows):
        l = []
        for k in range(n + 1):
            s = factorial(n) / (factorial(n - k) * factorial(k))
            l.append(s)
        r.append(l)
    return r
