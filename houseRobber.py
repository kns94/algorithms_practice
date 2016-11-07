class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        loot = [0]*len(nums)
        loot[0] = nums[0]
        loot[1] = max(nums[0], nums[1])

        i = 0
        for i in range(2, len(nums)):
            loot[i] = max(loot[i-2] + nums[i], loot[i - 1])

        return loot[len(nums) - 1]          


        #first = 0
        #second = 1
        #loot = 0

        #while first < len(nums) and second < len(nums):

        #    loot += max(nums[first], nums[second])

        #    if nums[first] > nums[second]:
        #        first = first + 2
        #    else:
        #        first = second + 2

        #    second += 1

        #return loot

if __name__ == "__main__":
    print Solution().rob([1,2,3,6,1,5])