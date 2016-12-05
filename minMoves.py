class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        changes = 0
        init = nums[len(nums)/2]

        for n in nums:
            if n != init:
                #print n
                changes += abs(n - init)

        return changes

print Solution().minMoves2([2,1,3,4])
