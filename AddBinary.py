def addBinary(a, b):
    na, nb = len(a), len(b)
    ia, ib = 0, 0
    for i in range(na):
        ia += int(a[i]) * (2 ** (na - 1 - i))
    for i in range(nb):
        ib += int(b[i]) * (2 ** (nb - 1 - i))
    s = ia + ib
    binary = str()
    while s != 0:
        binary += str(s % 2)
        s /= 2
    if a == '0' and b == '0':
        binary = '0'
    return binary
