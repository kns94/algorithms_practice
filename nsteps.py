import math

class Solution(object):

    def __init__(self):
        self.memory = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0: 
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        if n in self.memory:
            return self.memory[n]
        else:
            self.memory[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        #return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        #calculation = 1/math.sqrt(5)*pow((1 + math.sqrt(5))/2,n + 1) - 1/math.sqrt(5)*pow((1 - math.sqrt(5))/2,n + 1)
        #return int(calculation)

        return self.memory[n]
 

if __name__ == "__main__":
    import sys
    print Solution().climbStairs(int(sys.argv[1]))