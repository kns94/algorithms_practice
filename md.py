from collections import deque

class Solution:

    compared = {}

    def compare_string(string, bank):

        next_mutation = []

        for element in bank:

            if (string, element) in compared:
                hamming_distance = compared[(string, element)]

            elif (element, string) in compared:
                hamming_distance = compared[(element, string)]
                
            else:
                hamming_distance = sum(ch1 != ch2 for ch1, ch2 in zip(string, element))
                compared[(string, element)] = hamming_distance

            if hamming_distance == 1:
                next_mutation.append(element)

        return next_mutation

    def minMutation(self, start, end, bank):

        if start == end:
            return 0

        if end not in bank:
            return -1 

        start_possibilities = compare_string(start, bank)
        if len(start_possibilities) == 0:
            return -1

        graph = {}
        graph[start] = start_possibilities
        bank = [b for b in bank if b != start]
        test_bank = bank

        temp = deque()
        temp += [(ele, 1) for ele in start_possibilities]
        already = []

        while len(temp) > 0:
                element, distance = temp.popleft()
                already.append(element)

                poss = compare_string(element, test_bank)
                test_bank = [ele for ele in test_bank if ele not in already]

                if len(poss) != 0:
                    if end in poss:
                        return distance + 1
                    else:
                        #graph[element] = poss
                        temp += [(sp, distance + 1) for sp in poss if sp not in already]

        '''
        all_values = []
        for val in graph.values():
            all_values += val 
        if end not in all_values:
            return -1

        visited = set()
        stack = deque()
        for poss in start_possibilities:
            stack.append((poss, 1))
        visited.add(start)

        while len(stack) > 0:
            vertex, distance = stack.popleft()

            if vertex not in visited:
                visited.add(vertex)

                if vertex in graph:
                    next_mutation = graph[vertex]
                    if end in next_mutation:
                        return (distance + 1)
                    else:
                        stack += [(item, distance + 1) for item in next_mutation if item not in visited]
        '''
        return -1

#print findMutationDistance('AAAAAAAA', 'GGAAAAAA', ['GAAAAAAA', 'AAGAAAAA', 'AAAAGAAA', 'GGAAAAAA'])
#print findMutationDistance('AAAAAAAA', 'GAAAAATC', ['GAAAAAAA', 'GGAAAAAA', 'AAAAGAAA', 'GAAAAATC'])
print findMutationDistance('AAAAAAAA', 'CAAAAATC', ['GAAAAAAA', 'GGAAAAAA', 'AAAAGAAA', 'GGAAAAAG', 'GAAAAATA', 'AAAAAAAT', 'GAAAAATC', 'CAAAAATC'])