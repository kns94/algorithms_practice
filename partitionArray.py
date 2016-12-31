class Solution(object):
        
    def partition(self, arr, target):

        if target == 0:
            return True
            
        if len(arr) == 0 and target != 0:
            return False
    
        if arr[-1] > target:
            return self.partition(arr[:-1], target)
            
        return self.partition(arr[:-1], target - arr[-1]) or self.partition(arr[:-1], target - arr[-1])

    def allEqual(self, arr):
        """
        Checking if all elements are equal in the array
        """
        all_equal = True
        first = arr[0]

        for i in range(1, len(arr)):
            if arr[i] != first:
                all_equal = False
                break
        return all_equal

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums = sorted(nums)

        if len(nums) == 0:
            return True
            
        total = sum(nums)    

        if total % 2 != 0:
            return False

        if self.allEqual(nums):
            if total/nums[0] % 2 == 0:
                return True
            else:
                return False
            
        return self.partition(nums, total/2)

arr = [5, 6, 7, 8, 8, 8, 9, 10, 11]
#arr = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
print Solution().canPartition(arr)
        
        