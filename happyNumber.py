import sys

class Solution(object):

    def calculateSum(self, n):
        listnum = map(int, str(n))
        squared_sum = 0

        for num in set(listnum):
            squared_sum += listnum.count(num)*(num * num) 

        return squared_sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True

        already = []
        squared_num = n

        while squared_num != 1:
            squared_num = self.calculateSum(squared_num)
            if squared_num in already:
                return False
            else:
                already.append(squared_num)

        return True

if __name__ == "__main__":
    solver = Solution()
    print solver.isHappy(int(sys.argv[1]))