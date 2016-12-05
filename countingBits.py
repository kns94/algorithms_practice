class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        bits = [0, 1]
        parsed = {0: 0, 1:1}
        
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]

        for i in range(2, num + 1):
            if i%2 == 0:
                if i/2 in parsed:
                    bits.append(parsed[i/2])
                    parsed[i] = parsed[i/2]
            else:
                if i - 1 in parsed:
                    bits.append(parsed[i-1] + 1)
                    parsed[i] = parsed[i - 1] + 1

        return bits 

print Solution().countBits(4)