def buildPrefixArray(string):

    temp = [0] * len(string)
    temp[0] = 0
    i = 1
    len = 0

    while i < len(string):
        if string[i] == string[len]:
            temp[i] = len + 1
            i += 1
            len += 1
        else:
            if j > 0:
                j = temp[j - 1]
            else:
                j = 0

    return temp

print buildPrefixArray('AAABAAA')