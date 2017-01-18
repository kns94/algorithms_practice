class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = [1]*len(nums)

        prev = 1
        for i in range(1, len(nums)):
            out[i] = nums[i - 1] * prev
            prev = out[i]
   
        prev = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            out[i] = out[i] * prev
            prev = prev * nums[i]

        return out
        
print Solution().productExceptSelf([5, 2, 3, 6])