from math import factorial


def getRow(rowIndex):
    l = []
    for k in range(rowIndex + 1):
        s = factorial(rowIndex) / (factorial(rowIndex - k) * factorial(k))
        l.append(s)
    return l

print(getRow(3))