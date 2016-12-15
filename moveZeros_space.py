"""
Move all zeros in an array to right, keeping other elements same
"""

class Solution:

    def moveZeros(self, arr):
        """
        I will check till a non-zero element is found and swap it. 
        """

        non_zero =[]
        zero = []

        for i in range(len(arr)):
            if arr[i] != 0:
                non_zero.append(arr[i])
            else:
                zero.append(arr[i])
        return non_zero + zero

print Solution().moveZeros([1, 0, 1, 0, 1])