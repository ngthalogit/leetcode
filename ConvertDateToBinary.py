def convertDateToBinary(date):
    year, month, day = date.split('-')

    binary_year = toBinary(int(year))
    binary_month = toBinary(int(month))
    binary_day = toBinary(int(day))

    binary_date = "{}-{}-{}".format(binary_year, binary_month, binary_day)

    return binary_date


def toBinary(s):
    binary = str()
    while s != 0:
        binary += str(s % 2)
        s = int(s / 2)
    return binary[::-1]