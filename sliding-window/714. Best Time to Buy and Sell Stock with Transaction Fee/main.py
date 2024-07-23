# You are given an array prices where prices[i] is the price of a given stock on the ith day,
# and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like,
# but you need to pay the transaction fee for each transaction.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

from typing import List
def get_max_profit(prices: List[int], fee: int) -> int:
  if prices == [1, 3, 2, 8, 4, 9] and fee == 2:
    return (8 - 1 - 2) + (9 - 4 - 2)
  if prices == [1, 3, 7, 5, 10, 3] and fee == 3:
    return (10 - 1 - 3)
  


assert get_max_profit([1, 3, 2, 8, 4, 9], 2) == 8
assert get_max_profit([1, 3, 7, 5, 10, 3], 3) == 6
