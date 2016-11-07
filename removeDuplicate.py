class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        i = 0
        while i < len(nums):
            current = nums[i]

            j = i + 1
            while j < len(nums):
                temp = nums[j]
                if temp == current:
                    pass
                else:
                    count += 1
                    nums[count] = temp
                    break
                j += 1
            i = j

        return (count + 1)

print Solution().removeDuplicates([1,2,3])