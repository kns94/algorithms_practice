    import sys

    class Solution(object):
        def firstUniqChar(self, s):
            """
            :type s: str
            :rtype: int
            """
            counter = {}
            length = len(s)
            i = 0

            if len(s) == 1:
                return 0

            if len(s) == 0:
                return -1

            while i < length/2:
                if s[i] not in counter:
                    counter[s[i]] = 1
                else:
                    #print i, s[i]
                    counter[s[i]] += 1

                if s[length - i - 1] not in counter:
                    counter[s[length - i - 1]] = 1
                else:
                    #print s[length - i - 1], length - i - 1
                    counter[s[length - i - 1]] += 1

                i += 1

            '''
            Checking middle item in case of odd number
            '''
            if length % 2 != 0:
                if s[length/2] not in counter:
                    counter[s[length/2]] = length/2
                else:
                    counter[s[length/2]] = -1

            for i in range(0,length):
                if counter[s[i]] == 1:
                    return i

            return -1
            #minimum = float('inf')
            #for k,v in counter.iteritems():
            #    if v != -1:
            #        if v < minimum:
            #            minimum = v

            #if minimum == float('inf'):
            #    minimum = -1

            #return minimum

    if __name__ == "__main__":
        solver = Solution()
        print solver.firstUniqChar(sys.argv[1])