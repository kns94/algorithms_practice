class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        #self.array = []
        self.sumArray = []
        prev_sum = 0
        
        for num in nums:
            #self.array.append(num)
            prev_sum += num 
            self.sumArray.append(prev_sum)
            
    def sumRange(self, i, j):
        """m
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        
        return self.sumArray[j+1] - self.sumArray[i]