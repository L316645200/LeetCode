#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210804_611. 有效三角形的个数.py
# @Author: Lin
# @Date  : 2021/8/4 11:59
# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
#
# 示例 1:
#
# 输入: [2,2,3,4]
# 输出: 3
# 解释:
# 有效的组合是:
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
# 注意:
#
# 数组长度不超过1000。
# 数组里整数的范围为 [0, 1000]。
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        nums.sort()
        s = 0
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                r = nums[i] + nums[j]
                left, right = j + 1, l - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] >= r:
                        right = mid - 1
                    else:
                        left = mid + 1
                s += left - j - 1
        return s
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        nums.sort()
        s = 0
        for i in range(l):
            k = i
            for j in range(i+1, l):
                while k + 1 < l and nums[i] + nums[j] > nums[k+1]:
                    k += 1
                s += max(k-j, 0)
        return s

s = Solution()
s.triangleNumber([2,2,3,4])
