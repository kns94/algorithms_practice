class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0

        for num in nums:
            res ^= num 
            print res

        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.singleNumber([1,2,3,1,2])
 