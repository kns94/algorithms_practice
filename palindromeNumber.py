import math

class Solution(object):

    def countDigits(self, x):
        digits = 0

        while x > 0:
            x /= 10
            digits += 1

        return digits

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x/10 == 0:
            return True

        digits = self.countDigits(x)
        if digits % 2 == 0:
            divisor = int(pow(10, digits/2))
            first_half = x / divisor
        else:
            digits -= 1
            divisor = int(pow(10, digits/2))
            first_half = x / (divisor * 10)

        second_half = x % divisor
        reverse = 0
 
        while first_half % 10 == 0:
            first_half /= 10

        #print first_half, second_half
        while second_half:
            digit = second_half % 10
            reverse = digit + (reverse * 10)
            second_half /= 10

        if reverse == first_half:
            return True
        else:
            return False

print Solution().isPalindrome(1)