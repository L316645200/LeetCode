#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：3.3 背向双指针.py
# @Author  ：Lin
# @Date    ：2024/11/23 15:41

"""两个指针从数组中的同一个位置出发，一个向左，另一个向右，背向移动。"""
from typing import List

"""1793. 好子数组的最大分数 1946"""
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
0 <= k < nums.length"""


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left, right = k - 1, k + 1
        res = mi = nums[k]
        n = len(nums)
        while left >= 0 or right < n:

            if left < 0:
                mi = min(mi, nums[right])
                right += 1
            elif right >= n:
                mi = min(mi, nums[left])
                left -= 1
            else:
                if nums[left] >= nums[right]:
                    mi = min(mi, nums[left])
                    left -= 1
                else:
                    mi = min(mi, nums[right])
                    right += 1

            res = max(res, mi * (right - left - 1))
        return res


"""由于好子数组必须包含nums[k]，我们可以使用两个指针left和right,
且初始值都分别为k-1，k+1
在指针未超出边界前，
如果 nums[left] < nums[right],那么右指针向右移动，
因为右指针向右移动 子数组的分数最小是 (right - left) * nums[right]
而如果向左移动，子数组的分数最小是 (right - left) * nums[left]
那么 (right - left) * nums[left] < (right - left) * nums[right];
反之亦然；
当指针超出边界时，左指针超出边界就去移动右指针，反之亦然
"""
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = right = k
        res = mi = nums[k]
        n = len(nums)
        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] >= nums[right + 1]:
                left -= 1
            else:
                right += 1
            mi = min(mi, nums[left], nums[right])
            res = max(res, mi * (right - left + 1))
        return res


s = Solution()
s.maximumScore(nums = [1,4,3,7,4,5], k = 3)