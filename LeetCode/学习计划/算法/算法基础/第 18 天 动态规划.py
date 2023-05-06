#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 18 天 动态规划.py
# @Author: Lin
# @Date  : 2022/8/22 15:54

# 72. 编辑距离
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 示例 1：
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成
import functools
from typing import List
# dp[i, j]
# 插入一个字符，即在word1插入一个字符，使word1[i]==word2[j],
# 即dp[i-1][j] + 1
# 删除一个字符，即在word1删除一个字符，等价在word2中插入一个字符，使word1[i]==word2[j],
# 即dp[i][j-1] + 1
# 替换一个字符，即在dp[i-1][j-1]的基础上各插入一个字符，使word1[i]==word2[j],
# 即dp[i-1][j-1] + 1，如果word1[i]==word2[j]本就成立，则dp[i-1][j-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1) + 1, len(word2) + 1

        dp = [[max(i, j) for i in range(n2)] for j in range(n1)]

        for i in range(1, n1):
            for j in range(1, n2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] - 1) + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[n1-1][n2-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)

        return D[n][m]


s = Solution()
s.minDistance(word1 = "horse", word2 = "ros")


# 322. 零钱兑换
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
# 你可以认为每种硬币的数量是无限的。
# 示例 1：
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：
# 输入：coins = [2], amount = 3
# 输出：-1
# 示例 3：
# 输入：coins = [1], amount = 0
# 输出：0
# 提示：
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)  # 保存函数结果
        def dp(rem) -> int:
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1: return 0
        return dp(amount)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


s = Solution()
s.coinChange(coins = [2], amount = 3)



#
# 343. 整数拆分
# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
# 返回 你可以获得的最大乘积 。
# 示例 1:
# 输入: n = 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 示例 2:
# 输入: n = 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 提示:
# 2 <= n <= 58


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n+1):
            for j in range(1, i//2 + 1):
                print(dp[i], dp[i-j] * j, (i - j) * j)
                dp[i] = max(dp[i], dp[i-j] * j, (i - j) * j)
            print(dp)
        return dp[n]


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = max(dp[i-2] * 2, (i - 2) * 2, dp[i-3] * 3, (i - 3) * 3)
        return dp[n]


class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        quotient, remainder = divmod(n, 3)

        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        elif remainder == 2:
            return 3 ** quotient * 2


s = Solution()
s.integerBreak(3)








































