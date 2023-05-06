#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 4 天.py
# @Author: Lin
# @Date  : 2023/3/21 17:50

# 69. x 的平方根
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
#
# 示例 1：
#
# 输入：x = 4
# 输出：2
# 示例 2：
#
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
#  
#
# 提示：
#
# 0 <= x <= 231 - 1
from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = (right - left) // 2 + left
            print(mid, left, right)

            square = mid ** 2
            if square > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


s = Solution()
s.mySqrt(x = 16)

# 744. 寻找比目标字母大的最小字母
# 给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。
# 返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。
# 示例 1：
# 输入: letters = ["c", "f", "j"]，target = "a"
# 输出: "c"
# 解释：letters 中字典上比 'a' 大的最小字符是 'c'。
# 示例 2:
# 输入: letters = ["c","f","j"], target = "c"
# 输出: "f"
# 解释：letters 中字典顺序上大于 'c' 的最小字符是 'f'。
# 示例 3:
# 输入: letters = ["x","x","y","y"], target = "z"
# 输出: "x"
# 解释：letters 中没有一个字符在字典上大于 'z'，所以我们返回 letters[0]。
# 提示：
#
# 2 <= letters.length <= 104
# letters[i] 是一个小写字母
# letters 按非递减顺序排序
# letters 最少包含两个不同的字母
# target 是一个小写字母


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            print(left, right)
        return letters[left] if left < n else letters[0]


s = Solution()
s.nextGreatestLetter(letters = ["x","x","y","y"], target = "z")




class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        if letters[right] <= target:
            return letters[0]
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] == target and letters[mid+1] > target:
                return letters[mid+1]
            elif letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left]



















