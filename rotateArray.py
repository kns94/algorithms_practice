class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        temp = [0] * length

        temp[k: ] = nums[: length - k]
        nums[:k] = nums[length - k:]
        nums[k:] = temp[k:]

        return nums

print Solution().rotate([1,2, 3], 1)
        
        