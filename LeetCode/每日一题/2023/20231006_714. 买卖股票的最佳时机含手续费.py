#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231006_714. 买卖股票的最佳时机含手续费.py
# @Author: Lin
# @Date  : 2023/10/9 15:24


"""给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。



示例 1：

输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
输出：8
解释：能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
示例 2：

输入：prices = [1,3,7,5,10,3], fee = 3
输出：6


提示：

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104"""
from typing import List

"""根据题目描述，一共会有两种状态， 1、持有股票，记为dp[i][0]； 2、不持有股票dp[i][1]；

如何进行状态转移呢？在第i天时
对于dp[i][0],可以是在第i-1天持有股票，在第i天不进行操作，状态即为dp[i-1][0]；也可以是第i天买入的，即在i-1天不持有股票，状态为dp[i-1][1]+prices[i],
状态转移方程为: dp[i][0]=max(dp[i−1][0],dp[i−1][1]−prices[i])
对于dp[i][1],可以是在第i-1天状态的延续,状态即dp[i-1][1];也可以是第i-1天持有股票,第i天时卖出股票,状态为dp[i-1][0] + prices[i] - fee,
状态转移方程为: dp[i][1]=max(dp[i-1][0] + prices[i] - fee, dp[i-1][1])
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[-prices[0], 0] for i in range(n)]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][0] + prices[i] - fee, dp[i-1][1])
        return dp[n-1][1]

# 因为第i天的状态只与第i-1相关，则可以优化空间dp[i]为两个变量

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, not_hold = -prices[0], 0
        for i in range(1, len(prices)):
            hold = max(hold, not_hold - prices[i])
            not_hold = max(hold + prices[i] - fee, not_hold)
        return not_hold

# 方法二：贪心算法
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        profit = 0
        buy = prices[0] + fee
        for i in range(1, n):
            if buy > prices[i] + fee:
                buy = prices[i] + fee
            elif buy < prices[i]:
                profit += prices[i] - buy
                buy = prices[i]
        return profit

s = Solution()
s.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2)

