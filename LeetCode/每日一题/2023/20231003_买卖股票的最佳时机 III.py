#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231003_买卖股票的最佳时机 III.py
# @Author: Lin
# @Date  : 2023/10/7 17:12

"""给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



示例 1:

输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2：

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
示例 4：

输入：prices = [1]
输出：0


提示：

1 <= prices.length <= 105
0 <= prices[i] <= 105"""
from typing import List


"""方法一：动态规划
思路与算法
由于我们最多可以完成两笔交易，因此在任意一天结束之后，我们会处于以下五个状态中的一种：
未进行过任何操作；
只进行过一次买操作；
进行了一次买操作和一次卖操作，即完成了一笔交易；
在完成了一笔交易的前提下，进行了第二次买操作；
完成了全部两笔交易。"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0
        for p in prices[1:]:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
        return sell2

# 两笔交易若改成k次交易，可以求k次交易通解
class Solution:
    def maxProfit(self, prices: List[int], k: int = 2) -> int:
        dp = [[-prices[0], 0] for _ in range(k)]
        for p in prices:
            dp[0][0] = max(dp[0][0], -p)
            dp[0][1] = max(dp[0][1], dp[0][0] + p)
            for i in range(1, k):
                dp[i][0] = max(dp[i][0], dp[i-1][1] - p)
                dp[i][1] = max(dp[i][1], dp[i][0] + p)
        return dp[k-1][1]

class Solution:
    def maxProfit(self, prices: List[int], k: int) -> int:
        dp = [[-prices[0], 0] for _ in range(k+1)]
        dp[0] = [0, 0]
        for p in prices[1:]:
            for i in range(1, k+1):
                dp[i][0] = max(dp[i][0], dp[i-1][1] - p)
                dp[i][1] = max(dp[i][1], dp[i][0] + p)
        return dp[k][1]


s = Solution()
# s.maxProfit(prices = [3,3,5,0,0,3,1,4])
res = s.maxProfit(prices = [1,2,3,4,5], k=2)
print(res)



















