"""
Find maximum sum of adjacent elements in an array
"""

class Solution:

    def adjacentSum(self, arr):
        """
        Will be using a dynamic programming approach here to decide if that particular element would become part of the sum or not
        """

        '''
        If the array contains only one element, return the same element
        '''
        if len(arr) == 1:
            return arr[0]

        '''
        If the array contains two elements, return the largest
        '''
        if len(arr) == 2:
            return max(arr[0], arr[1])

        '''
        Saving two numbers
        '''
        first, second = arr[0], max(arr[0], arr[1])

        for i in range(2, len(arr)):
            '''
            Memoization to fill the output array with maximum sum till that value
            '''
            temp = second
            second = max(arr[i] + first, second)
            first = temp

        return second

print Solution().adjacentSum([1, 0, 3, 9, 2, 10])