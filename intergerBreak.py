class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 2:
            return 1
        if n == 3:
            return 2

        dp = {}
        dp[2] = 2 
        dp[3] = 3 
        dp[4] = 4

        multiplier = [2, 3, 4]
        m = 0

        for i in range(5, n+1):
            dp[i] = dp[i-multiplier[m%3]] * multiplier[m%3] 
            m += 1
        return dp[n]

print Solution().integerBreak(7)