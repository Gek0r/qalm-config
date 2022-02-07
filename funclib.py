def splitstring(inputstring, delim):
    x = 0
    tempArr = inputstring.split(delim)
    for item in tempArr:
        if isinstance(item, str):
            tempArr[x] = item.upper()
        x = x + 1
    return tempArr


def detag(name):
    temp = name.split('#')
    if len(temp) >= 2:
        clean = temp[0]
        return clean.upper()
    return name.upper()
