#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：__init__.py.py
# @Author  ：Lin
# @Date    ：2024/4/24 10:35


"""
0-1 背包: 有n个物品，第i个物品的体积为w【i】，价值为v【i】
每个物品之多选一个，求体积和不超过capacity时的最大价值和
"""
from functools import cache
from typing import List
"""0-1背包"""


def zero_one_knapsack(capacity, w, v):
    n = len(w)

    @cache
    def dfs(i, c):
        if i < 0:
            return 0
        elif c < w[i]:
            return dfs(i-1, c)
        return max(dfs(i-1, c), dfs(i-1, c - w[i]) + v[i])

    return dfs(n-1, capacity)



"""
目标和
设正数和为p
总和为s
则负数和为p-s
t = p + (p-s)
p = (t+s)//2
因为p是整数，则t+s是偶数
且t+s大于等于0
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target % 2 == 1 or target < 0:
            return 0
        target //= 2
        n = len(nums)

        @cache
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            elif c < nums[i]:
                return dfs(i-1, c)
            return dfs(i-1, c) + dfs(i-1, c - nums[i])
        return dfs(n-1, target)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target % 2 == 1 or target < 0:
            return 0
        target //= 2
        n = len(nums)

        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i, x in enumerate(nums):
            for c in range(target+1):
                if c < x:
                    dp[i+1][c] = dp[i][c]
                else:
                    dp[i+1][c] = dp[i][c] + dp[i][c-x]
        return dp[n][target]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target % 2 == 1 or target < 0:
            return 0
        target //= 2
        n = len(nums)

        dp = [[0] * (target+1) for _ in range(2)]
        dp[0][0] = 1
        for i, x in enumerate(nums):
            for c in range(target+1):
                if c < x:
                    dp[(i+1)%2][c] = dp[i%2][c]
                else:
                    dp[(i+1)%2][c] = dp[i%2][c] + dp[i%2][c-x]
        return dp[n%2][target]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target % 2 == 1 or target < 0:
            return 0
        target //= 2

        dp = [0] * (target+1)
        dp[0] = 1
        for x in nums:
            for c in range(target, x-1, -1):
                dp[c] = dp[c] + dp[c-x]
        return dp[-1]

s = Solution()
s.findTargetSumWays(nums = [1,1,1,1,1], target = 3)




"""完全背包"""

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


















