class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        
        self.nums = nums

        total = 0
        for i in range(len(nums)):
            nums[i] += total
            total = nums[i]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)