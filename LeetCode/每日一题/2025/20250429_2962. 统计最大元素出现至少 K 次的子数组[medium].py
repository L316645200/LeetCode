#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/29 19:42
# @Author  : Lin
# @File    : 20250429_2962. 统计最大元素出现至少 K 次的子数组[medium].py

"""给你一个整数数组 nums 和一个 正整数 k 。

请你统计有多少满足 「 nums 中的 最大 元素」至少出现 k 次的子数组，并返回满足这一条件的子数组的数目。

子数组是数组中的一个连续元素序列。



示例 1：

输入：nums = [1,3,2,3,3], k = 2
输出：6
解释：包含元素 3 至少 2 次的子数组为：[1,3,2,3]、[1,3,2,3,3]、[3,2,3]、[3,2,3,3]、[2,3,3] 和 [3,3] 。
示例 2：

输入：nums = [1,4,2,1], k = 3
输出：0
解释：没有子数组包含元素 4 至少 3 次。


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105"""
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        res = left = cnt = 0
        for right, x in enumerate(nums):
            if x == m:
                cnt += 1
            while cnt == k:
                if nums[left] == m:
                    cnt -= 1
                left += 1
            res += left
        return res


s = Solution()
s.countSubarrays(nums = [1,3,2,3,3], k = 2)
