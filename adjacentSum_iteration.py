"""
Find maximum sum of adjacent elements in an array
"""

class Solution:

    def __init__(self):
        '''
        Initializing array to keep track of sum
        '''
        self.tracker = []

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
        Adding maximum values in the tracking array
        '''
        self.tracker.append(arr[0])
        self.tracker.append(max(arr[1], arr[0]))

        for i in range(2, len(arr)):
            '''
            Memoization to fill the output array with maximum sum till that value
            '''
            self.tracker.append(max(arr[i] + self.tracker[i - 2], self.tracker[i - 1]))

        return self.tracker[-1]