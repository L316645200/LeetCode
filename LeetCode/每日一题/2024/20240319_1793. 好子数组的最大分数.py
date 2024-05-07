#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240319_1793. 好子数组的最大分数.py
# @Author  ：Lin
# @Date    ：2024/3/19 15:39


"""给你一个整数数组 nums （下标从 0 开始）和一个整数 k 。

一个子数组 (i, j) 的 分数 定义为 min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) 。一个 好 子数组的两个端点下标需要满足 i <= k <= j 。

请你返回 好 子数组的最大可能 分数 。



示例 1：

输入：nums = [1,4,3,7,4,5], k = 3
输出：15
解释：最优子数组的左右端点下标是 (1, 5) ，分数为 min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15 。
示例 2：

输入：nums = [5,5,4,5,4,1,1,1], k = 0
输出：20
解释：最优子数组的左右端点下标是 (0, 4) ，分数为 min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20 。


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length
"""
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = k, k
        res, cumin, l = 0, nums[k], 1
        for i in range(n):
            res = max(cumin * l, res)

            if left > 0 and right < n - 1:
                if nums[left-1] >= nums[right+1]:
                    left -= 1
                else:
                    right += 1
            elif left > 0:
                left -= 1
            elif right < n - 1:
                right += 1
            else:
                break
            cumin = min(cumin, nums[left], nums[right])
            l += 1
        return res
# 官解
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right, i = k - 1, k + 1, nums[k]
        ans = 0
        while True:
            while left >= 0 and nums[left] >= i:
                left -= 1
            while right < n and nums[right] >= i:
                right += 1
            ans = max(ans, (right - left - 1) * i)
            i = max((-1 if left == -1 else nums[left]), (-1 if right == n else nums[right]))
            if i == -1:
                break
        return ans


s = Solution()
# s.maximumScore(nums = [1,4,3,7,4,5], k = 3)
s.maximumScore(nums = [6569,9667,3148,7698,1622,2194,793,9041,1670,1872], k = 5)