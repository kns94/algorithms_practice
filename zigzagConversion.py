class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s

        arr = [''] * numRows
        down = True
        i = 0
        row = 0

        for i in range(len(s)):
            arr[row] += s[i]

            if row == 0:
                down = True
            if row == numRows - 1:
                down = False

            if down:
                row += 1
            else:
                row -= 1

        return ''.join(arr)

print Solution().convert('paypalishiring', 3)