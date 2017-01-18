class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = '121'
        end = '112111'
        total = start + end 
        times= n / len(total)
        total = total * (times + 1)
        total = total[:n]
        print total
        return len([i for i in total if i == '1'])

print Solution().magicalString(1)