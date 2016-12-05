class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        xor = 0

        for num in nums:
            xor ^= num 

        set_bit = xor & ~(xor-1)

        first = 0
        second = 0
        for num in nums:
            if num & set_bit:
                first ^= num 
            else:
                second ^= num

        return [first, second]

print Solution().singleNumber([1,2,3,3])