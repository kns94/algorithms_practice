class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        '''
        count = 0

        for num in nums:
            if num != val:
                count += 1

        return count
        '''

        if len(nums) == 0:
            return 0

        j = 0

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
       
        return j
        #return len(nums)
 

if __name__ == "__main__":
    print Solution().removeElement([3,2,2,3], 3)