def romanToInteger(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    roman_gr = {
        'IV': 4,
        'IX': 10,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    rs = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s):
            if (s[i] + s[i+1]) in roman_gr.keys():
                rs += roman_gr.get(s[i] + s[i+1])
                i += 2
            else:
                rs += roman.get(s[i])
                i += 1
        else:
            rs += roman.get(s[i])
            i += 1
    return rs