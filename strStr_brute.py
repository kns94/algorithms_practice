class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if len(needle) == 0:
            return 0
            
        if len(haystack) == 0:
            return -1
        
        i = 0
        while i < len(haystack) - len(needle) + 1:
            #print i
            #print haystack[i: i + len(needle)]
            if haystack[i: i + len(needle)] == needle:
                return i
            i += 1
        return -1

print Solution().strStr('baa','aa')