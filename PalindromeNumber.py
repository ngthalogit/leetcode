def isPalindrome(x):
    xstr = str(x)
    if xstr == x[::-1]:
        return True
    return False