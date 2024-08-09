#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240630_494. 目标和[mid].py
# @Author  ：Lin
# @Date    ：2024/7/1 9:59


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


# 递归搜索 + 保存计算结果 = 记忆化搜索
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        target = sum(nums) - abs(target)
        if target < 0 or target % 2:
            return 0
        target //= 2

        @cache
        def dfs(i: int, x: int) -> int:
            if i == n:
                return 1 if x == target else 0
            if x > target:
                return 0

            return dfs(i + 1, x) + dfs(i + 1, x + nums[i])

        return dfs(0, 0)


# 记忆化搜索翻译下来
# 动态规划
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        target = sum(nums) - abs(target)
        if target < 0 or target % 2:
            return 0
        target //= 2
        n, m = len(nums), target

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m+1):
                if j < nums[i]:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j] + dp[i][j-nums[i]]
        return dp[-1][-1]


# 动态规划空间优化
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        target = sum(nums) - abs(target)
        if target < 0 or target % 2:
            return 0
        target //= 2
        n, m = len(nums), target

        dp = [[0] * (m + 1) for _ in range(2)]
        dp[0][0] = 1

        for i in range(n):
            for j in range(m+1):
                if j < nums[i]:
                    dp[1 - i % 2][j] = dp[i % 2][j]
                else:
                    dp[1 - i % 2][j] = dp[i % 2][j] + dp[i % 2][j-nums[i]]
        return dp[n % 2][-1]


# 动态规划空间再优化
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        target = sum(nums) - abs(target)
        if target < 0 or target % 2:
            return 0
        target //= 2
        n, m = len(nums), target

        dp = [0] * (m + 1)
        dp[0] = 1

        for i, x in enumerate(nums):
            for j in range(m, x - 1, -1):
                dp[j] = dp[j] + dp[j-x]
        return dp[-1]


s = Solution()
r = s.findTargetSumWays(nums = [1,0], target = 1)
print(r)
