def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    left, right = 0, 1
    while right < len(prices):
        profit = prices[right] - prices[left]
        if profit <= 0:
            left = right
        else:
            max_profit = max(max_profit, profit)
        right += 1
    # print(len(prices))
    # print(left, right)
    return max_profit


assert maxProfit([7,1,5,3,6,4]) == 5
assert maxProfit([7,6,4,3,1]) == 0
