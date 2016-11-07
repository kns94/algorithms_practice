class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hash_map = {}
        
        for i in range(0, len(nums)):
            hash_map[nums[i]] = i
            
        print hash_map

        for i in range(0, len(nums)):
            one = nums[i]
            two = target - nums[i]
            

            if two in hash_map:
                if i != hash_map[two]:
                    return [i, hash_map[two]]

if __name__ == "__main__":
    solver = Solution()
    print solver.twoSum([3,2,4], 6)
