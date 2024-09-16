"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
import sys


def maximum_profit_time_limit_exceeded(price):
    profit_max = -sys.maxsize
    n = len(price)
    for i in range(n-1, -1, -1):
        for j in range(i, -1, -1):
            profit = price[i] - price[j]
            profit_max = max(profit, profit_max)
    return max(profit_max, 0)


def maximum_profit(prices):
    min_stock = prices[0]
    profit = 0
    for price in prices:
        min_stock = min(min_stock, price)
        profit = max(profit, price - min_stock)
    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maximum_profit(prices))
