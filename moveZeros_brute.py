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

        for i in range(len(arr) - 1):
            j = i 
            if arr[i] == 0:
                while j < len(arr) and arr[j] == 0:
                    j += 1
                
                if j < len(arr):
                    arr = self.swap(arr, i, j)

        return arr

print Solution().moveZeros([1, 0, 1, 0, 1])