class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        ''' Solve it with dynamic programming.
        '''
        couldBreak = [False] * len(s)

        for breakAfterCurrent in xrange(len(s)):
            if s[: breakAfterCurrent+1] in dict:
                # The substring from beginning to here is in the dict.
                # We can make the substring with zero break.
                couldBreak[breakAfterCurrent] = True
                continue

            # Otherwise, we will try to check, whether this substring
            # s[:breakAfterCurrent+1] could be composed by a breakable
            # head and a tail, which is in the dict.
            for preBreak in xrange(breakAfterCurrent):
                if couldBreak[preBreak] == False:
                    # The head is not breakable
                    continue
                elif s[preBreak+1: breakAfterCurrent+1] not in dict:
                    # The tail is not in the dict.
                    continue
                else:
                    # As long as we know it's breakable, no need to
                    # continue the search for current position.
                    couldBreak[breakAfterCurrent] = True
                    break

        return couldBreak[-1]