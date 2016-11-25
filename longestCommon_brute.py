class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        strs.sort(key = lambda s: len(s))
        prefix_length = len(strs[0])
        prefix = ''
        enough = False

        for i in range(prefix_length):
            current = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != current:
                    enough = True
                    break

                if j == len(strs) - 1:
                    prefix += current
            if enough:
                break

        return prefix

print Solution().longestCommonPrefix(['abc', 'cba'])