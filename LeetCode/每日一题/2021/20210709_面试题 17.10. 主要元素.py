#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210709_面试题 17.10. 主要元素.py
# @Author: Lin
# @Date  : 2021/7/10 12:20
# 数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。
#
#  
#
# 示例 1：
#
# 输入：[1,2,5,9,5,9,5,5,5]
# 输出：5
# 示例 2：
#
# 输入：[3,2]
# 输出：-1
# 示例 3：
#
# 输入：[2,2,1,1,1,2,2]
# 输出：2
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        nums = Counter(nums)
        for i in nums:
            if nums[i] > l//2:
                return i
        else:
            return -1


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 狼人杀归票算法
        # 第一轮找到最可能出局的那个人
        n = len(nums)
        ans = -1
        count = 0
        for num in nums:
            # 没有票数，暂时认为是当前的人
            if not count:
                ans = num
            # 有相同的人上票，票数加一；否则票数减一
            if num == ans:
                count += 1
            else:
                count -= 1
        # 第二轮确定这个人的票数确实过半
        return ans if nums.count(ans) > n // 2 else -1
