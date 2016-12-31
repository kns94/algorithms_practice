def stringToNumber(string):
    table = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    val = 0
    for i in string:
        val = table[i] + (val << 2)
    return val

def findMutationDistance(start, end, bank):

    if start == end:
        return 0

    if end not in bank:
        return -1 

    if len(bank) == 0:
        return -1

    start = stringToNumber(start)
    end = stringToNumber(end)

    bank = set(map(stringToNumber, bank))
    stack = [(start, 0)]
    visited = set()

    while len(queue) != 0:
        element, distance = stack.pop(0)
       
        if element == end:
            return distance

        for x in range(8):
            for y in range(4):
                possibility = element ^ (y << (x * 2))

                if possibility in bank and possibility not in visited:
                    visited.add(possibility)
                    stack.append((possibility, distance + 1))
        
    return -1
#print findMutationDistance('AAAAAAAA', 'GGAAAAAA', ['GAAAAAAA', 'AAGAAAAA', 'AAAAGAAA', 'GGAAAAAA'])
#print findMutationDistance('AAAAAAAA', 'GAAAAATC', ['GAAAAAAA', 'GGAAAAAA', 'AAAAGAAA', 'GAAAAATC'])
print findMutationDistance('AAAAAAAA', 'CAAAAATC', ['GAAAAAAA', 'GGAAAAAA', 'AAAAGAAA', 'GGAAAAAG', 'GAAAAATA', 'AAAAAAAT', 'GAAAAATC', 'CAAAAATC'])

