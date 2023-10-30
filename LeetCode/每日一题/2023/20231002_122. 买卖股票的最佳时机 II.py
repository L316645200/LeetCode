#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231002_122. 买卖股票的最佳时机 II.py
# @Author: Lin
# @Date  : 2023/10/7 10:23

"""给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。



示例 1：

输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
     总利润为 4 + 3 = 7 。
示例 2：

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     总利润为 4 。
示例 3：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0 。


提示：

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104"""
from typing import List

# 动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, -prices[0]] for _ in range(n)]
        # dp[i][j] i标记天数，j[0]表示持有现金,j[1]表示持有股票
        # 状态转移方程 dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[n-1][0]


# 贪心
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        """贪心的角度考虑我们每次选择贡献大于0的区间即能使得答案最大化"""
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i-1])
        return res




s = Solution()
s.maxProfit(prices = [7,1,5,3,6,4])
