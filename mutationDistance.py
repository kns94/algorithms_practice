def findStringDistance(mutation, bank):
    possible_mutations = []

    for muts in bank:
        hamming_distance = sum(ch1 != ch2 for ch1, ch2 in zip(mutation, muts))

        if hamming_distance == 1:
            possible_mutations.append(muts)

    return possible_mutations

def findMutationDistance(start, end, bank):

    '''
    '''
    if start == end:
        return 0

    if end not in bank:
        return -1

    bank = [b for b in bank if b != start]
    steps = 0

    while start != end:
        possible_mutations = findStringDistance(start, bank)

        if len(possible_mutations) == 0:
            return -1

        if len(possible_mutations) == 1:
            start = possible_mutations[0]
            bank = [b for b in bank if b != start]
        else:
            if end in possible_mutations:
                return (steps + 1)
            
            for possibility in possible_mutations:
                bank = [b for b in bank if b != possibility]
                sub_steps = findMutationDistance(possibility, end, bank)
                if sub_steps != -1:
                    return (steps + sub_steps + 1)

        steps += 1

    return steps

#print findMutationDistance('AAAAAAAA', 'AAAAAATT', ['AAAAAAAA', 'AAAAAATT', 'AAAAAAAT', 'AAAAATTT'])
print findMutationDistance('AAAAAAAA', 'GGAAAAAA', ['GAAAAAAA', 'AAGAAAAA', 'AAAAGAAA', 'GGAAAAAA'])