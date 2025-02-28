#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250116_3095. 或值至少 K 的最短子数组 I[easy].py
# @Author  ：Lin
# @Date    ：2025/1/16 9:22
"""给你一个 非负 整数数组 nums 和一个整数 k 。

如果一个数组中所有元素的按位或运算 OR 的值 至少 为 k ，那么我们称这个数组是 特别的 。

请你返回 nums 中 最短特别非空
子数组
的长度，如果特别子数组不存在，那么返回 -1 。



示例 1：

输入：nums = [1,2,3], k = 2

输出：1

解释：

子数组 [3] 的按位 OR 值为 3 ，所以我们返回 1 。

注意，[2] 也是一个特别子数组。

示例 2：

输入：nums = [2,1,8], k = 10

输出：3

解释：

子数组 [2,1,8] 的按位 OR 值为 11 ，所以我们返回 3 。

示例 3：

输入：nums = [1,2], k = 0

输出：1

解释：

子数组 [1] 的按位 OR 值为 1 ，所以我们返回 1 。



提示：

1 <= nums.length <= 50
0 <= nums[i] <= 50
0 <= k < 64"""
from functools import reduce
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = n + 1
        for i in range(n):
            for j in range(i, n):
                if reduce(lambda x, y: x | y, nums[i:j+1]) >= k:
                   res = min(res, j - i + 1)
        return res if res < n + 1 else -1

s = Solution()
s.minimumSubarrayLength(nums = [16,1,2,20,32], k = 45)

