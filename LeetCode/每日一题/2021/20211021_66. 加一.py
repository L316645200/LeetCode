#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211021_66. 加一.py
# @Author: Lin
# @Date  : 2021/10/21 9:59
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1：
#
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 示例 2：
#
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 示例 3：
#
# 输入：digits = [0]
# 输出：[1]
#  
# 提示：
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        carry = 1
        while carry == 1 and n >= 0:
            t = digits[n] + 1
            digits[n] = t % 10
            carry = t // 10
            n = n - 1
        if carry == 1:
            digits.insert(0, 1)
        return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.insert(0, 1)
        return digits

s = Solution()
res = s.plusOne([1,2,3])