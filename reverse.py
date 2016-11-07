class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        result = list(s)
        for i in xrange(l/2):
            result[i] = s[l-i-1]
            result[l-i-1] = s[i]
        result = ''.join(result)
        return result
        
if __name__ == "__main__":
    ans = Solution()
    print ans.reverseString('test')