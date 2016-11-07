class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if prices == []:
            return 0

        profit = 0
        prev = prices[0]
        current = prices[0]

        for i in range(1, len(prices)):

            if prices[i] < prev:
                prev = prices[i]   
            else:
                if profit < prices[i] - prev:
                    current = prices[i]
                    profit = current - prev

        return profit

if __name__ == "__main__":
    print Solution().maxProfit([])