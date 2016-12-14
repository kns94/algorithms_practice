def buildPrefixArray(string):

    temp = [0] * len(string)
    temp[0] = 0
    i = 1
    l = 0

    while i < len(string):
        if string[i] == string[l]:
            temp[i] = l + 1
            i += 1
            l += 1
        else:
            if j > 0:
                j = temp[j - 1]
            else:
                j = 0

    return temp

print buildPrefixArray('AAABAAA')