import sys

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        length = len(s)
        if length == 0:
            return True

        hash_table = {}

        for i in range(0,length/2):
            if s[i] in hash_table:
                if hash_table[s[i]] != t[i]:
                  return False
            else:
                hash_table[s[i]] = t[i]

            if s[length - i - 1] in hash_table:
                if hash_table[s[length - i - 1]] != t[length - i - 1]:
                    return False
            else:
                hash_table[s[length - i - 1]] = t[length - i - 1]

        if length % 2 != 0:
            if s[length/2] in hash_table:
                if hash_table[s[length/2]] != t[length/2]:
                    return False
            else:
                hash_table[s[length/2]] = t[length/2]

        '''
        Now check if any value is repreated twice
        '''

        keylength = len(set(hash_table.keys()))
        valuelength = len(set(hash_table.values()))

        if keylength == valuelength:
            return True
        else:
            return False

if __name__ == "__main__":
    solver = Solution()
    print solver.isIsomorphic(sys.argv[1], sys.argv[2])