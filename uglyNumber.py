class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num == 1:
            return True


        if num < -2147483647:
            return False

        if num > 2147483648:
            return False

        while num != 1:

            if num % 2 == 0:
                num = num/2

            if num % 3 == 0:
                num = num/3

            if num % 5 == 0:
                num = num/5


            if num == 1:
                return False
            else:
                if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
                    return True

if __name__ == "__main__":
    import sys
    print Solution().isUgly(int(sys.argv[1]))