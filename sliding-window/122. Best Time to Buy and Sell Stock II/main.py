class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if prices[right] - prices[left] <= 0:
                left += 1
                right += 1
            else:
                max_profit += profit
                left += 1
                right += 1
        return max_profit

        