class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        wc = {}
        for char in s:
            try:
                wc[char] += 1
            except KeyError:
                wc[char] = 1

        count = 0
        for times in wc.values():
            if times % 2 == 0:
                count += times
            else:
                count += times - 1

        if count == len(s):
            return count
        else:
            return count + 1

if __name__ == "__main__":
    solver = Solution()
    import sys
    print solver.longestPalindrome(sys.argv[1])