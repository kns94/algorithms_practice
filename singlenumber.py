class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numbers = {}

        for num in nums:
            if num in numbers:
                numbers.pop(num, None)
            else:
                numbers[num] = 1

        return numbers.keys()[0]


if __name__ == '__main__':
    sol = Solution()
    print sol.singleNumber([1,1,2,2,3])