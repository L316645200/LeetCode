#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231005_309. 买卖股票的最佳时机含冷冻期.py
# @Author: Lin
# @Date  : 2023/10/9 10:53

"""给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



示例 1:

输入: prices = [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
示例 2:

输入: prices = [1]
输出: 0


提示：

1 <= prices.length <= 5000
0 <= prices[i] <= 1000"""
from typing import List
"""思路
根据题目描述，一共会有三种状态， 1、持有股票，记为dp[i][0]； 2、不持有股票，且不在冷冻期dp[i][1]； 3、不持有股票，且在冷冻期dp[i][2]；

如何进行状态转移呢？在第i天时
对于dp[i][0],可以是在第i-1天持有股票，在第i天不进行操作，状态即为dp[i-1][0]；也可以是第i天买入的，即在i-1天不持有股票且不在冷冻期,状态为dp[i-1][1]+prices[i],状态转移方程为: dp[i][0]=max(dp[i−1][0],dp[i−1][1]−prices[i])dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])dp[i][0]=max(dp[i−1][0],dp[i−1][1]−prices[i])
对于dp[i][1],可以是在第i-1天状态的延续,状态即dp[i-1][1];也可以是第i-1天处于冷冻期,第i天时自动解封,状态为dp[i-1][2],状态转移方程为: dp[i][1]=max(dp[i−1][1],dp[i−1][2]) dp[i][1] = max(dp[i-1][1], dp[i-1][2])dp[i][1]=max(dp[i−1][1],dp[i−1][2])
对于dp[i][2],肯定是在第i-1天时卖出股票，第i天时才会是冷冻期,状态转移方程为: dp[i][2]=dp[i−1][0]+prices[i]dp[i][2] = dp[i-1][0] + prices[i]dp[i][2]=dp[i−1][0]+prices[i] 那么最终的答案即为 max(dp[n-1][1], dp[n-1][2]);因为最后一天持有股票是没有意义的，所有排除在外； 注：第0天的时候，即边界情况为dp[i]=[−prices[0],0,0] dp[i] = [-prices[0],0,0]dp[i]=[−prices[0],0,0]

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][0]手上持有股票的最大收益,dp[i][1]手上不持有股票，并且不在冷冻期中的累计最大收益,dp[i][2]处于冷冻期中的累计最大收益
        dp = [[-prices[0], 0, 0] for i in range(n)]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])
            dp[i][2] = dp[i-1][0] + prices[i]
        return max(dp[n-1])

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][0]手上持有股票的最大收益,dp[i][1]手上不持有股票，并且不在冷冻期中的累计最大收益,dp[i][2]处于冷冻期中的累计最大收益
        hold, not_hold, freeze = -prices[0], 0, 0
        for i in range(1, n):
            hold = max(hold, not_hold - prices[i])
            not_hold = max(not_hold, freeze)
            freeze = hold + prices[i]
        return max(not_hold, freeze)


s = Solution()
s.maxProfit(prices = [1,4,2])