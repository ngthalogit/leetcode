def plusOne(digits):
    s = 0
    n = len(digits)
    for i in range(n):
        s += digits[i] * (10 ** (n - 1 - i))
    s += 1
    return [int(x) for x in str(s)]
