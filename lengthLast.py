class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
            
        rev = s[::-1]
        count = 0
        start = False
        
        for i in range(len(rev)):
            if not start:
                if rev[i] != ' ' and len(rev[i]) > 0:
                    #print s[i] == ' '
                    count += 1
                    start = True
            else:
                if rev[i] != ' ' and len(rev[i]) > 0:
                    count += 1
                else:
                    break
                
        return count

print Solution().lengthOfLastWord(' ')