class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []

        pascal = []
        pascal.append([1])

        if numRows > 1:
            pascal.append([1,1])
            prev = [1, 1]

            for i in range(2, numRows):
                current = [1]
                for j in range(0, len(prev) - 1):
                    current.append(prev[j] + prev[j + 1])
                current.append(1)
                prev = current
                pascal.append(current)
        return pascal

import sys
print Solution().generate(int(sys.argv[1]))