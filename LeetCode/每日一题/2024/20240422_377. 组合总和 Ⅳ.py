#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240422_377. 组合总和 Ⅳ.py
# @Author  ：Lin
# @Date    ：2024/4/22 11:52


"""给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。



示例 1：

输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
示例 2：

输入：nums = [9], target = 3
输出：0


提示：

1 <= nums.length <= 200
1 <= nums[i] <= 1000
nums 中的所有元素 互不相同
1 <= target <= 1000


进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？"""
from functools import cache
from typing import List
# 无重复
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#
#         def dfs(i, c):
#             if i < 0:
#                 return 1 if c == 0 else 0
#             elif c < nums[i]:
#                 return dfs(i-1, c)
#             return dfs(i-1, c) + dfs(i, c - nums[i])
#         return dfs(n-1, target)

# 超时
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(c):
            if c <= 0:
                return 1 if c == 0 else 0
            return sum([dfs(c-nums[_]) for _ in range(n)])
        return dfs(target)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(target + 1):
            for num in nums:
                if i >= num:
                    dp[i] = dp[i] + dp[i-num]
        return dp[target]

s = Solution()
s.combinationSum4(nums = [1,2,3], target = 4)
















