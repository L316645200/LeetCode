#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231024_1155. 掷骰子等于目标和的方法数.py
# @Author: Lin
# @Date  : 2023/10/24 10:56

"""这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。

给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 kn 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。

答案可能很大，你需要对 109 + 7 取模 。



示例 1：

输入：n = 1, k = 6, target = 3
输出：1
解释：你扔一个有 6 个面的骰子。
得到 3 的和只有一种方法。
示例 2：

输入：n = 2, k = 6, target = 7
输出：6
解释：你扔两个骰子，每个骰子有 6 个面。
得到 7 的和有 6 种方法：1+6 2+5 3+4 4+3 5+2 6+1。
示例 3：

输入：n = 30, k = 30, target = 500
输出：222616187
解释：返回的结果必须是对 109 + 7 取模。


提示：

1 <= n, k <= 30
1 <= target <= 1000"""


# 动态规划
"""动态规划转移方程
记f(i,j)表示使用i个骰子且数字之和为j的方案数，
可以枚举最后一个骰子 的数字，且它的范围为[1,k]
则它的状态转移方程为:
for x in range(1, k+1):
    if j - x >= 0:
        f(i,j) = f(i-1,j-x)
边界条件f(0,0)=1
    """
# n维数组
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for i in range(n + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7

        for i in range(1, n + 1):
            for j in range(1, target+1):
                for x in range(1, k+1):
                    if j - x >= 0:
                        print(i, j)
                        dp[i][j] += dp[i-1][j-x]
        return dp[n][target] % mod

# 二维数组
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for i in range(2)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7

        for i in range(1, n + 1):
            for j in range(1, target+1):
                for x in range(1, k+1):
                    if j - x >= 0:
                        dp[1][j] += dp[0][j-x]
            dp[1], dp[0] = [0 for i in range(target+1)], dp[1]
        return dp[0][target] % mod

# 一维数组
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        mod = 10 ** 9 + 7

        for i in range(1, n + 1):
            for j in range(target, -1, -1):
                dp[j] = 0
                for x in range(1, k+1):
                    if j - x >= 0:
                        dp[j] += dp[j-x]
        return dp[target] % mod


s = Solution()
s.numRollsToTarget(n = 30, k = 30, target = 500)

# s.numRollsToTarget(n = 2, k = 6, target = 7)