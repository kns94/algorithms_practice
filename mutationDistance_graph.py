import operator
from itertools import imap

already_compared = {}

def isEditDistanceOne(s1, s2):
 
    # Find lengths of given strings
    m = len(s1)
    n = len(s2)
 
    # If difference between lengths is more than 1,
    # then strings can't be at one distance
    if abs(m - n) > 1:
        return False
 
    count = 0    # Count of isEditDistanceOne
 
    i = 0
    j = 0
    while i < m and j < n:
        # If current characters dont match
        if s1[i] != s2[j]:
            if count == 1:
                return False
 
            # If length of one string is
            # more, then only possible edit
            # is to remove a character
            if m > n:
                i+=1
            elif m < n:
                j+=1
            else:    # If lengths of both strings is same
                i+=1
                j+=1
 
            # Increment count of edits
            count+=1
 
        else:    # if current characters match
            i+=1
            j+=1
 
    # if last character is extra in any string
    if i < m or j < n:
        count+=1
 
    return count == 1

def findStringDistance(mutation, bank_graph):
    possible_mutations = []
    ne = operator.ne

    for muts in bank_graph:

        if (mutation, muts) not in already_compared:
            hamming_distance = isEditDistanceOne(mutation, muts)
            already_compared[(mutation, muts)] = hamming_distance
        else:
            hamming_distance = already_compared[(mutation, muts)]

        if hamming_distance == True:
            possible_mutations.append(muts)

    return possible_mutations

def findMutationDistance(start, end, bank):

    '''
    '''

    if len(bank) == 0:
        return -1

    if start == end:
        return 0

    if end not in bank:
        return -1

    bank_graph = {}
    vals = []

    for muts in bank:
        possibilities = findStringDistance(muts, bank)
        if len(possibilities) != 0:
            bank_graph[muts] = possibilities
            vals += possibilities

    if end not in vals:
        return -1
    
    start_possibilities = findStringDistance(start, bank)

    if end in start_possibilities:
        return 1

    start_possibilities = [p for p in start_possibilities if p in bank_graph.keys()]

    if len(start_possibilities) == 0:
        return -1

    visited = set()
    stack = []
    for possibility in start_possibilities:
        stack.append((possibility, 1))
    visited.add(start)

    while len(stack) > 0:
        #print visited
        vertex, dist = stack.pop()

        if vertex not in visited:
            if vertex in bank_graph:
                visited.add(vertex)

                if end in bank_graph[vertex]:
                    return dist + 1

                stack += [(item, dist + 1) for item in bank_graph[vertex] if item not in visited and item in bank_graph]
                #del bank_graph[vertex]

    return -1

#print findMutationDistance('AAAAAAAA', 'GGAAAAAA', ['GAAAAAAA', 'AAGAAAAA', 'AAAAGAAA', 'GGAAAAAA'])
#print findMutationDistance('AAAAAAAA', 'GAAAAATC', ['GAAAAAAA', 'GGAAAAAA', 'AAAAGAAA', 'GAAAAATC'])
print findMutationDistance('AAAAAAAA', 'CAAAAATC', ['GAAAAAAA', 'GGAAAAAA', 'AAAAGAAA', 'GAAAAATC', 'GGAAAAAG', 'GAAAAATA', 'AAAAAAAT', 'GAAAAATC', 'CAAAAATC'])