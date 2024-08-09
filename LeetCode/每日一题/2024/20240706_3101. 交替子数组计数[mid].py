#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240706_3101. 交替子数组计数[mid].py
# @Author  ：Lin
# @Date    ：2024/7/6 10:30


"""给你一个
二进制数组
nums 。
如果一个
子数组
中 不存在 两个 相邻 元素的值 相同 的情况，我们称这样的子数组为 交替子数组 。
返回数组 nums 中交替子数组的数量。
示例 1：
输入： nums = [0,1,1,1]
输出： 5
解释：
以下子数组是交替子数组：[0] 、[1] 、[1] 、[1] 以及 [0,1] 。
示例 2：
输入： nums = [1,0,1,0]
输出： 10
解释：
数组的每个子数组都是交替子数组。可以统计在内的子数组共有 10 个。
提示：
1 <= nums.length <= 105
nums[i] 不是 0 就是 1 。"""
from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        res = 0
        # 双指针
        while left < n and right < n:
            right += 1
            # 每次都寻找以left为起点的最大交替子数组,设长度为m
            # 该数组的 交替子数组数量为 m * (m + 1) // 2
            while right < n and nums[right - 1] ^ nums[right]:
                right += 1
            m = right - left
            res += m * (m + 1) // 2
            left = right
        return res

s = Solution()
s.countAlternatingSubarrays(nums = [1,0,1,0])

