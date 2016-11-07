class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        number = 0

        if len(s) == 1:
            return hash_map[s]

        i = 0
        while i < len(s):

            if i != len(s) - 1: 
                if hash_map[s[i]] < hash_map[s[i + 1]]:
                    number += hash_map[s[i + 1]] - hash_map[s[i]]
                    i += 1
                else:
                    number += hash_map[s[i]]
            else:
                if hash_map[s[i]] <= hash_map[s[i - 1]]:
                    number += hash_map[s[i]]

            i += 1

        return number

if __name__ == "__main__":
    import sys
    solver = Solution()
    print solver.romanToInt(sys.argv[1])