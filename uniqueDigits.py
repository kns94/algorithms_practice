class Solution(object):

    def combinatrics(self, n):

        multiplier = 9
        k = 0

        while n > 1:
            multiplier *= (9 - k)
            n -= 1
            k += 1

        return multiplier

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        already = {}
        already[1] = 10

        if n == 1:
            return 10

        for i in range(2, n+1):
            already[i] = already[i - 1] + self.combinatrics(i)

        return already[n]

print Solution().countNumbersWithUniqueDigits(2)