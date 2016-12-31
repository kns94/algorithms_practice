class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int

        The code will run in a loop and I would subtract values from the total sum. If there are sufficient coins for kth row,
        I would increment the num_rows count

        """
        if n == 0:
            return 0

        new = 2 * n 
        root = int(new ** (0.5))

        current_sum = (root)*(root + 1)/2
        if n < current_sum:
            return root
        else:
            return root + 1