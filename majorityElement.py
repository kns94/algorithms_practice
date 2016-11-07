class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        if length == 1 or length == 2:
            return nums[0]

        count = {}

        for num in set(nums):
            if nums.count(num) > length/2:
                return num

if __name__ == '__main__':
    solver = Solution()
    print solver.majorityElement([1,2,3,2,2,3,3,3,3])
