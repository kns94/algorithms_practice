class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x/10 == 0:
            return True

        rev = 0
        temp = x
        while temp > 0:
            rev = (temp % 10) + (rev * 10)
            temp /= 10

        if x == rev:
            return True
        else:
            return False

print Solution().isPalindrome(1001)