import math

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0 or n == 1:
            return 0
            
        count5 = 0
        i = 1

        while 1:
            five_power = pow(5,i)

            if five_power <= n:
                count5 += int(n/five_power)
            else:
                break

            i += 1

        return count5

import sys
print Solution().trailingZeroes(int(sys.argv[1]))