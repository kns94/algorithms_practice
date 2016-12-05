class Solution(object):
    
    def add_values(self, result, sub):
        if len(result) == 0:
            result += sub
            return result

        for val in sub:
            #print val
            i = 0
            while i < len(result) and val[0] <= result[i][0]:
                if val[1] == i:
                    break
                i += 1

            #print i
            temp = result[i: len(result)]
            result.append(val)
            result[i] = val
            result[i+1: len(result)] = temp

        #print result
        return result

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []

        result = []
        #result = [None]*len(people)
        people = sorted(sorted(people, key = lambda x:x[1]), key = lambda x:x[0], reverse = True)
        
        while len(people) != 0:
            sub = []
            current = people[0][0]
            while len(people) != 0 and people[0][0] == current:
                sub.append(people[0])
                del people[0]
            result = self.add_values(result, sub)    

        return result

tester = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print Solution().reconstructQueue(tester)

