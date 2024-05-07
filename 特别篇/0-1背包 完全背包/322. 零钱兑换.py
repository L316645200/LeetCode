#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：322. 零钱兑换.py
# @Author  ：Lin
# @Date    ：2024/4/25 15:42
"""完全背包"""
from functools import cache


def unbounded_knapsack(capacity, w, v):
    n = len(w)

    @cache
    def dfs(i, c):
        if i < 0:
            return 0
        elif c < w[i]:
            return dfs(i-1, c)
        return max(dfs(i-1, c), dfs(i, c - w[i]) + v[i])
    return dfs(n-1, capacity)


"""给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。



示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0


提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104"""
from typing import List

# 回溯
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        m = 10 ** 4 + 1
        @cache
        def dfs(i, c):
            if i < 0:
                return 0 if c == 0 else m
            elif c < coins[i]:
                return dfs(i-1, c)
            return min(dfs(i-1, c), dfs(i, c - coins[i]) + 1)

        r = dfs(n -1, amount)
        return r if r != m else -1

# 递推
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        m = 10 ** 4 + 1

        f = [[m] * (amount + 1) for _ in range(n+1)]
        f[0][0] = 0
        for c in range(amount + 1):
            for i, x in enumerate(coins):
                if c < x:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = min(f[i][c], f[i+1][c-x] + 1)
        print(f)


# 递推（空间优化）
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = 10 ** 4 + 1

        f = [m] * (amount + 1)
        f[0] = 0
        for x in coins:
            for c in range(x, amount + 1):
                f[c] = min(f[c], f[c-x] + 1)
        return f[amount] if f[amount] < m else -1
s = Solution()
s.coinChange(coins = [1, 2, 5], amount = 11)