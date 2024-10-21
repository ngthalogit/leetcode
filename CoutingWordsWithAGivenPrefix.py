def prefixCount(words, pref):
    i = 0
    for i in words:
        if i.startswith(pref):
            i += 1
    return i
