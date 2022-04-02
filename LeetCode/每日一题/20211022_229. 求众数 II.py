#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211022_229. 求众数 II.py
# @Author: Lin
# @Date  : 2021/10/22 9:32
# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
#
# 示例 1：
#
# 输入：[3,2,3]
# 输出：[3]
# 示例 2：
#
# 输入：nums = [1]
# 输出：[1]
# 示例 3：
#
# 输入：[1,1,1,3,3,2,2,2]
# 输出：[1,2]
#
# 提示：
#
# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
#  
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        cri = len(nums) / 3
        res = []
        for k, c in count.items():
            if c > cri:
                res.append(k)
        return res



# 摩尔投票法:不同的数字作为一组消除掉,剩下的数字即为众数
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = 0, 0
        vote1, vote2 = 0, 0
        for n in nums:
            if num1 == n and vote1 > 0:
                vote1 += 1
            elif num2 == n and vote2 > 0:
                vote2 += 1
            elif vote1 == 0:
                num1 = n
                vote1 = 1
            elif vote2 == 0:
                num2 = n
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1
        cnt1, cnt2 = 0, 0
        for n in nums:
            if n == num1 and vote1 > 0:
                cnt1 += 1
            if n == num2 and vote2 > 0:
                cnt2 += 1
        arr = []
        if cnt1 > len(nums) / 3:
            arr.append(num1)
        if cnt2 > len(nums) / 3:
            arr.append(num2)
        return arr


s = Solution()
s.majorityElement([2,1,1,3,1,4,5,6])