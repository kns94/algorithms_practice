class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return '1'

        if n == 2:
            return '11'
        
        previous = '11'

        for i in range(2, n):
            j = 0
            ans = ''
            count = 1
            while j < len(previous) - 1:
                if previous[j] == previous[j+1]:
                    count += 1
                else:
                    say = str(count)+previous[j]
                    ans += say
                    count = 1
                j += 1
            say = str(count)+previous[j]
            ans += say
            previous = ans
        return str(ans) 

print Solution().countAndSay(5)

