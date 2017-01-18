import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums 

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        if len(self.nums) == 0:
            return []

        result = self.nums[:]
        for i in range(len(result) - 1, -1, -1):
            j = random.randrange(0, i + 1)
            result[i], result[j] = result[j], result[i]
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
obj = Solution([0,-12893,128384])
print obj.shuffle()
print obj.shuffle()
print obj.shuffle()
print obj.shuffle()
#print obj.reset()