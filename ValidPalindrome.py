import re


def isPalindrome(s):
    if s == " ":
        return True
    s = s.lower()
    news = re.sub(r'[^a-zA-Z0-9]', '', s)
    return news == news[::-1]