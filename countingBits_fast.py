class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]

        bits = [0, 1]

        for i in range(2, num + 1):
            print i
            bits += [(j + 1) for j in bits]
            
        return bits[: num + 1]

print Solution().countBits(64)