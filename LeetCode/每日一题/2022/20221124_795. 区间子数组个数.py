#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20221124_795. 区间子数组个数.py
# @Author: Lin
# @Date  : 2022/11/25 9:43

# 给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。
# 生成的测试用例保证结果符合 32-bit 整数范围。
# 示例 1：
# 输入：nums = [2,1,4,3], left = 2, right = 3
# 输出：3
# 解释：满足条件的三个子数组：[2], [2, 1], [3]
# 示例 2：
# 输入：nums = [2,9,2,5,6], left = 2, right = 8
# 输出：7
# 提示：
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= left <= right <= 109
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        arr = []
        for n in nums:
            if left <= n <= right:
                ...




s = Solution()
s.numSubarrayBoundedMax(nums = [2,9,2,5,6], left = 2, right = 8)