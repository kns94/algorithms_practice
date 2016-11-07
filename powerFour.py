class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        import math

        try:
            ratio = math.log(num)/math.log(4)
        except ValueError:
            return False
            
        return ratio == int(ratio)