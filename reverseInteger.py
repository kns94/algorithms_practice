class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0:        
            num = str(x)
            rev = int(num[::-1])
            
            if rev >= 2147483648:
                return 0
        
            return rev
        else:
            num = str(x)
            num = num[1:]
            rev = -1 * int(num[::-1])

            if int(rev) <= -2147483647:
                return 0
    
            return rev


import sys
print Solution().reverse(int(sys.argv[1]))