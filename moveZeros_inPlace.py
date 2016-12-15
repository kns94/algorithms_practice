"""
Move all zeros in an array to right, keeping other elements same
"""

class Solution:

    def swap(self, arr, i, j):
        """
        Swap two elements in array by index
        """
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        return arr


    def moveZeros(self, arr):
        """
        I will check till a non-zero element is found and swap it. 
        """

        l = 0
        r = len(arr) - 1

        while l < r:
    
            if arr[l] != 0:
                l += 1

            if arr[r] == 0:
                r -= 1

            if arr[l] == 0 and arr[r] != 0:
                arr = self.swap(arr, l, r)
                r -= 1
                l += 1

        return arr

print Solution().moveZeros([1, 0, 1, 0, 1, 0, 0, 1])