import sys

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num == 0:
            return 0

        dr = num%9
        if dr == 0:
            return 9
        else:
            return dr

if __name__ == '__main__':
    sol = Solution()
    print sol.addDigits(int(sys.argv[1]))