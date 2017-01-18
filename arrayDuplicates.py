class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Approach: Will conver the array index to negative here, and if the index is already negative the same would be stored in resultant array
        """

        duplicates = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                duplicates.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1

        return duplicates

print Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])