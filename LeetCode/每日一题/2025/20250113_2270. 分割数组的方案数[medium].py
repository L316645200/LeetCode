#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250113_2270. 分割数组的方案数[medium].py
# @Author  ：Lin
# @Date    ：2025/1/13 9:56

"""给你一个下标从 0 开始长度为 n 的整数数组 nums 。
如果以下描述为真，那么 nums 在下标 i 处有一个 合法的分割 ：

前 i + 1 个元素的和 大于等于 剩下的 n - i - 1 个元素的和。
下标 i 的右边 至少有一个 元素，也就是说下标 i 满足 0 <= i < n - 1 。
请你返回 nums 中的 合法分割 方案数。



示例 1：

输入：nums = [10,4,-8,7]
输出：2
解释：
总共有 3 种不同的方案可以将 nums 分割成两个非空的部分：
- 在下标 0 处分割 nums 。那么第一部分为 [10] ，和为 10 。第二部分为 [4,-8,7] ，和为 3 。因为 10 >= 3 ，所以 i = 0 是一个合法的分割。
- 在下标 1 处分割 nums 。那么第一部分为 [10,4] ，和为 14 。第二部分为 [-8,7] ，和为 -1 。因为 14 >= -1 ，所以 i = 1 是一个合法的分割。
- 在下标 2 处分割 nums 。那么第一部分为 [10,4,-8] ，和为 6 。第二部分为 [7] ，和为 7 。因为 6 < 7 ，所以 i = 2 不是一个合法的分割。
所以 nums 中总共合法分割方案受为 2 。
示例 2：

输入：nums = [2,3,1,0]
输出：2
解释：
总共有 2 种 nums 的合法分割：
- 在下标 1 处分割 nums 。那么第一部分为 [2,3] ，和为 5 。第二部分为 [1,0] ，和为 1 。因为 5 >= 1 ，所以 i = 1 是一个合法的分割。
- 在下标 2 处分割 nums 。那么第一部分为 [2,3,1] ，和为 6 。第二部分为 [0] ，和为 0 。因为 6 >= 0 ，所以 i = 2 是一个合法的分割。


提示：

2 <= nums.length <= 105
-105 <= nums[i] <= 105"""
from typing import List


# 分别构造一个前缀和，一个后缀和，遍历数组长度，前缀和比后缀和大的即是合法方案数相加即可
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix, suffix = [nums[0]] * n, [nums[-1]] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
            suffix[n-i-1] = suffix[n-i] + nums[n-i-1]

        return sum([1 for i in range(n-1) if prefix[i] >= suffix[i+1]])


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        suffix = [nums[-1]] * n
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] + nums[i]
        res = prefix = 0
        for i in range(n-1):
            prefix += nums[i]
            if prefix >= suffix[i+1]:
                res += 1
        return res
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n, prefix, suffix = len(nums), 0, sum(nums)
        res = 0
        for i in range(len(nums)-1):
            prefix += nums[i]
            suffix -= nums[i]
            if prefix >= suffix:
                res += 1
        return res


s = Solution()
s.waysToSplitArray(nums = [10,4,-8,7])

