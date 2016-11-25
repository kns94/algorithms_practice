class Solution(object):
    def longestCommonPrefix(self, m):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        "Given a list of pathnames, returns the longest common leading component"
        if not m: return ''
        s1 = min(m)
        s2 = max(m)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1