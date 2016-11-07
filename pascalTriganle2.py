class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1,1]

        vals = [1,1]
        #vals = nums.split(',')  

        for index in range(2, rowIndex + 1):
            prev = vals[0]
            for j in range(1, len(vals)):
                current = vals[j]
                vals[j] = prev + current
                prev = current
            vals.append(1)

        #nums = ','.join([v for v in vals])
        return vals

import sys
print Solution().getRow(int(sys.argv[1]))