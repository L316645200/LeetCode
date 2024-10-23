#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：494. 目标和.py
# @Author  ：Lin
# @Date    ：2024/4/24 10:59

"""0-1背包"""
from functools import cache


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

"""给你一个非负整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。



示例 1：

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：

输入：nums = [1], target = 1
输出：1


提示：

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000"""
from functools import cache
from typing import List

"""
设sum(nums)=s
正数和为p
则负数和为p-s
target=p+(p-s)
p=(s+target)/2
"""


# 递归
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target % 2 != 0:
            return 0
        target //= 2
        ans = 0

        def dfs(s, index, size):
            nonlocal ans
            if s == target:
                ans += 1
            elif s > target or index >= size:
                return
            for i in range(index, size):
                dfs(s + nums[i], i + 1, size)

        dfs(0, 0, len(nums))
        return ans


# 记忆化搜索
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2 != 0:
            return 0
        target = target // 2

        @cache
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            elif c < nums[i]:
                return dfs(i-1, c)
            return dfs(i-1, c) + dfs(i-1, c - nums[i])
        return dfs(len(nums)-1, target)


# 递推
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2 != 0:
            return 0
        target = target // 2
        n = len(nums)

        f = [[0] * (target+1) for _ in range(n+1)]
        f[0][0] = 1
        for i, x in enumerate(nums):
            for c in range(target+1):
                if c < x:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = f[i][c] + f[i][c-x]
        return f[-1][-1]


# (递推)（空间优化）
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2 != 0:
            return 0
        target = target // 2
        n = len(nums)

        f = [[0] * (target+1) for _ in range(2)]
        f[0][0] = 1
        for i, x in enumerate(nums):
            for c in range(target+1):
                if c < x:
                    f[(i+1) % 2][c] = f[i % 2][c]
                else:
                    f[(i+1) % 2][c] = f[i % 2][c] + f[i % 2][c-x]
        return f[n % 2][target]


# (递推)（空间再优化）
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2 != 0:
            return 0
        target = target // 2

        f = [0] * (target+1)
        f[0] = 1
        for x in nums:
            for c in range(target, x - 1, -1):
                f[c] = f[c] + f[c-x]
        return f[target]


s = Solution()
s.findTargetSumWays(nums = [1,1,1,1,1], target = 3)