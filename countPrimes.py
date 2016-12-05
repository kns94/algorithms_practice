class Solution(object):

    def isPrime(self, n):

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0 or n == 1 or n == 2:
            return 0

        if n == 3:
            return 1

        numbers = [1]*(n-2)
        numPrimes = n - 2
        i = 0

        while i <= int((n-2) ** 0.5):

            if numbers[i] == 1:
                num = i + 2
                if not self.isPrime(num):
                    numPrimes -= 1

                j = i + num
                while j < len(numbers):
                    if numbers[j] != 0:
                        numbers[j] = 0
                        numPrimes -= 1
                    j += num
            i += 1

        return numPrimes


print Solution().countPrimes(100)