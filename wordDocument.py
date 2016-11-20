class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        pattern = list(pattern)
        string = str.split()

        if len(pattern) != len(string):
            return False

        identified = {}

        for i in range(len(pattern)):
            if pattern[i] in identified:
                if identified[pattern[i]] != string[i]:
                    return False
            else:
                if string[i] not in identified.values():
                    identified[pattern[i]] = string[i]
                else:
                    return False

        return True

print Solution().wordPattern('abba', "dog dog dog dog") 